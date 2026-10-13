import pypdf
import json

reader = pypdf.PdfReader('f:/EzzeMap/NEW PDF.pdf')

pages_data = []

for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ''
    # extract annotations/links if any
    links = []
    if '/Annots' in page:
        annots = page['/Annots']
        for annot in annots:
            obj = annot.get_object()
            if '/A' in obj and '/URI' in obj['/A']:
                uri = obj['/A']['/URI']
                rect = [float(x) for x in obj.get('/Rect', [])]
                links.append({'uri': uri, 'rect': rect})
    pages_data.append({
        'page': idx + 1,
        'text': text,
        'links': links
    })

with open('scripts/new_20_pdf_dump.json', 'w', encoding='utf-8') as f:
    json.dump(pages_data, f, ensure_ascii=False, indent=2)

print(f"Dumped {len(pages_data)} pages.")
for p in pages_data:
    first_lines = [l.strip() for l in p['text'].splitlines() if l.strip()][:3]
    print(f"Page {p['page']} ({len(p['links'])} links): {' | '.join(first_lines)}")
