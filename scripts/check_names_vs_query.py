import json, urllib.parse, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_150_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    for it in d['items']:
        name = it['name']
        q_name = urllib.parse.unquote_plus(urllib.parse.parse_qs(urllib.parse.urlparse(it['map_link']).query).get('query', [''])[0]).split(',')[0].strip()
        if name != q_name:
            print(f"{d['slug']:12s} [{it['category'][:4]}-{it['id']}] Name: \"{name}\"  |  Query: \"{q_name}\"")
