# -*- coding: utf-8 -*-
import sys
import pypdf
import json

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('NEW PDF.pdf')

def dump_page(pno):
    page = reader.pages[pno - 1]
    print(f"=== PAGE {pno} TEXT ===")
    print(page.extract_text())
    
    print(f"=== PAGE {pno} LINKS ===")
    links = []
    if '/Annots' in page:
        annots = page['/Annots']
        for a in annots:
            obj = a.get_object()
            if '/A' in obj and '/URI' in obj['/A']:
                uri = obj['/A']['/URI']
                rect = obj.get('/Rect', [])
                links.append({'uri': str(uri), 'rect': [float(x) for x in rect]})
    print(json.dumps(links, indent=2))

dump_page(3)
dump_page(4)
