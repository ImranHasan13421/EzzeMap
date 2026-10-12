import json, sys, re
import urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Define district definitions
districts_info = [
    {"name": "Munshiganj", "pages": [4, 5, 6]},
    {"name": "Gazipur", "pages": [7, 8]},
    {"name": "Narsingdi", "pages": [9, 10]},
    {"name": "Manikganj", "pages": [11, 12]},
    {"name": "Shariatpur", "pages": [13, 14]},
    {"name": "Madaripur", "pages": [15, 16]},
    {"name": "Tangail", "pages": [17, 18]},
    {"name": "Brahmanbaria", "pages": [19, 20]},
    {"name": "Rajbari", "pages": [21, 22]},
    {"name": "Chandpur", "pages": [23, 24]},
    {"name": "Mymensingh", "pages": [25, 26]},
    {"name": "Kishoreganj", "pages": [27, 28]},
    {"name": "Sirajganj", "pages": [29, 30]},
    {"name": "Faridpur", "pages": [31, 32]},
    {"name": "Jamalpur", "pages": [33, 34]}
]

# Let's inspect each district
for dist in districts_info:
    name = dist["name"]
    total_links = 0
    all_links = []
    for p_num in dist["pages"]:
        p = pages[p_num - 1]
        total_links += len(p["links"])
        all_links.extend(p["links"])
    print(f"District: {name:15s} | Pages: {dist['pages']} | Total links: {total_links}")

