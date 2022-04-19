import requests
from bs4 import BeautifulSoup


def web_crawler(url_input, max_urls):
    urln = 1
    while urln <= max_urls:
        url = url_input
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.select('a'):
            href = link.get('href')
            print(href)
        urln += 1
