import time
import json
from get_data import article_data

start = time.time()
articles = article_data('no', 'title', 'time', 'url', 'tagText')
with open('ltn.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4, sort_keys=True)
end = time.time()
print('完成\n執行時間：', end - start)


