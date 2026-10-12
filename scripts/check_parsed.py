import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_parsed.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    print('='*60)
    print(f"District: {d['district']} ({len(d['items'])} items)")
    for it in d['items']:
        print(f"  [{it['category'][:4].upper()} {it['id']}] Name: {it['name']} (Query: {it['query_name']})")
        print(f"         Loc:  {it['location']}")
        print(f"         Desc: {it['description'][:85]}...")
