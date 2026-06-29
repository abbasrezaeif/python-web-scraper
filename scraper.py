import requests


def download_page(url):
    response = requests.get(url)

    return response.text