from get_data import article_data
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

articles = article_data('no', 'title', 'url', 'tagText')


def article_content(url):
    response = urlopen(url)
    html = BeautifulSoup(response)
    s = ''
    if url.split('/')[2] == 'news.ltn.com.tw':
        result = html.find('div', class_='text boxTitle boxText')
        target = result.find_all('p')
        for r in target:
            if len(r.text) != 0:
                if r.text[-1] == '。':
                    s += r.text
        return s
    else:
        return ''



