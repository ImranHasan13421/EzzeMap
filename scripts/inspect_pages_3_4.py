import json
import re

with open('scripts/new_20_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Let's see text of Page 3 and Page 4
print("=== PAGE 3 TEXT ===")
print(pages[2]['text'])
print("=== PAGE 3 LINKS ===")
for l in pages[2]['links']:
    print(l['uri'])

print("=== PAGE 4 TEXT ===")
print(pages[3]['text'])
print("=== PAGE 4 LINKS ===")
for l in pages[3]['links']:
    print(l['uri'])
