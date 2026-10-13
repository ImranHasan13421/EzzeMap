# -*- coding: utf-8 -*-
import sys
import json
import urllib.request
import urllib.parse

sys.stdout.reconfigure(encoding='utf-8')
USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap)'

def check_wiki(title, lang='en'):
    clean = title.replace(' ', '_')
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(clean)}&prop=pageimages&format=json&pithumbsize=1000"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=4) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
    except Exception:
        pass
    return None

def check_commons(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1200&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=4) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                    info = pdata['imageinfo'][0]
                    return info.get('thumburl') or info.get('url')
    except Exception:
        pass
    return None

test_places = [
    ("Sixty Dome Mosque", "ষাট গম্বুজ মসজিদ"),
    ("Khan Jahan Ali's Tomb", "খান জাহান আলীর সমাধি"),
    ("Mahasthangarh", "মহাস্থানগড়"),
    ("Gokul Medh", "গোকুল মেধ"),
    ("Vasu Bihar", "ভাসু বিহার"),
    ("Natore Rajbari", "নাটোর রাজবাড়ি"),
    ("Uttara Ganabhaban", "উত্তরা গণভবন"),
    ("Shilaidaha Rabindra Kuthibari", "শিলাইদহ রবীন্দ্র কুঠিবাড়ি"),
    ("Lalon", "লালন শাহের মাজার"),
    ("Kuakata Beach", "কুয়াকাটা সমুদ্র সৈকত"),
    ("Mujibnagar Memorial", "মুজিবনগর স্মৃতিসৌধ"),
    ("Amjhupi Nilkuthi", "আমঝুপি নীলকুঠি"),
    ("Lawachara National Park", "লাউয়াছড়া জাতীয় উদ্যান"),
    ("Madhabkunda waterfall", "মাধবকুণ্ড জলপ্রপাত"),
    ("Michael Madhusudan Dutt", "মাইকেল মধুসূদন দত্তের বাড়ি"),
    ("Gajni Abakash", "গজনী অবকাশ"),
    ("Madhutila Eco Park", "মধুটিলা ইকোপার্ক"),
    ("Bhimruli", "ভিমরুলী ভাসমান পেয়ারা বাজার"),
    ("Barobazar", "বারোবাজার"),
    ("Carew & Co (Bangladesh) Ltd", "কেরু অ্যান্ড কোম্পানি")
]

for en_title, bn_title in test_places:
    url = check_wiki(en_title, 'en') or check_wiki(bn_title, 'bn') or check_commons(en_title) or check_commons(bn_title)
    print(f"{en_title} -> {url[:60] if url else 'NONE'}")
