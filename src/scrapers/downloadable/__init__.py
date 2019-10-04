"""
Downloadable package:
"""

from requests_html import HTML

# from src.scrapers import TRINITY_LINK as url
# from src.scrapers import get_html
url = "http://trinitcollege.edu.np"


def get_downloadable(html_soup):
    # html_soup = get_html()

    left_div = html_soup.find("div#leftnoav", first=True)
    left_div_a_tag = left_div.find("p", first=True).find("a", first=True)
    left_title = left_div_a_tag.text
    link = left_div_a_tag.attrs.get("href")
    left_link = f"{url}/{link.strip()}"

    right_a_xpath = "/html/body/div/div[2]/div[2]/div[3]/a"
    right_a_tag = html_soup.xpath(right_a_xpath, first=True)
    print(right_a_tag.html)
    # right_title_img = right_div_a_tag.find("img", first=True).attrs.get("src")


#    right_title_img = None
#    link = right_div_a_tag.attrs.get("href")
#    right_link = f"{url}/{link.strip()}"

#    download_dict = {
#        "left_side": {"title": left_title, "link": left_link},
#        "right_side": {"img": right_title_img, "link": right_link},
#    }
#    print(download_dict)
#    return download_dict


if __name__ == "__main__":
    with open("../cache/index.html", "r", encoding="utf-8") as rf:
        data = rf.read()
        html = HTML(html=data, url=url)

    get_downloadable(html)

    top = """
    from requests_html import HTMLSession

    url = "http://trinitycollege.edu.np?page=event&type=event"
    session = HTMLSession()
    result = session.get(url)

    with open("../cache/events/all_events.html", "w") as rf:
        data = rf.write(result.html.html)
        # html = HTML(html=data, url=url)
    """
