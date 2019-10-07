import json

from flask import Flask, request

from webapi.scrapers import get_html
from webapi.scrapers.downloadable import get_downloadable
from webapi.scrapers.events import event_page_link, get_top_event
from webapi.scrapers.footer import get_footer
from webapi.scrapers.navigation import get_main_nav_menu, get_side_nav_menu
from webapi.scrapers.news import get_all_news, get_top_news, news_page_link
from webapi.scrapers.notice import (get_all_notice, get_top_notice,
                                    notice_page_link)

app = Flask(__name__)


@app.route("/notice")
def notice():
    type = request.args.get("type", "top", type=str)
    html_soup = get_html()
    if type == "all":
        notice_url = notice_page_link(html_soup)
        html_soup = get_html(notice_url)

    type_function_map = {
        "all": get_all_notice,
        "top": get_top_notice,
        "link": notice_page_link,
    }
    data = type_function_map[type](html_soup)
    return json.dumps(data)


@app.route("/event")
def event():
    type = request.args.get("type", "top", type=str)
    type_function_map = {"top": get_top_event, "link": event_page_link}
    html_soup = get_html()
    data = type_function_map[type](html_soup)
    return json.dumps(data)


@app.route("/news")
def news():
    type = request.args.get("type", "top", type=str)
    html_soup = get_html()
    if type == "all":
        news_url = news_page_link(html_soup)
        html_soup = get_html(news_url)

    type_function_map = {
        "all": get_all_news,
        "top": get_top_news,
        "link": news_page_link,
    }
    data = type_function_map[type](html_soup)
    return json.dumps(data)


@app.route("/navigation")
def navigation():
    type = request.args.get("type", "side", type=str)
    html_soup = get_html()
    type_function_map = {"side": get_side_nav_menu, "main": get_main_nav_menu}
    data = type_function_map[type](html_soup)
    return json.dumps(data)


@app.route("/downloadable")
def downloadable():
    html_soup = get_html()
    data = get_downloadable()
    return json.dumps(data)


@app.route("/footer")
def footer():
    html_soup = get_html()
    data = get_footer()
    return json.dumps(data)
