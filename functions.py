import requests
from bs4 import BeautifulSoup



def writeToFile(url_input,url):
    filename = url+".txt"
    path = r'./output/{}'.format(filename)
    file = open(path, "a")
    file.write("\n")
    file.write(url_input)
    file.close()

def crawl(url_input, urlOriginal, max_urls):
    urln = 1
    while urln <= max_urls:
        url = url_input
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.select('a'):
            href = link.get('href')
            print(href)
            writeToFile(href, urlOriginal)
        urln += 1