# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap)'

def search_query(q):
    # Try Commons generator
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=3&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                    info = pdata['imageinfo'][0]
                    return info.get('thumburl') or info.get('url')
    except Exception as e:
        pass

    # Try EN search generator
    url2 = f"https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=2&prop=pageimages&format=json&pithumbsize=1600"
    try:
        req2 = urllib.request.Request(url2, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req2, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
    except Exception as e:
        pass

    # Try BN search generator
    url3 = f"https://bn.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=2&prop=pageimages&format=json&pithumbsize=1600"
    try:
        req3 = urllib.request.Request(url3, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req3, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
    except Exception as e:
        pass

    return None

test_items = {
    "amjhupi": "আমঝুপি নীলকুঠি",
    "amjhupi_en": "Amjhupi Neelkuthi",
    "misripara": "Misripara",
    "misripara_bn": "মিশ্রিপাড়া",
    "kuakata_bihar": "Kuakata Buddhist Temple",
    "fatrar_char": "ফাতরার চর",
    "lebur_char": "লেবুর চর",
    "gangamati": "Gangamati Kuakata"
}

for k, q in test_items.items():
    u = search_query(q)
    print(f"{k} ({q}) -> {u[:65] if u else 'NONE'}")
