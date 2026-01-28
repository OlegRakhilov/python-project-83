import requests
from bs4 import BeautifulSoup


def get_check_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
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
        description = meta_description.get("content").strip() if meta_description else ""

        status_code = response.status_code

        return {"status_code": status_code, "h1": h1, "title": title, "description": description}
    except requests.RequestException as e:
        print(f"Ошибка при проверке URL {url}: {e}")
        return None
