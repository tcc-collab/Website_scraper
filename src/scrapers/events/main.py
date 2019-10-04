"""
Events: main.py module
"""

from requests_html import HTML

from src.scrapers import TRINITY_LINK as url


def event_page_link(html_soup):
    """
    Returns -> [str] link of event page.
    Params -> [requests.HTML object] HTML of web page.
    """
    # Container div with event and news
    container_div = html_soup.find("div#backgroundBox", first=True)
    # First div is events div
    event_div = container_div.find("div", first=True)

    view_more_div = event_div.find("div.viewmr", first=True)
    view_more_a_tag = view_more_div.find("a", first=True)
    more_events_link = url + "/" + view_more_a_tag.attrs.get("href")
    print(more_events_link)
    return more_events_link


def get_top_event(html_soup):
    """
    Returns -> [list] list of latest event[type dict]
      Event -> [Dict] attrs:
        'title' -> [str] title of event
        'link' -> [str] full link for the event

    Params -> [requests.HTML object] HTML of web page.
    """
    # Container div with event and event
    container_div = html_soup.find("div#backgroundBox", first=True)
    # First div is events div
    event_div = container_div.find("div", first=True)

    # list of divs containing event title and link
    event_items = event_div.find("div.event")
    top_events = []

    for event in event_items:
        eng_month = event.find("div.engname", first=True).text
        eng_day = event.find("div.date", first=True).text
        eng_date = f"{eng_day} {eng_month}"
        nep_date = event.find("div.nepname", first=True).text
        title = event.find("div.eventtitle", first=True).text
        subtitle = event.find("p", first=True).text
        desc_div = event.find("div.description", first=True)
        if desc_div:
            desc_a_tag = desc_div.find("a", first=True)
            description = desc_a_tag.text
            link = desc_a_tag.attrs.get("href")
            full_link = url + link
        else:
            description, full_link = None, None

        event_dict = {
            "title": title,
            "subtitle": subtitle,
            "english_date": eng_date,
            "nepali_date": nep_date,
            "description": description,
            "link": full_link,
        }
        print(event_dict)
        top_events.append(event_dict)

    return top_events


if __name__ == "__main__":
    with open("../cache/events/all_events.html", "r", encoding="utf-8") as rf:
        data = rf.read()
        html = HTML(html=data, url=url)

    #    get_top_event(html)
    #    event_page_link(html)
    get_all_event(html)

    top = """
    from requests_html import HTMLSession

    url = "http://trinitycollege.edu.np?page=event&type=event"
    session = HTMLSession()
    result = session.get(url)

    with open("../cache/events/all_events.html", "w") as rf:
        data = rf.write(result.html.html)
        # html = HTML(html=data, url=url)
    """
