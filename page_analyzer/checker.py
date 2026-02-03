"""URL Checker module."""
import requests
from bs4 import BeautifulSoup


"""Get SEO info from URL."""


def get_check_info(url):
    headers = {
    'User-Agent': (
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    ),
    'Accept': (
        'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/avif,image/webp,image/apng,*/*;q=0.8,'
        'application/signed-exchange;v=b3;q=0.7'
    ),
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
}
    try:
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()

        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.text, "html.parser")
        h1_tag = soup.find("h1")
        h1 = h1_tag.get_text().strip() if h1_tag else ""

        title_tag = soup.find("title")
        title = title_tag.get_text().strip() if title_tag else ""

        meta_description = soup.find("meta", attrs={"name": "description"})
        description = meta_description.get("content").strip()
        if meta_description else ""

        status_code = response.status_code

        return {"status_code": status_code,
                "h1": h1,
                "title": title,
                "description": description}
    except requests.RequestException as e:
        print(f"Ошибка при проверке URL {url}: {e}")
        return None
