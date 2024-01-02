import os
import re
import time
from collections import deque
from urllib.parse import urljoin, urlparse

import html2text
import requests
import streamlit as st

from AdvancedHTMLParser import AdvancedHTMLParser, AdvancedTag

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from statwords import Items, StatusItem
from webdriver_manager.chrome import ChromeDriverManager

from statwords import Items, StatusItem

st.set_page_config("Minor Scrapes", "🔪", "wide")
st.title("Minor Scrapes")

STATE = st.session_state


SCRAPE_TOP      = st.columns([0.618, 0.01, 0.372])
SCRAPE_PROGRESS = SCRAPE_TOP[0].empty()
PROGRESS_ITEM   = SCRAPE_TOP[0].empty()
COLUMNS         = st.columns([0.618, 0.01, 0.372])
NOTIFICATION3   = SCRAPE_TOP[2].empty()
NOTIFICATION4   = SCRAPE_TOP[2].empty()
RIGHT_TABLE     = COLUMNS[2].container()
LEFT_TOP        = COLUMNS[0].container()
LEFT_TABLE      = COLUMNS[0].container()
LEFT_SHOW       = COLUMNS[0].empty()


OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--headless=new")
OPTIONS.add_experimental_option(
    "mobileEmulation",
    {
        "deviceMetrics": {"width": 512, "height": 864, "pixelRatio": 1.0},
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
        "clientHints": {"platform": "Android", "mobile": True},
},)

DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)

DRIVER.implicitly_wait(10)
DRIVER.set_script_timeout(20)
DRIVER.set_page_load_timeout(20)

def load_page(url):
    DRIVER.get(url)
    return DRIVER.page_source

def get_hyperlinks(local_domain, url):
    rendered_html = load_page(url)
    parser = BeautifulSoup(rendered_html, "html5lib")
    links = parser.find_all("a")
    clean_links = [urljoin(url, link.get("href")) for link in links if link.get("href")]
    return [link for link in clean_links if link.startswith(f"https://{local_domain}")]

def get_domain_hyperlinks(local_domain, url):
    return {
        urljoin(
            f"https://{local_domain}/", urlparse(link, "https", allow_fragments=True).path
        ).rstrip("/")
        for link in get_hyperlinks(local_domain, url)
    }


def convert_to_safe_url(text):
    return re.sub(r"[^a-zA-Z0-9_-]", "_", text).strip()

def add_https(url):
    return url if url.startswith("http") else f"https://{url}"

STATE.HTML_TAGS_LIST = [
    "a",
    "aside",
    "article",
    "blockquote",
    "caption",
    "code",
    "dialog",
    "div",
    "embed",
    "figure",
    "footer",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "head",
    "head",
    "header",
    "hgroup",
    "html",
    "i",
    "iframe",
    "img",
    "ins",
    "label",
    "li",
    "link",
    "main",
    "menu",
    "meta",
    "nav",
    "object",
    "ol",
    "p",
    "pre",
    "script",
    "section",
    "style",
    "svg",
    "table",
    "ul",
    "video",
]

STATE.annotations = {
    "action": "Specifies the URL where the form data should be submitted.",
    "alt": "Provides an alternate text for an image.",
    "content": "Specifies the value of the meta tag.",
    "data": "Allows you to store custom data attributes.",
    "href": "Specifies the URL of a linked resource.",
    "id": "Provides a unique identifier for an element.",
    "src": "Specifies the URL of an external resource, such as an image or script.",
    "class": "Allows you to target elements by their class names.",
    "name": "Sets a name for an input field, form, or iframe.",
    "value": "Specifies the value of an input field or a button.",
}


def get_code_language(tag: AdvancedTag):
    languages = [
        "abap",
        "actionscript",
        "ada",
        "apex",
        "applescript",
        "assembly",
        "awk",
        "bash",
        "batchfile",
        "c",
        "c#",
        "c++",
        "cobol",
        "css",
        "cuda",
        "dart",
        "elixir",
        "elm",
        "erlang",
        "go",
        "gradle",
        "groovy",
        "haskell",
        "html",
        "java",
        "javascript",
        "julia",
        "kotlin",
        "less",
        "lisp",
        "lua",
        "matlab",
        "objective-c",
        "pascal",
        "perl",
        "php",
        "powershell",
        "prolog",
        "protobuf",
        "python",
        "r",
        "ruby",
        "rust",
        "scala",
        "scheme",
        "shell",
        "solidity",
        "sql",
        "swift",
        "tcl",
        "typescript",
        "xml",
        "yaml",
    ]
    has_class = tag.hasAttribute("class")
    if has_class:
        for class_name in tag["class"]:
            if class_name in languages:
                return class_name
            for language in languages:
                if language in class_name:  ## may be inaccurate
                    return language
            if class_name.startswith("language-"):
                return class_name.replace("language-", "")
    return None


def format_tables(content, replacements):
    tables = BeautifulSoup(content, "html.parser")
    caption = re.search(r"<caption[^>]*>((?:.|\n)*)<\/caption>", content, re.IGNORECASE)
    if caption:
        for c in range(len(caption.groups())):
            st.write(caption)
            content.replace(caption.groups()[c], f" ")
    tables = re.findall(r"(<table[^>]*?>.*?<\/table>)", content, re.DOTALL)
    for t, table in enumerate(tables):
        markdown = html2text.HTML2Text().handle(table)
        placeholder = f"tableplaceholder{t}{hash(markdown)}"
        replacements.append({"placeholder": placeholder, "replacement": markdown})
        content = content.replace(table, f"<p>{placeholder}</p>")
    return content


def remove_captions(content):
    caption = re.search(r"(<caption[^>]*?>[^<]*?<\/caption>)", content, re.IGNORECASE)
    if caption:
        for c in range(len(caption.groups())):
            st.code(caption)
            content.replace(caption.group(c), f" ")
    return content

def process_dom(content):
    replacements = []
    content = format_tables(content, replacements)
    if content:
        for replacement in replacements:
            old_part = replacement["placeholder"]
            new_part = replacement["replacement"]
            content = content.replace(old_part, new_part)
    return content

import json


def convert_to_absolute_url(html, base_url):
    soup = BeautifulSoup(html, "html.parser")

    for img_tag in soup.find_all("img"):
        if img_tag.get("src"):
            src = img_tag.get("src")
            if src.startswith(("http://", "https://")):
                continue
            absolute_url = urljoin(base_url, src)
            img_tag["src"] = absolute_url
        elif img_tag.get("data-src"):
            src = img_tag.get("data-src")
            if src.startswith(("http://", "https://")):
                continue
            absolute_url = urljoin(base_url, src)
            img_tag["data-src"] = absolute_url

    for link_tag in soup.find_all("a"):
        href = link_tag.get("href")
        if href:
            if href.startswith(("http://", "https://")):
                continue
            absolute_url = urljoin(base_url, href)
            link_tag["href"] = absolute_url

    return str(soup)

def load_urls(base):
    save_folder = f"./markdown/{base}/urls.json"
    try:
        with open(save_folder, 'r') as f:
            sites = json.loads(f.read())
            return sites
    except FileNotFoundError:
        return []


def store_urls(base, urls):
    save_folder = f"./markdown/{base}/urls.json"
    content = json.dumps(urls)
    try:
        with open(save_folder, 'w') as f:
            NOTIFICATION3.success(f"Saved {urls[-1]}\n to {save_folder}")
            f.write(content)


    except FileNotFoundError:
        NOTIFICATION3.error(f"Could not save {content} to {save_folder}")

def crawl_website(url, filter_criteria={}, do_save=False, up_level=False, overwrite=False):
    """
    Crawls a website and saves or displays the content.
    """
    start_time = time.time()
    item_prog = PROGRESS_ITEM.progress(text="Crawling", value=0.0)

    mdconvert                 = html2text.HTML2Text()
    mdconvert.ignore_links    = True
    mdconvert.ignore_images   = True
    mdconvert.ignore_tables   = False
    mdconvert.ignore_emphasis = False
    mdconvert.body_width      = 200
    mdconvert.mark_code       = True

    url          = add_https(url)
    local_domain = urlparse(url).netloc
    local_path   = urlparse(url).path
    parts        = len(local_path.split("/")[1:])
    home_url           = str(os.path.split(url)[0])

    folder_path = url.split("://")[1]


    if parts >= 2 and up_level:
        home_url = os.path.split(home_url)[0]

    queue = deque([url])
    seen = set()
    converted = set() if overwrite else set(load_urls(folder_path) )

    if not os.path.exists("processed"):
        os.mkdir("processed")

    progress = SCRAPE_PROGRESS.progress(text="Crawling", value=1.0)

    data = {"resp_code": None, "downloaded": None, "remaining": None, "saving": ""}

    stattable = LEFT_TOP.empty()
    statsvals = Items()
    statsvals.add_item(StatusItem("resp_code"))
    statsvals.add_item(StatusItem("finished"))
    statsvals.add_item(StatusItem("pending"))
    statsvals.add_item(StatusItem("saving"))

    split_column = int(st.session_state.get("colsplit", 1))
    result_columns = st.columns(split_column)
    i = 0

    while queue:
        url = queue.pop()

        current_column = i
        local_path = os.path.join(local_domain, urlparse(url).path)

        item_prog.progress(0.1, text="Checking if already processed")

        parent_path, path_tail = (
            os.path.split(local_path) if "/" in local_path else (None, local_path)
        )

        item_prog.progress(0.1, text=f"Getting new hyperlinks in {parent_path}")

        for link in get_domain_hyperlinks(local_domain, url):
            if not overwrite and link in converted:
                continue
            if (link in seen) or folder_path not in link:
                continue
            queue.append(link)
            seen.add(link)
            NOTIFICATION4.write(f"Added {link} to queue")

        if url in converted:
            continue
        save_folder = f"markdown/{local_domain}{parent_path}"
        base_filename = f"{save_folder}/{convert_to_safe_url(path_tail)}"

        if do_save:
            os.makedirs(save_folder, exist_ok=True)
        content = None

        def update_status(data):
            value0 = data["resp_code"]
            value1 = data["downloaded"]
            value2 = data["remaining"]
            value3 = data["saving"]
            statsvals.items[0].response_code(value0)
            statsvals.items[2].set("pending", value2)
            statsvals.items[1].set("downloaded", value1)
            statsvals.items[3].set("saving", value3)

            progress.progress(
                max(
                    i / (1 + i + len(queue)),
                    max(0, i - len(queue)) / (1 + i + len(queue)),
                ),
                text=f":orange[{value3}]",
            )


        stattable.table([s.display for s in statsvals.items])
        item_prog.progress(0.25, text="Downloading Page")


        PARSER: AdvancedHTMLParser = AdvancedHTMLParser()


        def fetch_content(url, data):
            content = load_page(url)
            data["resp_code"] = requests.get(url, timeout=5).status_code
            data["downloaded"] = i
            data["remaining"] = 1 + len(queue)
            data["saving"] = local_path
            return content, data

        try:
            content, data = fetch_content(url, data)
            update_status(data)
        except Exception as e:
            data["saving"] = f"{url} - {e}"
            update_status(data)
            continue

        item_prog.progress(0.5, text="Parsing")
        PARSER.parseStr(convert_to_absolute_url(content, url))

        def get_language(input):
            langs = [
                "python",
                "bash",
                "java",
                "sh",
                "javascript",
                "c++",
                "c#",
                "ruby",
                "php",
                "go",
                "swift",
                "kotlin",
                "typescript",
                "rust",
                "html",
                "css",
                "shell",
                "sql",
                "r",
                "matlab",
                "perl",
                "scala",
            ]
            regex = r"((?=\<(code|div|pre)\s+(\w+\=\"((?:\s+).*?)+\")?[^\>]+\>).*?<\/\2>)"
            items = re.finditer(regex, input)
            language = ""
            if items:
                for item in items:
                    language = next((x for x in langs if x in item.group(2)), "python")
                return language

        def filter_tags(parser: AdvancedHTMLParser, filters):

            if "include" in filters:
                item_prog.progress(0.7, "including tags")
                for include_tag in filters["include"]:
                    tag_name = include_tag["name"]
                    values = [
                        value
                        for attribute in include_tag["attributes"]
                        for value in attribute["values"]
                    ]
                    selector = f"{tag_name}{'.' + '.'.join(values) if values else ''}"
                    for element in parser.getElementsByClassName(selector):
                        element.attributes.clear()

            if "exclude" in filters:
                item_prog.progress(0.8, "Excluding tags")
                for exclude_tag in filters["exclude"]:
                    tag_name = exclude_tag["name"]
                    values = [
                        value
                        for attribute in exclude_tag["attributes"]
                        for value in attribute["values"]
                    ]
                    selector = f"{tag_name}{'.' + '.'.join(values) if values else ''}"
                    for element in parser.getElementsByTagName(selector):
                        element.parentNode.removeChild(element)

            tags = set()
            replacement = {}  ## {"old": "new"}
            for tag in parser.createBlocksFromHTML(parser.getHTML()):
                language = None
                if tag is None:
                    continue
                item = tag if isinstance(tag, str) else tag.outerHTML
                if "<table" in item:
                    item = remove_captions(item)
                    table = mdconvert.handle(item)
                    replacement[item] = table

                try:
                    if isinstance(tag, AdvancedTag):
                        language = get_code_language(tag)
                except:
                    language = get_language(item)
                tags.add(tag)
                old = mdconvert.handle(item)
                new = old.replace("[code]", f"\n```{language}\n\n\n")
                new = new.replace("[/code]", "\n\n```\n")
                replacement[old] = new

            return parser.getHTML(), replacement

        item_prog.progress(0.6, text="Filering Page")
        htmlout, replacements = filter_tags(PARSER, filter_criteria)

        VIEWDOC = LEFT_SHOW.empty()

        if not do_save:
            VIEWDOC = result_columns[current_column % split_column].expander(
                f":green[ {i} - {url} ]", expanded=False
            )

        item_prog.progress(0.85, text="Converting Page")
        md_output = mdconvert.handle(htmlout)

        item_prog.progress(0.9, text="Checking for Source Code")
        for key, value in replacements.items():
            md_output = md_output.replace(key, value)

        item_prog.progress(0.95, text="Saving")

        if md_output:
            item_prog.progress(1.0, text=f"Page {i} Done {url}")

        if STATE.ALLOW_IMG:
            VIEWDOC.markdown(md_output, unsafe_allow_html=STATE.ALLOW_HTML)

        if do_save and (overwrite or not os.path.exists(f"{base_filename}.md")):
            with open(f"{base_filename}.md", "w", encoding="UTF-8") as file:
                file.write(md_output)

        i += 1
        converted.add(url)
        STATE["scraped_sites"].append(url)
        time.sleep(0.3)

        if do_save:
            urls = list(converted)
            store_urls(folder_path, urls)

    NOTIFICATION4.empty()
    time.sleep(2)
    stattable.empty()
    item_prog.empty()
    progress.empty()
    progress.info(f"Done, saved in {folder_path}:\n {i} Sites in {time.time() - start_time} seconds")
    return i

PRESETS_FOLDER = "presets"


# Create initial tag instance
def update_includes():
    for tag in STATE.HTML_TAGS_LIST:
        if tag in STATE.incl_tag_set:
            if tag not in STATE.include_tags:
                STATE.include_tags[tag] = {"name": tag, "attributes": []}
        elif tag in STATE.include_tags.keys():
            del STATE.include_tags[tag]

        if tag in STATE.excl_tag_set:
            if tag not in STATE.exclude_tags:
                STATE.exclude_tags[tag] = {"name": tag, "attributes": []}
        elif tag in STATE.exclude_tags.keys():
            del STATE.exclude_tags[tag]

    st.session_state["filter_dict"]["include"] = list(STATE.include_tags.values())
    st.session_state["filter_dict"]["exclude"] = list(STATE.exclude_tags.values())
    if st.session_state.get("arria", False) is True:
        st.session_state["filter_dict"]["exclude"].extend([
            {"name": "div", "attributes": [{"name": "aria-label", "values": ["navigation"]}]},
            {"name": "span", "attributes": [{"name": "aria-label", "values": ["navigation"]}]},
            {"name": "i", "attributes": [{"name": "aria-hidden", "values": ["true"]}]},
        ])


def main():
    """
    The main function that runs the web scraping application.
    """

    # larger area view
    main_area = LEFT_TABLE.container()
    main_top = main_area.container()
    main_bottom = main_area.container()
    main_top_columns = main_top.columns([9, 0.1, 9])
    main_bottom_expander = main_bottom.expander("Expand Instructions Here")
    main_bot_help = main_bottom_expander.container()
    main_bot_columns = main_bottom_expander.columns([9, 0.1, 9])

    # side view
    inclusivity_execution = COLUMNS[2].container()
    inclusivity = COLUMNS[2].container()
    inclusivity.divider()
    inclusivity_attributes = COLUMNS[2].container()
    upper_tag = inclusivity.columns([1, 0.01, 1])
    middle_attr = inclusivity.columns([1, 0.01, 1])
    lowerr_edit = inclusivity_attributes.columns([1, 0.01, 1])

    st.session_state["ran"] = st.session_state.get("ran", None)

    url = LEFT_TOP.text_input(
        "URL",
        placeholder="https://www.example.com",
        value="https://example.com",
        label_visibility="collapsed",
    )

    params = st.experimental_get_query_params()

    if "dev" in params and params["dev"][0] == st.secrets.dev.password:
        testin = inclusivity_execution.selectbox(
            "URL",
            [
                "https://nicegui.io/documentation/section_text_elements",
                "https://pygithub.readthedocs.io/en/stable/examples/MainClass.html",
                "https://python.langchain.com/docs/expression_language/interface",
                "https://docs.embedchain.ai/data-sources/docs-site",
        ],)
        if inclusivity_execution.checkbox("Test"):
            url = testin

    main_bot_help.markdown(
        """
            `https://python.langchain.com/docs/expression_language/interface`

            # Add specific attributes for tags..
            1. Enter a URL ( the... `http://` is optional )
            2. Select HTML tag to add Attribute
            3. Select an attribute
            4. Enter a Value to search for that Attr.
            5. Click to Add to the content.

            ### 'Crawl It' ... will  :
            - Crawl the website and display,
            - Fill a markdown folder.
        """
    )

    if url and url.endswith("/"):
        url = url[:-1]

    parsed_folders = os.path.split(urlparse(url).path)[0]

    # Choices allow scraping to expand to one directtor abovev the path.
    up_level = main_top_columns[2].checkbox("Allow parent path?")
    overwrite = main_top_columns[2].checkbox("Overwrite?")
    STATE.ALLOW_IMG = main_top_columns[0].checkbox(
        "Show Previews?", help="Allows Images in the Renderoutput"
    )
    STATE.ALLOW_HTML = main_top_columns[2].checkbox(
        "Allow HTML?", help="Allows HTML in the Renderoutput"
    )
    if up_level:
        parsed_folders = os.path.split(urlparse(parsed_folders).path)[0]

    do_save = main_top_columns[0].checkbox(
        f"Dowwnload to drive?",
        help="Obv disabled  for cloud server, but handy at home..",
        key="do_save",
    )

    main_top_columns[2].markdown(f":blue[.../markdown/{urlparse(url).netloc}{parsed_folders}]")

    main_top_columns[0].markdown(

        """
        :red[ Saving is disabled on demo for obvious space saving reasons ]
        """
    )

    STATE.annotations = {
        "action": "Specifies the URL where the form data should be submitted.",
        "alt": "Provides an alternate text for an image.",
        "content": "Specifies the value of the meta tag.",
        "data": "Allows you to store custom data attributes.",
        "href": "Specifies the URL of a linked resource.",
        "id": "Provides a unique identifier for an element.",
        "src": "Specifies the URL of an external resource, such as an image or script.",
        "class": "Allows you to target elements by their class names.",
        "name": "Sets a name for an input field, form, or iframe.",
        "value": "Specifies the value of an input field or a button.",
    }

    STATE.setting_tags = STATE.get("setting_tags", [])
    STATE.include_tags = STATE.get("include_tags", {})
    STATE.exclude_tags = STATE.get("exclude_tags", {})

    st.session_state["filter_dict"] = st.session_state.get(
        "filter_dict", {"include": [], "exclude": []}
    )

    upper_tag[0].write("### :green[🗟⇪] :blue[Include]")
    upper_tag[2].write("### :red[🗑⇣] :orange[Blocked]")

    upper_tag[0].multiselect(
        "",
        STATE.HTML_TAGS_LIST,
        ["div", "code", "article"],
        key="incl_tag_set",
        label_visibility="collapsed",
        on_change=update_includes,
    )

    upper_tag[2].multiselect(
        "",
        STATE.HTML_TAGS_LIST,
        [
            "style",
            "script",
            "head",
            "footer",
            "nav",
            "caption",
            "menu",
            "label",
            "head",
            "header",
            "object",
            "figure",
            "embed",
            "i"
        ],
        key="excl_tag_set",
        label_visibility="collapsed",
        on_change=update_includes,
    )

    middle_attr[0].radio(
        ":green[Include] Tag to Edit ",
        STATE.include_tags.keys(),
        key="incl_select_tag",
        horizontal=True,
    )

    middle_attr[2].radio(
        ":red[Exclude] Tag to Edit ",
        STATE.exclude_tags.keys(),
        horizontal=True,
        key="excl_select_tag",
    )
    if not st.session_state["ran"]:
        update_includes()
        st.session_state["ran"] = True

    def edit_tag(loc, tag_inp, side):
        attr = STATE.get("attrib", " ")

        val: str = loc.text_input(
            "",
            placeholder=f'<{tag_inp} "{attr}"=thisvalue',
            label_visibility="collapsed",
            key=f"{side}_strinp3",
        )

        col = ":green" if side == "include" else ":red"

        astrt = (attr + '="' + val + '"') if attr else " "
        button_string = f"{col}[{side}] <{tag_inp} {astrt}>"

        # Add new attribute button
        if loc.button(button_string, key=f"{side}_add_attribute_button"):
            if tag_inp in STATE.get(f"{side}_tags"):
                STATE[f"{side}_tags"][tag_inp]["attributes"].append({"name": attr, "values": [val]})

        # add value to attribute  in N slot of tag

        clrthis = f"{col}[All ]"
        for tag in STATE.get(f"{side}_tags", {}).values():
            attributes: list = tag.get("attributes", [])

            loc.markdown(f"""{clrthis if len(attributes) == 0 else ""}   { tag.get("name") } """)
            if len(attributes) > 0:
                for attr in attributes:
                    atrtname = attr.get("name")
                    atrtvals = ", ".join(attr.get("values"))
                    loc.write(f" - {atrtname}: {atrtvals}")

        # clear attribute button
        if loc.button(":red[Clear]", key=f"{side}_clear_attribute_button"):
            STATE[f"{side}_tags"][tag_inp]["attributes"] = []

        update_includes()

    edit_tag(lowerr_edit[0], STATE.get("incl_select_tag", ""), "include")
    edit_tag(lowerr_edit[2], STATE.get("excl_select_tag", ""), "exclude")

    with main_bot_columns[0]:
        st.json(st.session_state["filter_dict"]["include"])
    with main_bot_columns[2]:
        st.checkbox("Aria Tweak?", True, key="arria", on_change=update_includes)
        st.json(st.session_state["filter_dict"]["exclude"])

    # Display the dataframe
    do_save = st.session_state.get("do_save", False)

    crawl_execute = RIGHT_TABLE.button("Crawl It", use_container_width=True, type="secondary")
    inclusivity_execution.slider("Columns...", 1, 5, 2, 1, key="colsplit")

    inclusivity.write(STATE.annotations.get(STATE.get("attrib", ""), ""))
    if crawl_execute:
        STATE["scraped_sites"] = STATE.get("scraped_sites", [])
        converted = crawl_website(url, st.session_state["filter_dict"], do_save, up_level,overwrite)
        SCRAPE_PROGRESS.info("Crawling complete!")
        time.sleep(2)
        SCRAPE_PROGRESS.empty()

        with NOTIFICATION3.expander(f"{converted} Sites Finished"):
            st.markdown("\n".join(STATE.get("scraped_sites", [])))


    inclusivity.radio(
        ":blue[Attribute] Tag to Edit",
        STATE.annotations.keys(),
        horizontal=True,
        key="attrib",
    )


if __name__ == "__main__":
    main()
