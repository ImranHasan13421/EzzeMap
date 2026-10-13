import pypdf
import json
import re

reader = pypdf.PdfReader('f:/EzzeMap/NEW PDF.pdf')
print(f"Total pages: {len(reader.pages)}")

# Let's check catalog slugs
with open('data/main-info/catalog.js', 'r', encoding='utf-8') as f:
    text = f.read()

slugs = re.findall(r'"slug":\s*"([^"]+)"', text)
print(f"Total catalog districts: {len(slugs)}")

districts_to_find = [
    "lakshmipur", "gopalganj", "habiganj", "pabna", "netrokona",
    "noakhali", "sherpur", "jashore", "jhalokathi", "moulvibazar",
    "bagerhat", "bogura", "natore", "pirojpur", "kushtia",
    "jhenaidah", "khulna", "chuadanga", "meherpur", "patuakhali"
]

print("Checking presence in catalog:")
for d in districts_to_find:
    found = d in slugs
    print(f"  {d}: {'FOUND' if found else 'NOT FOUND'}")
    if not found:
        # check partial
        matches = [s for s in slugs if d[:4] in s]
        print(f"    candidates: {matches}")
