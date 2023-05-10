import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_pages():
    request_session = requests.Session()
    start_url = "https://en.uitm.edu.eu/news/page/{0}/?wpv_view_count=505"

    html_bytes = None
    while html_bytes is None:
        try:
            html_bytes = request_session.get(start_url.format(1)).text
        except Exception as e:
            print(f"Try again {e}")
            return

    soup = BeautifulSoup(html_bytes, "lxml")

    elements = []

    for val in soup.find_all("a", {"class": "wpv-archive-pagination-link js-wpv-archive-pagination-link page-link"}):
        elements.append(val.getText())

    return int(elements[-1])


def get_news(pages: int):
    request_session = requests.Session()
    start_url = "https://en.uitm.edu.eu/news/page/{0}/?wpv_view_count=505"
    list_of_news = []

    for i in range(1, pages + 1):
        print("CYCLE {0}".format(i))
        print(start_url.format(i))

        try:
            html_bytes = request_session.get(start_url.format(i)).text
        except Exception as e:
            print(f"Try again {e}")
            return

        soup = BeautifulSoup(html_bytes, "lxml")

        for val in soup.find_all("div", {"class": "col-md-8 news-small-padding"}):
            try:
                list_of_news.append({
                    "date": val.find("span", {"class": "date-small-news"}).getText(),
                    "title": val.find("h2").getText(),
                    "text": val.find("div", {"class": "post-excerpt"}).find("p").getText(),
                })
            except Exception as e:
                print(f"Skipped because of {e}")
                pass

    return list_of_news


if __name__ == '__main__':
    print(get_pages())

    print(get_news(get_pages()))
