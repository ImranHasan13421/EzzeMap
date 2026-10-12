import json, sys, re, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

districts_info = [
    {"name": "Munshiganj", "slug": "munshiganj", "pages": [4, 5, 6]},
    {"name": "Gazipur", "slug": "gazipur", "pages": [7, 8]},
    {"name": "Narsingdi", "slug": "narsingdi", "pages": [9, 10]},
    {"name": "Manikganj", "slug": "manikganj", "pages": [11, 12]},
    {"name": "Shariatpur", "slug": "shariatpur", "pages": [13, 14]},
    {"name": "Madaripur", "slug": "madaripur", "pages": [15, 16]},
    {"name": "Tangail", "slug": "tangail", "pages": [17, 18]},
    {"name": "Brahmanbaria", "slug": "brahmanbaria", "pages": [19, 20]},
    {"name": "Rajbari", "slug": "rajbari", "pages": [21, 22]},
    {"name": "Chandpur", "slug": "chandpur", "pages": [23, 24]},
    {"name": "Mymensingh", "slug": "mymensingh", "pages": [25, 26]},
    {"name": "Kishoreganj", "slug": "kishoreganj", "pages": [27, 28]},
    {"name": "Sirajganj", "slug": "sirajganj", "pages": [29, 30]},
    {"name": "Faridpur", "slug": "faridpur", "pages": [31, 32]},
    {"name": "Jamalpur", "slug": "jamalpur", "pages": [33, 34]}
]

for d in districts_info:
    name = d["name"]
    print(f"\n==================== {name.upper()} ====================")
    district_links = []
    district_blocks = []
    
    for p_num in d["pages"]:
        p = pages[p_num - 1]
        text = p["text"]
        # links sorted top-to-bottom
        links = p["links"]
        district_links.extend([l["uri"] for l in links])
        
        # split on "Open map ■"
        parts = text.split("Open map ■")
        # every part except the last one corresponds to a link on this page
        for part in parts[:-1]:
            district_blocks.append(part)
            
    print(f"Total links: {len(district_links)}, Total blocks: {len(district_blocks)}")
    
    for idx, (b, link) in enumerate(zip(district_blocks, district_links)):
        cat = "Historical" if idx < 5 else "Tourist"
        # Parse query from link
        parsed_url = urllib.parse.urlparse(link)
        query = urllib.parse.parse_qs(parsed_url.query).get('query', [''])[0]
        
        # Clean block text
        lines = [l.strip() for l in b.split('\n') if l.strip()]
        # remove page headers or table headers
        cleaned_lines = []
        skip_words = ['BANGLADESH', 'PAGE ', 'District', 'HISTORICAL &', 'TOURIST ATTRACTIONS', 'PLACE NAME', 'DESCRIPTION', 'EXACT LOCATION', 'GOOGLE', 'MAPS']
        for l in lines:
            if any(sw in l for sw in skip_words):
                continue
            cleaned_lines.append(l)
            
        print(f"[{cat} {idx%5 + 1}] Query: {query[:50]}... | Raw lines count: {len(cleaned_lines)}")
        if len(cleaned_lines) > 0:
            print(f"   First line: {cleaned_lines[0]}")
            print(f"   Last line:  {cleaned_lines[-1]}")
