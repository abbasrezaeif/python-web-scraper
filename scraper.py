import requests
from bs4 import BeautifulSoup


def download_page(url):
    response = requests.get(url)
    return response.text


def get_title(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.text