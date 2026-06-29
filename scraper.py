import requests
from bs4 import BeautifulSoup


def download_page(url):
    response = requests.get(url)
    return response.text


def get_title(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.text


def get_links(html):
    soup = BeautifulSoup(html, "html.parser")

    links = []

    for link in soup.find_all("a"):
        href = link.get("href")
        text = link.text.strip()

        if href:
            links.append({
                "text": text,
                "url": href
            })

    return links