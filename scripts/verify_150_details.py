import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_150_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    print(f"================ {d['district'].upper()} ({d['slug']}) ================")
    for item in d['items']:
        tag = f"[{item['category'][:4].upper()}-{item['id']}]"
        print(f"{tag:7s} Name: {item['name']}")
        print(f"        Loc:  {item['location']}")
        print(f"        Desc: {item['description'][:90]}...")
        print(f"        Link: {item['map_link'][:70]}...")
