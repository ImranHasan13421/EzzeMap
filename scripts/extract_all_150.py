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

all_extracted = []

for d in districts_info:
    name = d["name"]
    slug = d["slug"]
    
    district_links = []
    district_blocks = []
    
    for p_num in d["pages"]:
        p = pages[p_num - 1]
        text = p["text"]
        links = p["links"]
        district_links.extend([l["uri"] for l in links])
        
        parts = text.split("Open map ■")
        for part in parts[:-1]:
            district_blocks.append(part)
            
    assert len(district_links) == 10, f"Expected 10 links for {name}, got {len(district_links)}"
    assert len(district_blocks) == 10, f"Expected 10 blocks for {name}, got {len(district_blocks)}"
    
    dist_items = []
    for idx, (b, link) in enumerate(zip(district_blocks, district_links)):
        cat_type = "historical" if idx < 5 else "tourist"
        item_id = (idx % 5) + 1
        
        parsed_url = urllib.parse.urlparse(link)
        q = urllib.parse.parse_qs(parsed_url.query).get('query', [''])[0]
        unq = urllib.parse.unquote_plus(q).strip()
        
        # Clean lines from block
        raw_lines = [l.strip() for l in b.split('\n') if l.strip()]
        lines = []
        for l in raw_lines:
            if any(h in l for h in ['BANGLADESH', 'PAGE ', 'HISTORICAL &', 'TOURIST ATTRACTIONS', 'PLACE NAME', 'DESCRIPTION', 'EXACT LOCATION', 'GOOGLE', 'MAPS']):
                continue
            if l.endswith('District') and len(l) < 30 and not 'area' in l.lower() and not 'confirm' in l.lower():
                continue
            lines.append(l)
            
        # The block has:
        # [0..k]: Name lines
        # [k+1..m]: Description lines (ends with period or similar sentence-ender)
        # [m+1..]: Location lines (ends with 'Bangladesh' or location details)
        
        # We can extract the location by finding where address begins
        # The location string in unq is everything after the first name part
        # Let's split unq:
        # We know Bangladesh is at the end of location.
        # Let's find the sentence ending with period before the address:
        
        # Find all lines ending with '.'
        period_indices = [i for i, l in enumerate(lines) if l.endswith('.') or l.endswith('!')]
        
        if period_indices:
            # The last sentence of the description is period_indices[-1]
            # (unless an address line happens to end with period, but addresses in this PDF end with 'Bangladesh' without period)
            last_desc_idx = period_indices[-1]
            # Check if there are lines after last_desc_idx that look like address
            loc_lines = lines[last_desc_idx + 1:]
            
            # Now find where name ends and description begins:
            # Description lines start with capital letters and form sentences.
            # Name lines match the beginning of unq:
            # Let's find the best split point between name and desc:
            name_lines = []
            desc_lines = []
            
            # Check lines 0, 1, 2 against unq:
            best_n = 1
            for n in range(1, min(4, last_desc_idx + 1)):
                test_name = " ".join(lines[:n]).lower().replace(" ", "").replace("-", "")
                unq_start = unq.lower().replace(" ", "").replace("-", "")
                if test_name in unq_start:
                    best_n = n
                    
            name_lines = lines[:best_n]
            desc_lines = lines[best_n : last_desc_idx + 1]
        else:
            name_lines = [lines[0]]
            desc_lines = lines[1:-2]
            loc_lines = lines[-2:]
            
        name_str = " ".join(name_lines).strip()
        desc_str = " ".join(desc_lines).strip()
        loc_str = ", ".join([l.strip().rstrip(',') for l in loc_lines if l.strip()])
        
        # Verify against unq:
        # If unq has the name, and unq starts with name_str or name_str has small diff:
        # unq is formatted as: "<Exact Name>, <Exact Location>"
        # Let's find comma in unq:
        parts = [p.strip() for p in unq.split(',') if p.strip()]
        
        # If loc_str is empty or doesn't have Bangladesh, use parts from unq:
        if not loc_str or "Bangladesh" not in loc_str:
            loc_str = ", ".join(parts[1:]) if len(parts) > 1 else loc_str
            
        # Clean up any unicode artifacts in name
        if '■' in name_str:
            # use query name
            name_str = parts[0]
            
        dist_items.append({
            "id": item_id,
            "category": cat_type,
            "name": name_str,
            "query_full": unq,
            "description": desc_str,
            "location": loc_str,
            "map_link": link
        })
        
    all_extracted.append({
        "district": name,
        "slug": slug,
        "items": dist_items
    })

with open('scripts/all_150_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(all_extracted, f, ensure_ascii=False, indent=2)

print("Saved all 150 items to scripts/all_150_extracted.json")
