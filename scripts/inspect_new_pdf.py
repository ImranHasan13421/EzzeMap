import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages[3:10]: # pages 4 to 10
    print(f"=== PAGE {p['page']} (links: {len(p['links'])}) ===")
    lines = [l for l in p['text'].split('\n') if l.strip()]
    for l in lines[:20]:
        print('  ', l[:100])
