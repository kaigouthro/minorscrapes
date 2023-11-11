import os
import re
import asyncio
import time
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import mdformat
import requests
import streamlit as st
from markdownify import MarkdownConverter
from statwords import StatusWordItem, Items

st.set_page_config("Minor Scrapes", "🔪", "wide")
STATE = st.session_state

st.title("Minor Scrapes")

NOTIFICATION = st.empty()
COLUMNS = st.columns([0.618, 0.01, 0.372])
LEFT_TABLE = COLUMNS[0].empty()

def get_matching_tags(soup, tags_plus_atrtibutes):
    """
    Get all tags that match the given parameters, but ignore tags if the parent exists
    if an attribute exists, only get tags witth that attribute, otherwise get all of tho9se tags


    Args:
        soup (beautifulsoup object): BeautifulSoup Object
        tags_attr (list): list of dictionary objects describing the tags and their attributes
            [{ "tag": "h1", "attrs": [{"class": "some_class"}]}, {"tag": "p", "attrs": None}]
    Yields:
        BeautifulSoup.Tag: tags that match the given parameters
    """
    for tag_attr in tags_plus_atrtibutes:
        tag = tag_attr["tag"]
        # get all tags that match the tag
        tags = soup.find_all(tag)
        if tag_attr["attrs"] is not None:
            attrs = tag_attr["attrs"]
            for attr in attrs:
                # get all tags with those attributes
                tags = [t for t in tags if t.has_attr(attr) or t.has_attr(attr + "s")]
        for t in tags:
            if not t.find_parents(tag):
                yield t

class RenderedPage:
    def __init__(self):
        self.driver = self.get_driver()
    
    @st.cache_resource
    def get_driver(self):
        # Set up the headless browser
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # Run the browser in headless mode
        chrome_options.add_argument('--disable-gpu')    
        return webdriver.Chrome(sevice=Service(ChromeDriverManager().install()), options=chrome_options)

    async def get_rendered_page(self, url):
        # Load the webpage in the headless browser
        self.driver.get(url)

        # Wait for JavaScript to execute and render the page
        # You can use explicit waits to wait for specific elements to appear on the page
        await asyncio.sleep(5)
        
        # Get the fully rendered HTML
        full_html = self.driver.page_source
        
        # Close the browser
        self.driver.quit()
        
        # Create a Beautiful Soup object of the fully rendered page
        soup = BeautifulSoup(full_html, "html.parser")
        return soup


def convert_to_markdown(soup):
    """
    Converts the input text to Markdown format.

    Args:
        input_text (soup): The input text to be converted.
        **options (kwargs): Additional options for the Markdown conversion.

    Returns:
        str: The converted Markdown text.
    """

    converter = MarkdownConverter(
        code_language="python",
        default_title=False,
        escape_asterisks=False,
        escape_underscores=False,
    )
    return converter.convert_soup(soup)


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
    return re.sub(regex, subst, text, count=0, flags=re.DOTALL)


def add_https(url):
    return url if url.startswith(r"http") else f"https://{url}"


def crawl_website(url, tags_to_save=None, do_save=False, up_level=False):
    """
    Crawls a website and saves or displays the content.

    Args:
        url (str): The URL of the website to crawl.
        tags_to_save (list): A list of HTML tags to save.
        do_save (bool): Whether to save the content to a folder.
    """
    if tags_to_save is None:
        tags_to_save = []
        
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
    i = 0
    local_path = ''

    if not os.path.exists("processed"):
            src = (
                await RenderedPage()
                .get_rendered_page(url)
                .renderContents(encoding="UTF-8", prettyPrint=True)
            )
    progress = NOTIFICATION.progress(text="Crawling", value=1.0)
    data = {"resp_code": None, "downloaded": None, "remaining": None, "saving": ""}
    stattable = LEFT_TABLE.empty()

    class HyperlinkParser(HTMLParser):
        """
        A class that parses HTML and extracts hyperlinks.
        """

        def __init__(self):
            super().__init__()
            self.hyperlinks = []

        def handle_starttag(self, tag, attrs):
            """
            Handles the start tag of an HTML element and extracts hyperlinks.

            Args:
                tag (str): The name of the HTML tag.
                attrs (list): A list of attribute-value pairs for the HTML tag.
            """
            if tag == "a":
                for attr in attrs:
                    if attr[0] == "href":
                        self.hyperlinks.append(attr[1])

    def get_hyperlinks(url):

        """
        Retrieves all hyperlinks from a given URL.

        Args:
            url (str): The URL to retrieve hyperlinks from.

        Returns:
            list: A list of hyperlinks found in the URL.
        """
        try:
            src = await RenderedPage().get_rendered_page(url).prettify()
            parser = HyperlinkParser()
            parser.feed(src)
            return parser.hyperlinks
        except Exception:
            return []

    def get_domain_hyperlinks(local_domain, url):
        """
        Retrieves domain-specific hyperlinks from a given URL.

        Args:
            local_domain (str): The local domain to filter hyperlinks.
            url (str): The URL to retrieve hyperlinks from.

        Returns:
            list: A list of domain-specific hyperlinks found in the URL.
        """
        clean_links = []
        hl = get_hyperlinks(url)
        for link in hl:
            clean_link = None
            if re.search(rf"http.*?{local_domain}/.+", link):
                url_obj = urlparse(link)
                if url_obj.netloc == local_domain:
                    clean_link = link
            else:
                clean_link = urljoin(url, link)
            if clean_link is not None:
                if clean_link.endswith("/"):
                    clean_link = clean_link[:-1]
                clean_links.append(clean_link)
        return clean_links

    statsvals = Items()

    statsvals.add_item(StatusWordItem("resp_code"))
    statsvals.add_item(StatusWordItem("finished"))
    statsvals.add_item(StatusWordItem("pending"))
    statsvals.add_item(StatusWordItem("saving"))

    while queue:
        stattable.table([s.display for s in statsvals.items])
        url = queue.pop()
        if url in converted:
            continue
        local_path = os.path.join(local_domain, urlparse(url).path)
        parent_path, path_tail = (
            os.path.split(local_path) if "/" in local_path else (None, local_path)
        )

        if do_save:
            os.makedirs(f"markdown/{local_domain}/{parent_path}", exist_ok=True)
        content = None

        def update_status(data, i, local_path):
            value0 = data["resp_code"]
            value1 = data["downloaded"]
            value2 = data["remaining"]
            value3 = data["saving"]

            if value0 != 200:
                statsvals.items[0].response_code(value0)
            else:
                statsvals.items[1].set("finished", value1)
                statsvals.items[2].set("pending", value2)
                statsvals.items[3].set("saving", value3)

            progress.progress(
                max(
                    i / (1 + i + len(queue)),
                    max(0, i - len(queue)) / (1 + i + len(queue)),
                ),
                text=f":orange[{local_path}]",
            )

        def fetch_content(url, data):
            src = (
                await RenderedPage()
                .get_rendered_page(url)
                .renderContents(encoding="UTF-8", prettyPrint=True)
            )
            content = src
            # content = body.get_dom_attribute("outerHTML")
            data["resp_code"] = requests.get(url, timeout=5).status_code
            data["downloaded"] = i
            data["remaining"] = 1 + len(queue)
            data["saving"] = local_path
            return content

        try:
            content = fetch_content(url, data)
            update_status(data)

        except Exception as e:
            data["saving"] = f"{url} - {e}"
            update_status(data)
            continue

        base_filename = f"{f'{convert_to_safe_url(parent_path)}/' if parent_path else '/'}{convert_to_safe_url(path_tail)}"
        soup = BeautifulSoup(content, "html5lib")
        tag_items = list(get_matching_tags(soup, tags_to_save))
        # remove duplicates starting from the last item towards the first..

        md_output = None
        md_display = ""
        md_add = ""
        expnd = st.expander(f":green[{base_filename}]") if not do_save else st.empty()
        for tag in tag_items:
            # tag = tag.text
            if re.search(
                r"\<\s*\w+\s+class\s*\=\s*(?=\"[^\"]*?(footer|menu|breadcrumbs|header)[^\"]*\")",
                tag.text,
            ):
                continue
            md_display = mdformat.text(convert_to_markdown(tag))
            if do_save:
                md_add += "\n" + md_display + "\n"
            else:
                expnd.markdown(md_display)

        if do_save:
            md_output = mdformat.text(md_add)
            with open(
                f"markdown/{local_domain}/{base_filename}.md", "w", encoding="UTF-8"
            ) as file:
                file.write(md_output)
        i += 1

        for link in get_domain_hyperlinks(local_domain, url):
            if (
                re.search(r"(?<=#)[A-Za-z0-9]+", link)
                or (link in seen)
                or home_url not in link
            ):
                continue
            queue.append(link)
            seen.append(link)

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

    COLUMNS[0].markdown(
        f"####  :blue[.../markdown/{urlparse(url).netloc}{parsed_folders}]"
    )
    do_save = COLUMNS[0].checkbox(
        f"Hide Display and download to drive?",
        disabled=True,
        help="Obv disabled  for cloud server, but handy at home..",
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

    COLUMNS[2].multiselect(
        "",
        STATE.HTML_TAGS_LIST,
        ["h1", "h2", "h3", "a", "p", "pre"],
        key="htmltags",
        label_visibility="collapsed",
    )

    STATE.tags = STATE.get("tags", {})

    # Create initial tag instance
    for tag in STATE.HTML_TAGS_LIST:
        if tag in STATE.htmltags:
            if tag not in STATE.tags.keys():
                STATE.tags[tag] = []
        else:
            if tag in STATE.tags.keys():
                del STATE.tags[tag]
    COLUMNS[2].columns([0.2, 0.8])

    COLUMNS[2].write("### Tag enable above")
    html_tag = COLUMNS[2].radio(
        ":blue[HTML] ", STATE.htmltags, horizontal=True, key="strinp1"
    )

    attr_name = (
        COLUMNS[2].radio(
            ":red[Attr]", list(STATE.annotations.keys()), key="strinp2", horizontal=True
        )
        or ""
    )
    COLUMNS[2].write(STATE.annotations[attr_name])
    val: str = COLUMNS[2].text_input("", label_visibility="collapsed", key="strinp3")

    # Add new tag instance
    if COLUMNS[2].button(
        f"""Add :blue[{html_tag}] :red[{attr_name}]=":green[{val}]" """,
        use_container_width=True,
    ):
        st.session_state.tags[html_tag].append({attr_name: val})
    if COLUMNS[2].button("Clear", type="secondary", use_container_width=True):
        st.session_state.tags[html_tag] = []

    # make dataframe data..
    df_data = {
        "Tag": list(st.session_state.tags.keys()),
        "Attr": [(v or None) for v in st.session_state.tags.values()],
    }

    # Display the dataframe
    COLUMNS[0].dataframe(df_data, use_container_width=True, height=400)

    COLUMNS[2].slider("Not yet implemented...", 1, 5, 2, 1, key="colsplit")

    tag_requests = [{"tag": t, "attrs": None} for t in st.session_state.tags.keys()]

    # Iterate over tags and properties
    for tag, properties in st.session_state.tags.items():

        for property_dict in properties:
            # Create dictionary for each tag and properties
            data = {"tag": tag, "attrs": property_dict}
            tag_requests.append(data)  # Append the dictionary to the list

    if COLUMNS[2].button("Crawl It", use_container_width=True, type="primary"):
        crawl_website(url, tag_requests, do_save, up_level)
        NOTIFICATION.info("Crawling complete!")
        time.sleep(5)
        NOTIFICATION.empty()


if __name__ == "__main__":
    main()
