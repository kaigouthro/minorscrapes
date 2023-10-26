
import os
import re
import time
import urllib.request
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

import mdformat
import requests
import streamlit as st
from bs4 import BeautifulSoup
from markdownify import MarkdownConverter
from statwords import StatusWords

def convert_to_markdown(input_text, **options):
    """
    Converts the input text to Markdown format.

    Args:
        input_text (str): The input text to be converted.
        **options (kwargs): Additional options for the Markdown conversion.

    Returns:
        str: The converted Markdown text.
    """
    if lang := re.search(r"language-(\w+)", input_text):
        options["code_language"] = lang[1]
    return MarkdownConverter(**options).convert(input_text)


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
        with urllib.request.urlopen(url) as response:
            if not response.info().get("Content-Type").startswith("text/html"):
                return []
            parser = HyperlinkParser()
            while True:
                if chunk := response.read(1024):
                    parser.feed(chunk.decode("utf-8"))
                else:
                    break
    except Exception as e:
        st.warning(e)
        return []
    return parser.hyperlinks


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
    for link in set(get_hyperlinks(url)):
        clean_link = None
        if re.search(r"^http[s]*://" + local_domain.replace(".", r"\.") + r"/.+", link):
            url_obj = urlparse(link)
            if url_obj.netloc == local_domain:
                clean_link = link
        else:
            clean_link = urljoin(url, link)
        if clean_link is not None:
            if clean_link.endswith("/"):
                clean_link = clean_link[:-1]
            clean_links.append(clean_link)
    return [
        link
        for link in clean_links
        if link and link.startswith(f"https://{local_domain}")
    ]


def convert_to_safe_url(text):
    """
    Converts a text into a safe URL format.

    Args:
        text (str): The text to be converted.

    Returns:
        str: The converted safe URL.
    """
    subst = "_"
    regex = r"[^a-zA-Z0-9-_\/]|\:"
    return re.sub(regex, subst, text, 0, re.DOTALL)


def crawl_website(url, tags_to_save=[], do_save=False):
    """
    Crawls a website and saves or displays the content.

    Args:
        url (str): The URL of the website to crawl.
        tags_to_save (list): A list of HTML tags to save.
        do_save (bool): Whether to save the content to a folder.
    """
    local_domain = urlparse(url).netloc
    local_path = urlparse(url).path
    queue = deque([url])
    seen = []
    converted = []

    if not os.path.exists("processed"):
        os.mkdir("processed")

    columns = st.columns([0.6, 0.4])
    progress = columns[0].progress(text="Crawling", value=1.0)
    data = {"resp_code": None, "downloaded": None, "remaining": None, "saving": ""}
    stattable = columns[1].empty()
    i = 0

    while queue:
        url = queue.pop()
        has_hash = re.search(r"(?<=#)\w+", url)
        if url in converted:
            continue
        if has_hash:
            continue
        local_path = urlparse(url).path
        parent_path, last_folder = os.path.split(local_path)
        os.makedirs(f"markdown/{local_domain}/{convert_to_safe_url(parent_path)}", exist_ok=True)
        content = None
        converted.append(url)
        statview1 = StatusWords()
        statview2 = StatusWords()
        statview3 = StatusWords()

        def update_status(data):
            value0 = data["resp_code"]
            value1 = data["downloaded"]
            value2 = data["remaining"]
            value3 = data["saving"]

            if value0 != 200:
                statview1.response_code(value0)
            else:
                statview1.set("finished", value1)
                statview2.set("pending", value2)
                statview3.set("saving", value3)

            stattable.dataframe([statview1.display, statview2.display])
            progress.progress(
                max(i / (1 + i + len(queue)), max(0, i - len(queue)) / (1 + i + len(queue))),
                text=f":orange[{statview3.display['value']}]",
            )

        def fetch_content(url, data):
            content = requests.get(url, timeout=5)
            data["resp_code"] = content.status_code
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

        base_filename = f"{convert_to_safe_url(parent_path)}/{convert_to_safe_url(last_folder)}"
        tag_items = BeautifulSoup(content.text, "html5lib").find_all(tags_to_save)

        md_output = None
        md_display = ""
        md_add = ""

        for tag in tag_items:
            tag = str(tag)
            if re.search(r"\<\s*\w+\s+class\s*\=\s*(?=\"[^\"]*?(footer|menu|breadcrumbs|header)[^\"]*\")", tag):
                continue
            md_display = mdformat.text(convert_to_markdown(tag))
            if do_save:
                md_add += "\n" + md_display + "\n"
            else:
                st.markdown(md_display)

        if do_save:
            md_output = mdformat.text(md_add)
            with open(f"markdown/{local_domain}/{base_filename}.md", "w", encoding="UTF-8") as file:
                file.write(md_output)

        i += 1
        for link in get_domain_hyperlinks(local_domain, url):
            if link not in seen and (parent_path in link):
                queue.append(link)
                seen.append(link)
    time.sleep(2)
    stattable.empty()
    progress.empty()


def main():
    """
    The main function that runs the web scraping application.
    """
    st.title("Minor Scrapes")
    st.write("Enter a URL and click 'Submit' to crawl the website and fill the markdown folder.")
    columns = st.columns([0.8, 0.2])
    url = columns[0].text_input(
        "URL", placeholder="https://www.example.com", label_visibility="collapsed"
    )
    notification = st.empty()
    if url.endswith("/"):
        url = url[:-1]
    do_save = st.checkbox(
        f"Do not Display. Save instead to folder? :n  :blue['./markdown/{urlparse(url).netloc}{os.path.split(urlparse(url).path)[0]}']"
    )
    tags_to_save = st.multiselect(
        "Tags to scrape",
        ["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "img", "table", "pre", "code"],
        ["h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "img", "table", "pre"],
    )
    if columns[1].button("Submit"):
        crawl_website(url, tags_to_save, do_save)
        notification.info("Crawling complete!")
        time.sleep(2)
        notification.empty()


if __name__ == "__main__":
    main()
