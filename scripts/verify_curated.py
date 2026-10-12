import importlib
import sys

import os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))

slugs = ['narayanganj', 'feni', 'cumilla', 'bhola', 'barishal', 'chattogram', 'sylhet', 'noakhali', 'rajshahi', 'coxs_bazar', 'kurigram', 'dinajpur']
for s in slugs:
    mod = importlib.import_module(f'scripts.data_districts.{s}')
    d = mod.DISTRICT_DATA
    print(f"OK: {d['en']} ({d['slug']}) -> {len(d['hist'])} hist, {len(d['tour'])} tour, {len(d['carousel'])} carousel")
