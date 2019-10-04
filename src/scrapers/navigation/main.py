"""
Navigation: main.py module
"""

from requests_html import HTML

# from src.scrapers import fetch_html
# from src.scrapers import TRINITY_LINK as url
url = "http://trinitycollege.edu.np"


def get_side_nav_menu(html_soup):
    """
    Returns -> [list] list of side navigation menus[type dict]
      Menu -> [Dict] attrs:
        'name' -> [str] name of menu
        'link' -> [str] link for the menu
        'image' -> [str] URL for menu image

    Params -> [requests.HTML object] HTML of web page.
    """
    # Container ul with all navigation menus
    menu_div = html_soup.find("ul#suckertree1", first=True)

    # list of divs containing menu title and link
    menu_items = menu_div.find("li")
    side_menus = []

    for menu in menu_items:
        menu_a_tag = menu.find("a", first=True)
        name = menu_a_tag.text
        link = menu_a_tag.attrs.get("href")
        full_link = url + link
        image = menu.find("img", first=True).attrs.get("src")
        menu_dict = {"name": name, "link": full_link, "image": image}
        side_menus.append(menu_dict)

    return top_menu


def get_main_menu(html_soup):
    """
    Returns -> [list] list of all main menus[type dict]
      Menu -> [Dict] attrs:
        'name' -> [str] name of menu
        'link' -> [str] link for the menu
        'image' -> [str] URL for menu image

    Params -> [requests.HTML object] HTML of web page.
    """

    print(html_soup)


#    all_menu_div = menu_page_soup.find("div#content_text", first=True)
#    menu = all_menu_div.find("div#menu")
#
#    more_menu = []
#    for menu in menu:
#        date = menu.find("div.date", first=True).text
#        content = menu.find("div.content", first=True).text
#        title_div = menu.find("div.title1", first=True)
#        title = title_div.find("a", first=True).text
#        link_div = menu.find("div.more", first=True)
#        link = url + link_div.find("a", first=True).attrs.get("href")
#
#        menu_dict = {"date": date, "title": title, "content": content, "link": link}
#        more_menu.append(menu_dict)
#
#    return more_menu


if __name__ == "__main__":
    with open("../cache/index.html", "r") as rf:
        data = rf.read()
        html = HTML(html=data, url=url)

    get_side_nav_menu(html)
