# -*- coding: utf-8 -*-
import sys
import pypdf
import json
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('NEW PDF.pdf')

DISTRICT_NAMES = [
    ("Magura", "magura"),
    ("Narail", "narail"),
    ("Naogaon", "naogaon"),
    ("Satkhira", "satkhira"),
    ("Khagrachhari", "khagrachhari"),
    ("Joypurhat", "joypurhat"),
    ("Sunamganj", "sunamganj"),
    ("Gaibandha", "gaibandha"),
    ("Rangpur", "rangpur"),
    ("Rangamati", "rangamati"),
    ("Chapainawabganj", "chapainawabganj"),
    ("Bandarban", "bandarban"),
    ("Barguna", "barguna"),
    ("Lalmonirhat", "lalmonirhat"),
    ("Nilphamari", "nilphamari"),
    ("Thakurgaon", "thakurgaon"),
    ("Panchagarh", "panchagarh")
]

all_districts = {}

for idx, (dist_name, dist_slug) in enumerate(DISTRICT_NAMES):
    p1 = 3 + idx * 2
    p2 = 4 + idx * 2
    page1 = reader.pages[p1 - 1]
    page2 = reader.pages[p2 - 1]
    
    # Extract links from page 1 and page 2
    links1 = []
    if '/Annots' in page1:
        for a in page1['/Annots']:
            obj = a.get_object()
            if '/A' in obj and '/URI' in obj['/A']:
                uri = str(obj['/A']['/URI'])
                rect = [float(x) for x in obj.get('/Rect', [])]
                links1.append({'uri': uri, 'rect': rect})
    # Sort top to bottom (higher y first)
    links1.sort(key=lambda x: -x['rect'][1])

    links2 = []
    if '/Annots' in page2:
        for a in page2['/Annots']:
            obj = a.get_object()
            if '/A' in obj and '/URI' in obj['/A']:
                uri = str(obj['/A']['/URI'])
                rect = [float(x) for x in obj.get('/Rect', [])]
                links2.append({'uri': uri, 'rect': rect})
    links2.sort(key=lambda x: -x['rect'][1])

    all_links = links1 + links2
    print(f"[{idx+1}/17] {dist_name} (pages {p1}-{p2}): found {len(links1)} links on P{p1}, {len(links2)} links on P{p2}. Total: {len(all_links)}")

    # Extract query param from link uri to see place and location
    parsed_places = []
    for l_idx, l in enumerate(all_links):
        uri = l['uri']
        parsed = urllib.parse.urlparse(uri)
        q = urllib.parse.parse_qs(parsed.query).get('query', [''])[0]
        parsed_places.append({
            'index': l_idx + 1,
            'type': 'hist' if l_idx < 5 else 'tour',
            'full_query': q,
            'uri': uri
        })

    all_districts[dist_slug] = {
        'name': dist_name,
        'slug': dist_slug,
        'page1': p1,
        'page2': p2,
        'places': parsed_places,
        'text_page1': page1.extract_text(),
        'text_page2': page2.extract_text()
    }

with open('scripts/all_17_extracted_raw.json', 'w', encoding='utf-8') as f:
    json.dump(all_districts, f, ensure_ascii=False, indent=2)

print(f"\nSuccessfully parsed all 17 districts into scripts/all_17_extracted_raw.json!")
