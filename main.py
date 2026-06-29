from scraper import download_page
from scraper import get_title


def main():

    url = "https://example.com"

    html = download_page(url)

    title = get_title(html)

    print(title)


if __name__ == "__main__":
    main()