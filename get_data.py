from urllib.request import urlopen, Request
import json


def get_data(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        data = json.load(response)
    return data


def get_article_data():
    """取得20 * 25篇報導 dict所有keys"""
    base = 'https://news.ltn.com.tw/ajax/breakingnews/all/'
    page = 1
    article_list = []
    while True:
        page_url = base + str(page)
        page_data = get_data(page_url).get('data')  # {code: '200', data: ...}
        if len(page_data) == 0:  # 最後一頁停止
            break
        if page > 1:  # page2 -> data: {no:{...}, ...}
            article_list.extend(list(page_data.values()))
        else:  # page1 -> data: [{...}, {...}, ...]
            article_list.extend(page_data)
        page += 1
    return article_list


def article_data(*args):
    """取得要的資料"""
    all_article = get_article_data()
    new_list = []
    for article in all_article:
        new_dict = {key: article[key] for key in args if key in article.keys()}
        new_list.append(new_dict)
    return new_list




