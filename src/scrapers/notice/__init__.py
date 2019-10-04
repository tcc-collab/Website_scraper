"""
Notice package:
get_html -> [requests HTML object] HTML
get_top_notices -> [List] list of recent 3 notices[type dict]
notice_page_link -> [str] link of notice page containing all notices
get_all_notices -> [List] list of all notices[type dict]
"""

from pathlib import Path

from requests_html import HTML

from src.scrapers import CACHE_DIR, TRINITY_LINK, fetch_html
from src.scrapers.notice.main import (get_all_notice, get_top_notice,
                                      notice_page_link)


def get_html(url=TRINITY_LINK):
    """
    Returns a valid <requests HTML> object.
    Params:
        url: [str] URL of page. Default trinity homepage
    """
    html = __get_html_from_cache(url)
    if not html:
        html = fetch_html(url)
    return html


def __get_html_from_cache(url):
    """
    Loads <requests HTML> object from cache files
    Params:
        url = [str] URL of page to load
    """
    notice_url = "http://trinitycollege.edu.np?page=notice&type=notice"
    link_resource_map = {
        TRINITY_LINK: "index.html",
        notice_url: "notice/all_notice.html",
    }

    index_file = Path(CACHE_DIR) / link_resource_map[url]
    try:
        with open(index_file, "r", encoding="utf-8") as rf:
            html_str = rf.read()
        html_soup = HTML(html=html_str, url=url)
        return html_soup
    except Exception as E:
        print(E)
        return None
