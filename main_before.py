# 自由時報
from urllib.request import urlopen, Request
import json
import time
from bs4 import BeautifulSoup
# 報導種類
categories = ['all', 'popular', 'politics', 'society', 'life', 'world', 'local', 'novelty']
base = 'https://news.ltn.com.tw/ajax/breakingnews/'
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
ltn = {'articles': []}


def get_data(url):
    request = Request(url, headers=headers)
    with urlopen(request) as response:
        data = response.read().decode('utf-8')
        data = json.loads(data)
    return data


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


# 文章資訊 -> dic
def article_to_dic(dic):
    no = dic['no']
    title = dic['title']
    article_time = dic['time']
    url = dic['url']
    tag_text = dic['tagText']
    ltn['articles'].append({
        'no': no,
        'title': title,
        'time': article_time,
        'url': url,
        'tag_text': tag_text,
        'content': article_content(url)
    })


# 取得文章
def get_article(category):
    article_num = 0
    page = 1
    while True:
        tmp = []
        target_url = get_data(base + category + '/' + str(page))
        target_data = target_url['data']
        if page == 1:
            for index, value in enumerate(target_data):
                article_num += 1
                article_to_dic(target_data[index])
                # print(target_data[index])
                # time.sleep(1)
                print(category, article_num, '......')
        if page >= 2:
            for index, value in enumerate(target_data):
                tmp.append(value)
                article_num += 1
                article_to_dic(target_data[tmp[index]])
                # print(target_data[tmp[index]])
                # time.sleep(1)
                print(category, article_num, '......')
        if len(target_data) == 0:
            break
        page += 1
    return article_num


num = 0

for c in range(1):
    start = time.time()
    num += get_article(categories[c])
    end = time.time()
    time.sleep(5)
    print('完成爬取', c, ' 執行時間：', end - start, ' 累計', num, '篇文章')

with open('ltn.json', 'w', encoding='utf-8') as f:
    json.dump(ltn, f, ensure_ascii=False, indent=4, sort_keys=True)
