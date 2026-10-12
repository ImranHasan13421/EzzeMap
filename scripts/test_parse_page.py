import json, re

with open('scripts/new_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# Inspect page 7 (Gazipur historical)
p7 = pages[6] # page 7
print("=== PAGE 7 LINKS ===")
for l in p7['links']:
    print(l['rect'], l['uri'])

print("\n=== PAGE 7 TEXT BLOCKS ===")
text = p7['text']
blocks = text.split("Open map ■")
for i, b in enumerate(blocks[:-1]):
    print(f"--- Block {i+1} ---")
    lines = [line.strip() for line in b.split('\n') if line.strip()]
    print("LINES:", lines)
