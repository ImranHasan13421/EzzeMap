import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print(f"Total pages: {len(pages)}")
for p in pages:
    p_num = p['page']
    if p_num < 4:
        continue
    links = p['links']
    text = p['text']
    first_lines = [l.strip() for l in text.split('\n') if l.strip()][:3]
    print(f"Page {p_num:2d} | links: {len(links):2d} | {' // '.join(first_lines)}")
