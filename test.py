from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json


def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        # data = response.read().decode('utf-8')
        data = json.load(response)
    return data.get('data')



# base = 'https://news.ltn.com.tw/ajax/breakingnews/all/'
# page_url = base + '1'
# page_data = get_data(page_url)
# print(type(page_data))
# print(list(page_data[0].items()))

dic = {'hery0': 10, 'amy': 20}
for i in dic.keys():
    print(i)
    del dic[i]
    print(dic)

