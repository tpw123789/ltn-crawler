import json
import get_data

all_article = get_data.get_all_article()

with open('ltn.json', 'w', encoding='utf-8') as f:
    json.dump(all_article, f, ensure_ascii=False, indent=4, sort_keys=True)
