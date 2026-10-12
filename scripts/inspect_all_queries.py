import json, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Let's inspect each link across all pages 4..34
total_links = 0
for p in pages:
    if p['page'] < 4:
        continue
    for l in p['links']:
        total_links += 1
        uri = l['uri']
        parsed_url = urllib.parse.urlparse(uri)
        q = urllib.parse.parse_qs(parsed_url.query).get('query', [''])[0]
        unq = urllib.parse.unquote_plus(q)
        # check if unq has any weird chars
        # print first 50 chars
        if total_links <= 10 or '■' in unq or '?' in unq:
            print(f"Link {total_links:3d} (Page {p['page']:2d}): {unq}")

print(f"Total links across all pages: {total_links}")
