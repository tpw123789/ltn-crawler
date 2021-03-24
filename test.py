from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'https://news.ltn.com.tw/news/life/breakingnews/3469688'


def get_content():
    response = urlopen(url)
    html = BeautifulSoup(response)
    s = ''
    result = html.find('div', class_='text boxTitle boxText')
    target = result.find_all('p')
    for r in target:
        if len(r.text) != 0:
            if r.text[-1] == '。':
                s += r.text
                print(r.text)
    return s


a = get_content()
print(a)


