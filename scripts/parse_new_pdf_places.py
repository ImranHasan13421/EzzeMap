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

all_districts = []

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
            
    items = []
    for idx, (b, link) in enumerate(zip(district_blocks, district_links)):
        cat_type = "historical" if idx < 5 else "tourist"
        item_id = (idx % 5) + 1
        
        # Link query info
        parsed_url = urllib.parse.urlparse(link)
        query_str = urllib.parse.parse_qs(parsed_url.query).get('query', [''])[0]
        query_unquoted = urllib.parse.unquote_plus(query_str).strip()
        
        # Clean lines from block
        raw_lines = [l.strip() for l in b.split('\n') if l.strip()]
        lines = []
        for l in raw_lines:
            # skip headers
            if any(h in l for h in ['BANGLADESH', 'PAGE ', 'HISTORICAL &', 'TOURIST ATTRACTIONS', 'PLACE NAME', 'DESCRIPTION', 'EXACT LOCATION', 'GOOGLE', 'MAPS']):
                continue
            if l.endswith('District') and len(l) < 30:
                continue
            lines.append(l)
            
        # Separate into Name, Description, Location
        # From bottom up: lines ending with Bangladesh or part of address belong to Location
        # Find where location starts:
        # In almost all entries, location ends with "Bangladesh" or area name.
        # And descriptions end with a period "."
        
        # Let's inspect the lines:
        # The location lines match parts of query_unquoted
        # Let's find split between description and location
        # A description sentence typically ends with '.', ';', or '!'
        
        # Find the last period in the middle
        # Any line after that last sentence ending is part of location!
        desc_end_idx = -1
        for i, l in enumerate(lines):
            # If line ends with period or is part of description
            # but wait, can location have a period? e.g. "St. Nicholas" is name.
            # Addresses don't usually end with period, they end with "Bangladesh".
            if l.endswith('.') and i > 0 and i < len(lines) - 1:
                desc_end_idx = i
                
        # If desc_end_idx is found:
        # Name is lines 0..name_end
        # But how many lines is Name?
        # Name is at the top. Let's see if query_unquoted starts with lines[0]
        # Let's determine name:
        name_lines = []
        desc_lines = []
        loc_lines = []
        
        # We can find name by matching the start of query_unquoted:
        # query_unquoted is typically "Name, Address, Bangladesh"
        # Let's find the comma in query_unquoted that separates name and location
        # But wait! Query_unquoted might be e.g. "Bhawal Rajbari, Joydebpur, Gazipur Sadar..."
        # If we take the first comma-separated segment of query_unquoted:
        q_parts = [p.strip() for p in query_unquoted.split(',') if p.strip()]
        q_name = q_parts[0] if q_parts else ""
        
        # Sometimes name in query has 2 words across 2 lines in text:
        # Let's accumulate text lines until we form the name:
        curr_name = ""
        n_idx = 0
        while n_idx < len(lines):
            test_name = (curr_name + " " + lines[n_idx]).strip()
            # check if test_name matches or starts q_name
            # or if lines[n_idx] is clearly part of description (starts with 'A ', 'This ', 'The ', etc.)
            clean_test = test_name.replace(" ", "").lower()
            clean_q = q_name.replace(" ", "").lower()
            if clean_test in clean_q or clean_q in clean_test:
                curr_name = test_name
                n_idx += 1
                if clean_test == clean_q:
                    break
            else:
                break
        if not curr_name and len(lines) > 0:
            curr_name = lines[0]
            n_idx = 1
            
        # Description is from n_idx to desc_end_idx + 1
        if desc_end_idx >= n_idx:
            desc_lines = lines[n_idx : desc_end_idx + 1]
            loc_lines = lines[desc_end_idx + 1 :]
        else:
            # Fallback: location is last 2-3 lines
            loc_lines = lines[-3:] if len(lines) >= 4 else lines[-1:]
            desc_lines = lines[n_idx : -len(loc_lines)]
            
        name_text = curr_name.strip()
        desc_text = " ".join(desc_lines).strip()
        loc_text = ", ".join([l.strip().rstrip(',') for l in loc_lines if l.strip()])
        
        # If loc_text is missing or malformed, fallback to query address
        if not loc_text or "Bangladesh" not in loc_text:
            if len(q_parts) > 1:
                loc_text = ", ".join(q_parts[1:])
                
        items.append({
            "id": item_id,
            "category": cat_type,
            "name": name_text,
            "query_name": q_name,
            "description": desc_text,
            "location": loc_text,
            "map_link": link,
            "raw_lines": lines
        })
        
    all_districts.append({
        "district": name,
        "slug": slug,
        "items": items
    })

print(f"Parsed {len(all_districts)} districts, {sum(len(d['items']) for d in all_districts)} total items.")

with open('scripts/new_pdf_parsed.json', 'w', encoding='utf-8') as f:
    json.dump(all_districts, f, ensure_ascii=False, indent=2)

