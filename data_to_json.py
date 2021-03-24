import json
import get_data

articles = get_data.article_data()
with open('ltn.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=4, sort_keys=True)
