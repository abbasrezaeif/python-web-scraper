from scraper import download_page, get_title, get_links


def main():
    url = "https://example.com"

    html = download_page(url)

    title = get_title(html)
    links = get_links(html)

    print("Page Title:")
    print(title)

    print("\nLinks:")
    for link in links:
        print(f"- {link['text']}: {link['url']}")


if __name__ == "__main__":
    main()