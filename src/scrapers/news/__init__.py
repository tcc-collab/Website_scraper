"""
News package:
get_html -> [requests HTML object] HTML
get_top_news -> [List] list of recent news[type dict]
news_page_link -> [str] link of news page containing all notices
get_all_news -> [List] list of all news[type dict]
"""

from pathlib import Path

from requests_html import HTML

from src.scrapers import CACHE_DIR, TRINITY_LINK, fetch_html
from src.scrapers.news.main import get_all_news, get_top_news, news_page_link


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
    news_url = "http://trinitycollege.edu.np?page=news&type=news"
    link_resource_map = {TRINITY_LINK: "index.html", news_url: "news/all_news.html"}

    index_file = Path(CACHE_DIR) / link_resource_map[url]
    try:
        with open(index_file, "r", encoding="utf-8") as rf:
            html_str = rf.read()
        html_soup = HTML(html=html_str, url=url)
        return html_soup
    except Exception as E:
        print(E)
        return None
