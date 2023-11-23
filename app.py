import os
import re
import time
from collections import deque
from urllib.parse import urljoin, urlparse

import mdformat
import requests
import streamlit as st
from AdvancedHTMLParser import AdvancedTag, IndexedAdvancedHTMLParser as AdvancedHTMLParser
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.util import ClassNotFound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from statwords import Items, StatusWordItem
from webdriver_manager.chrome import ChromeDriverManager

st.set_page_config("Minor Scrapes", "🔪", "wide")
STATE = st.session_state
st.title("Minor Scrapes")
NOTIFICATION = st.empty()
NOTIFICATION2 = st.empty()
COLUMNS = st.columns([0.618, 0.01, 0.372])
LEFT_TABLE = COLUMNS[0].empty()
BLOCK_ARIA_HIDDEN = COLUMNS[0].checkbox(
    "Block aria-hidden", key="block_aria_hidden", value=True, help="Block tags with aria-hidden"
)


def detect_language(code):
    try:
        lexer = get_lexer_by_name("text")
        lexer = guess_lexer(code)
        return lexer.name.lower()
    except ClassNotFound:
        return "Unknown"


OPTIONS = webdriver.ChromeOptions()
OPTIONS.add_argument("--headless=new")  # Hide the browser window
MOBILE_EMULATION = {
    "deviceMetrics": {"width": 1280, "height": 720, "pixelRatio": 3.0},
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
    "clientHints": {"platform": "Android", "mobile": True},
}

OPTIONS.add_experimental_option("mobileEmulation", MOBILE_EMULATION)

DRIVER = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=OPTIONS)
DRIVER.implicitly_wait(3)

def load_page(url):
    DRIVER.get(url)
    # Wait for the page to load, when load is hit, continue the script
    return DRIVER.page_source


def get_hyperlinks(local_domain, url):
    DRIVER.get(url)
    rendered_html = DRIVER.page_source
    parser = BeautifulSoup(rendered_html, "html5lib")
    links = parser.find_all("a")
    clean_links = []
    for link in links:
        st.write(link.get("href"))
        if href := link.get("href"):
            cleaned_link = urljoin(url, href)
            if cleaned_link.endswith("/"):
                cleaned_link = cleaned_link[:-1]
            if cleaned_link.startswith(f"https://{local_domain}"):
                clean_links.append(cleaned_link)
    return clean_links


def get_domain_hyperlinks(local_domain, url):
    clean_links = set()
    for link in set(get_hyperlinks(local_domain, url)):
        url_obj = urlparse(link, "https", allow_fragments=False)
        # Check if the domain is the same or if it's a relative link
        if url_obj.netloc == local_domain or not url_obj.netloc:
            full_url = urljoin(f"https://{local_domain}/", url_obj.path)
            clean_links.add(full_url.rstrip("/"))

    return clean_links


CONVERTER = MarkdownConverter(default_title=False, escape_asterisks=False, escape_underscores=False)


def convert_to_markdown(tag: AdvancedTag) -> str:
    """
    Converts the input tag to Markdown format.
    If code or pre tag, check for a language attribute or a common language used in attributes.

    Args:
        tag (bs4.Tag): The BeautifulSoup Tag object to be converted.

    Returns:
        str: The converted Markdown text.
    """

    if tag.tagName not in ["pre", "code", "div"]:
        return CONVERTER.convert(tag.asHTML())

    language = next(
        (value.replace("language-", "") for value in tag.getAttributesDict().get("class", [])), None
    )
    if tag.name == "div":
        return mdformat.text(CONVERTER.convert(tag.getHTML()))

    CONVERTER.options["code_language"] = language or detect_language(tag.text)
    return mdformat.text(CONVERTER.convert_soup(BeautifulSoup(tag.getHTML(), "html.parser")))


def convert_to_safe_url(text):
    """
    Converts a text into a safe URL format.

    Args:
        text (str): The text to be converted.

    Returns:
        str: The converted safe URL.
    """
    subst = "_"
    regex = r"[^a-zA-Z0-9-_]|\:"
    return re.sub(regex, subst, text, 0, re.DOTALL)

def add_https(url):
    return url if url.startswith(r"http") else f"https://{url}"


def apply_filter(tags: AdvancedHTMLParser, filter_data):
    included_tags = []
    excluded_tags = []

    if "include" in filter_data:
        for include_filter in filter_data["include"]:
            include_filter.get("name")
            attributes = include_filter.get("attributes", [])
            if len(attributes) == 0:
                included_tags.extend(tags.getElementsByTagName(include_filter.get("name")))
                continue
            for attr in attributes:
                attr_name = attr.get("name")
                # Flatten attribute values into a single string
                attr_values = list(attr.get("values", []))
                attr_values = ", ".join(attr_values)
                print(attr_values)
                included_tags.extend(tags.getElementsByAttr(attr_name, attr_values))

    if "exclude" in filter_data:
        for exclude_filter in filter_data["exclude"]:
            exclude_filter.get("name")
            attributes = exclude_filter.get("attributes", [])
            if len(attributes) == 0:
                excluded_tags.extend(tags.getElementsByTagName(exclude_filter.get("name")))
                continue
            for attr in attributes:
                attr_name = attr.get("name")
                # Flatten attribute values into a single string
                attr_values = list(attr.get("values", []))
                attr_values = ", ".join(attr_values)
                print(attr_values)
                excluded_tags.extend(tags.getElementsByAttr(attr_name, attr_values))

    return [tag for tag in included_tags if tag not in excluded_tags]


def crawl_website(url, tags_to_save={}, do_save=False, up_level=False):
    """
    Crawls a website and saves or displays the content.

    Args:
        url (str): The URL of the website to crawl.
        tags_to_save (list): A list of HTML tags to save.
        do_save (bool): Whether to save the content to a folder.
    """
    item_prog = NOTIFICATION2.progress(text="Crawling", value=0.0)
    url = add_https(url)
    local_domain = urlparse(url).netloc
    local_path = urlparse(url).path
    parts = len(local_path.split("/")[1:])
    home_url = str(os.path.split(url)[0])
    if parts >= 2 and up_level:
        home_url = os.path.split(home_url)[0]
    queue = deque([url])
    seen = []
    converted = []

    if not os.path.exists("processed"):
        os.mkdir("processed")

    progress = NOTIFICATION.progress(text="Crawling", value=1.0)

    data = {"resp_code": None, "downloaded": None, "remaining": None, "saving": ""}

    stattable = LEFT_TABLE.empty()

    statsvals = Items()

    statsvals.add_item(StatusWordItem("resp_code"))
    statsvals.add_item(StatusWordItem("finished"))
    statsvals.add_item(StatusWordItem("pending"))
    statsvals.add_item(StatusWordItem("saving"))

    split_column = int(st.session_state.get("colsplit", 1))
    result_columns = st.columns(split_column)
    i = 0

    while queue:
        url = queue.pop()
        if url in converted:
            continue
        current_column = i
        item_prog.progress(0.1, text="Checking if already processed")
        local_path = os.path.join(local_domain, urlparse(url).path)
        parent_path, path_tail = (
            os.path.split(local_path) if "/" in local_path else (None, local_path)
        )
        base_filename = f"{f'{convert_to_safe_url(parent_path)}/' if parent_path else '/'}{convert_to_safe_url(path_tail)}"

        item_prog.progress(0.1, text=f"Getting new hyperlinks in {parent_path}")

        if do_save:
            os.makedirs(f"markdown/{local_domain}/{parent_path}", exist_ok=True)

        HTML_CONTENT = ""

        st.write(f"markdown/{local_domain}/{parent_path}")

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

        item_prog.progress(0.25, text="Rendering Page")

        def fetch_content(url, data):
            content = load_page(url)
            data["resp_code"] = requests.get(url).status_code
            data["downloaded"] = i
            data["remaining"] = 1 + len(queue)
            data["saving"] = local_path
            return content, data

        item_prog.progress(0.5, text="Parsing")
        PARSER = AdvancedHTMLParser()
        try:
            # Create an instance of the AdvancedHTMLParser and parse the HTML content
            HTML_CONTENT, data = fetch_content(url, data)
            PARSER.parseStr(HTML_CONTENT)
            update_status(data)
        except Exception as e:
            data["saving"] = f"{url} - {e}"
            update_status(data)
            continue

        item_prog.progress(0.65, text="Filering Page")

        # Apply the filter using the defined function

        # Apply the filter using the defined function
        FILTERED_TAGS: list[AdvancedTag] = apply_filter(PARSER, tags_to_save)

        def russian_dolly(html_content, kept_tags):
            """
            Extracts specific tags and their siblings from the HTML content based on the provided criteria.

            Args:
                html_content (str): The HTML content of the page.
                kept_tags (list[AdvancedTag]): A list of tags that should be captured and their siblings.

            Returns:
                list[AdvancedTag]: The extracted tags and their siblings.
            """
            parser = AdvancedHTMLParser()
            parser.parseStr(html_content)
            extracted_tags = []

            for tag in kept_tags:
                extracted_tags.extend(get_tag_and_siblings(tag))

            return extracted_tags

        def get_tag_and_siblings(tag):
            """
            Recursively extracts a tag and its siblings.

            Args:
                tag (AdvancedTag): The tag to extract.

            Returns:
                list[AdvancedTag]: The extracted tag and its siblings.
            """
            extracted_tags = []

            if tag.parent and tag.name in {"code", "pre", "table", "ul", "ol"}:
                extracted_tags.extend(get_tag_and_siblings(tag.parent))
            else:
                extracted_tags = tag.getChildren()

            return extracted_tags

        # Example usage`
        cleaned_tags = []

        cleaned_tags = russian_dolly(HTML_CONTENT, FILTERED_TAGS)

        item_prog.progress(0.8, text="Writing Markdown")
        md_output = None
        md_display = ""
        md_add = ""
        expnd = (
            st.empty()
            if do_save
            else result_columns[current_column % split_column].expander(
                f":green[{base_filename}]", expanded=True
        ))
        item_prog.progress(0.85, text="Converting Page")

        for tag in cleaned_tags:
            if tag.children:
                children: list[AdvancedTag] = tag.getAllChildNodes()
                if any(child in cleaned_tags for child in children):
                    continue

            md_display = convert_to_markdown(tag)

            if do_save:
                md_add += "\n" + md_display + "\n"
            else:
                expnd.write(tag.tagName)
                expnd.write(md_display)

        if do_save:
            item_prog.progress(0.95, text="Saving Page")

            md_output = mdformat.text(md_add)

            with open(f"markdown/{local_domain}/{base_filename}.md", "w", encoding="UTF-8") as file:
                file.write(md_output)
        i += 1
        item_prog.progress(1.0, text=f"Page {i} Done {url}")

        for link in get_domain_hyperlinks(local_domain, url):
            if link in converted:
                continue
            if (link in seen) or home_url not in link:
                continue
            seen.append(link)
            queue.append(link)

        converted.append(url)

    time.sleep(2)
    stattable.empty()
    progress.empty()


def main():
    """
    The main function that runs the web scraping application.
    """

    url = COLUMNS[0].text_input(
        "URL",
        placeholder="https://www.example.com",
        value="https://example.com",
        label_visibility="collapsed",
    )

    COLUMNS[0].write(
        """
    :red[ Saving is disabled on demo for obvious space saving reasons ]
        """
    )
    COLUMNS[0].expander("Expand Instructions Here").markdown(
        """
    `https://python.langchain.com/docs/expression_language/interface`

    # Add specific attributes for tags..
    1. Enter a URL ( the... `http://` is optional )
    2. Select HTML tag to add Attribute
    3. Select an attribute
    4. Enter a Value to search for that Attr.
    5. Click to Add to the content.

    ### 'Crawl It' ... will:
    - Crawl the website and display,
    - Fill a markdown folder.

        """
    )

    if url.endswith("/"):
        url = url[:-1]

    parsed_folders = os.path.split(urlparse(url).path)[0]

    up_level = COLUMNS[0].checkbox("Allow parent path?")
    # Choices for HTML tags
    if up_level:
        parsed_folders = os.path.split(urlparse(parsed_folders).path)[0]

    COLUMNS[0].markdown(f"####  :blue[.../markdown/{urlparse(url).netloc}{parsed_folders}]")

    COLUMNS[0].checkbox(
        f"Dowwnload to drive?",
        help="Obv disabled  for cloud server, but handy at home..",
        key="DoSave",
    )

    STATE.HTML_TAGS_LIST = [
        "article",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "a",
        "p",
        "ul",
        "ol",
        "li",
        "img",
        "table",
        "pre",
        "script",
        "code",
        "div",
        "nav",
        "section",
        "style",
        "footer",
        "head",
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

    STATE.include_tags = STATE.get("include_tags", {})
    STATE.exclude_tags = STATE.get("exclude_tags", {})
    STATE.setting_tags = STATE.get("setting_tags", [])

    st.session_state["filter_dict"] = st.session_state.get(
        "filter_dict", {"include": [], "exclude": []}
    )

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

    inclusivity = COLUMNS[2].container()
    attribute_inclusivity = COLUMNS[2].container()

    upper_tag = inclusivity.columns([1, 0.01, 1])
    lowerr_tag = attribute_inclusivity.columns([1, 0.01, 1])

    upper_tag[0].write("### :green[🗟⇪] :blue[Include]")
    upper_tag[0].multiselect(
        "",
        STATE.HTML_TAGS_LIST,
        ["h1", "h2", "h3", "pre", "p", "pre", "code", "div", "article"],
        key="incl_tag_set",
        label_visibility="collapsed",
        on_change=update_includes,
    )
    upper_tag[2].write("### :red[🗑⇣] :orange[Blocked]")
    upper_tag[2].multiselect(
        "",
        STATE.HTML_TAGS_LIST,
        ["code", "div", "article"],
        key="excl_tag_set",
        label_visibility="collapsed",
        on_change=update_includes,
    )

    upper_tag[0].radio(
        ":green[HTML] Tag to Edit ",
        STATE.include_tags.keys(),
        horizontal=True,
        key="inc_select_tag",
    )
    lowerr_tag[0].radio(
        ":blue[Attribute] Tag to Edit",
        STATE.annotations.keys(),
        horizontal=True,
        key="inc_select_attr",
    )
    lowerr_tag[0].write(STATE.annotations.get(STATE.get("inc_select_attr", ""), ""))

    upper_tag[2].radio(
        ":red[HTML] Tag to Edit", STATE.exclude_tags.keys(), horizontal=True, key="exc_select_tag"
    )
    lowerr_tag[2].radio(
        ":orange[Attr] Tag to Edit",
        STATE.annotations.keys(),
        horizontal=True,
        key="exc_select_attr",
    )
    lowerr_tag[2].write(STATE.annotations.get(STATE.get("exc_select_attr", ""), ""))

    main_lower = COLUMNS[0].container()
    mainlow_coluumns = main_lower.columns([6, 1, 6])

    st.session_state["ran"] = st.session_state.get("ran", None)

    if not st.session_state["ran"]:
        update_includes()
        st.session_state["ran"] = True

    def edit_tag(loc, tag, attr, side):
        val: str = loc.text_input(
            "",
            placeholder=f"{tag} {attr} = thisvalue ",
            label_visibility="collapsed",
            key=f"{side}_strinp3",
        )
        col = ":green" if side == "include" else ":red"

        astrt = " " + attr + '"=' + val if attr else " "
        button_string = f"{col}[{side}] <{tag} {astrt}>"

        # Add new attribute button
        if loc.button(button_string, key=f"{side}_add_attribute_button"):
            if tag in STATE.get(f"{side}_tags"):
                STATE[f"{side}_tags"][tag]["attributes"].append({"name": attr, "values": [val]})

        # clear attribute button
        if loc.button(":red[Clear]", key=f"{side}_clear_attribute_button"):
            if tag in STATE.get(f"{side}_tags"):
                STATE[f"{side}_tags"][tag]["attributes"].clear()

        for tag in STATE.get(f"{side}_tags", {}).values():
            attributes: list = tag.get("attributes", [])
            loc.write(
                f"""{ tag.get("name") } :navy {(" :gray[ any ]") if len(attributes) == 0 else ""} """
            )
            if len(attributes) > 0:
                for attr in attributes:
                    atrtname = attr.get("name")
                    atrtvals = ", ".join(attr.get("values"))
                    loc.write(f" - {atrtname}: {atrtvals}")
        update_includes()

    edit_tag(
        lowerr_tag[0],
        STATE.get("inc_select_tag", ""),
        STATE.get("inc_select_attr", ""),
        "include",
    )
    edit_tag(
        lowerr_tag[2],
        STATE.get("exc_select_tag", ""),
        STATE.get("exc_select_attr", ""),
        "exclude",
    )

    with mainlow_coluumns[0]:
        st.json({
            tag["name"]: {attr["name"]: attr["values"] for attr in tag["attributes"]}
            for tag in st.session_state["filter_dict"]["include"]
        })
    with mainlow_coluumns[2]:
        st.json({
            tag["name"]: {attr["name"]: attr["values"] for attr in tag["attributes"]}
            for tag in st.session_state["filter_dict"]["exclude"]
        })

    # Display the dataframe
    inclusivity.slider("Not yet implemented...", 1, 5, 2, 1, key="colsplit")

    do_save = st.session_state.get("DoSave", False)

    st.code(st.session_state["filter_dict"])

    if inclusivity.button("Crawl It", use_container_width=True, type="secondary"):

        crawl_website(url, st.session_state["filter_dict"], do_save, up_level)
        NOTIFICATION.info("Crawling complete!")
        time.sleep(2)
        NOTIFICATION.empty()

if __name__ == "__main__":
    main()
