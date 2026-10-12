import pypdf
import json
import re

reader = pypdf.PdfReader('Bangladesh_Districts_Historical_and_Tourist_Places.pdf')

pages_info = [
    (2, 'Narayanganj'),
    (3, 'Feni'),
    (4, 'Cumilla'),
    (5, 'Bhola'),
    (6, 'Barishal'),
    (7, 'Chattogram'),
    (8, 'Sylhet'),
    (9, 'Noakhali'),
    (10, 'Rajshahi'),
    (11, "Cox's Bazar"),
    (12, 'Kurigram'),
    (13, 'Dinajpur')
]

# Read catalog to get district slug and info
with open('data/main-info/catalog.js', 'r', encoding='utf-8') as f:
    cat_text = f.read()

# match "slug": "...", "en": "..."
items = re.findall(r'"slug":\s*"([^"]+)",\s*"en":\s*"([^"]+)"', cat_text)
slug_map = {en.strip().lower(): slug for slug, en in items}

all_districts_data = []

for p_num, dist_name in pages_info:
    page = reader.pages[p_num - 1]
    raw_text = page.extract_text()
    
    # Extract links in top-to-bottom order (y descending)
    links = []
    if '/Annots' in page:
        for annot in page['/Annots']:
            obj = annot.get_object()
            if '/A' in obj and '/URI' in obj['/A']:
                uri = obj['/A']['/URI']
                rect = [float(x) for x in obj['/Rect']]
                links.append((rect[1], uri))
    links.sort(key=lambda x: x[0], reverse=True)
    
    key = dist_name.lower().replace("'", "").replace("’", "")
    slug = None
    for en_k, s in slug_map.items():
        if en_k.replace("'", "").replace("’", "") == key:
            slug = s
            break
    if not slug:
        slug = key.replace(' ', '-')

    all_districts_data.append({
        'page': p_num,
        'district': dist_name,
        'slug': slug,
        'raw_text': raw_text,
        'links': [u for _, u in links]
    })

print(f"Extracted {len(all_districts_data)} districts:")
for d in all_districts_data:
    print(f"  {d['district']} -> slug: {d['slug']}, links: {len(d['links'])}")

with open('scripts/extracted_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_districts_data, f, ensure_ascii=False, indent=2)
