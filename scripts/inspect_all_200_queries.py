import json
import urllib.parse
import re

with open('scripts/all_200_raw.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

for slug, d in raw.items():
    print(f"\n==================== {d['name']} ====================")
    p1_text = d['p1_text']
    p2_text = d['p2_text']
    
    # check where 'Five tourist' appears
    print(f"P1 text has 'Five tourist': {'Five tourist' in p1_text}")
    print(f"P2 text has 'Five tourist': {'Five tourist' in p2_text}")
    
    # Print decoded links
    print(f"Total links: {len(d['hist_links'])} + {len(d['tour_links'])}")
    for i, l in enumerate(d['hist_links']):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(l).query).get('query', [''])[0]
        print(f"  Hist {i+1}: {q}")
    for i, l in enumerate(d['tour_links']):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(l).query).get('query', [''])[0]
        print(f"  Tour {i+1}: {q}")
