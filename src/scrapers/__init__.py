"""
Scrapers Package

This package contains following modules:
 notice:
 events:
 login:
 navigation:
 news:

__vars__:
TRINITY_LINK -> [str] URL of Trinity college, Dilibazar, Kathmandu
"""

CACHE_DIR = "/home/h/website_scraper/src/scrapers/cache/"
TRINITY_LINK = "http://trinitycollege.edu.np/"


def fetch_html(url):
    """
    Fetch html from web.
    Returns -> <requests HTML> object.
    Params -> URL of the web resource.
    """
    session = HTMLSession()
    result = session.get(url)
    return result.html
