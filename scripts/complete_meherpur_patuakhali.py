# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap)'

TARGETS = {
    "meherpur": {
        "hero": ["Mujibnagar", "Mujibnagar Memorial"],
        "carousel-1": ["Mujibnagar", "মুজিবনগর স্মৃতিসৌধ"],
        "carousel-2": ["Mujibnagar Memorial", "Statue representing the signing"],
        "carousel-3": ["আমঝুপি নীলকুঠি", "Amjhupi Neelkuthi"],
        "carousel-4": ["Bhairab River", "ভৈরব নদী"],
        "carousel-5": ["Natural Landscape of Meherpur District", "Meherpur"],
        "hist-1": ["Mujibnagar", "Mujibnogor smritisoudho"],
        "hist-2": ["আমঝুপি নীলকুঠি", "Amjhupi Neelkuthi"],
        "hist-3": ["Mujibnagar Memorial", "মুজিবনগর"],
        "hist-4": ["Baidyanathtala", "Mujibnagar"],
        "hist-5": ["Meherpur District", "Meherpur"],
        "tour-1": ["Mujibnagar", "মুজিবনগর স্মৃতি উদ্যান"],
        "tour-2": ["আমঝুপি নীলকুঠি", "Amjhupi"],
        "tour-3": ["Bhairab River", "Voyrab River"],
        "tour-4": ["Meherpur", "Natural Landscape of Meherpur District"],
        "tour-5": ["Natural Landscape of Meherpur District", "Meherpur District"]
    },
    "patuakhali": {
        "hero": ["Kuakata", "Kuakata Beach"],
        "carousel-1": ["Kuakata Beach", "কুয়াকাটা সমুদ্র সৈকত"],
        "carousel-2": ["Misripara", "মিশ্রিপাড়া সীমা বিহার"],
        "carousel-3": ["লেবুর চর", "Lebur Char"],
        "carousel-4": ["ফাতরার চর", "Fatrar Char"],
        "carousel-5": ["Payra Bridge", "The Payra Bridge over the Payra River"],
        "hist-1": ["Kuakata Buddhist Temple", "কুয়াকাটা বৌদ্ধ মন্দির"],
        "hist-2": ["Misripara", "মিশ্রিপাড়া"],
        "hist-3": ["Patuakhali", "পটুয়াখালী"],
        "hist-4": ["Laukathi River", "Patuakhali"],
        "hist-5": ["Kalapara Upazila", "Patuakhali"],
        "tour-1": ["Kuakata Beach", "Kuakata sea beach evening"],
        "tour-2": ["ফাতরার চর", "Fatrar Char"],
        "tour-3": ["Gangamati Kuakata", "Gangamati"],
        "tour-4": ["লেবুর চর", "Lebur Char"],
        "tour-5": ["Payra Bridge", "The Payra Bridge over the Payra River"]
    }
}

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
    except Exception:
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
    except Exception:
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
    except Exception:
        pass

    return None

def download_and_crop(url, out_path, target_size=(1200, 675)):
    temp_file = out_path + ".temp"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=12) as resp, open(temp_file, 'wb') as f:
            f.write(resp.read())

        with Image.open(temp_file) as img:
            img = img.convert('RGB')
            target_w, target_h = target_size
            target_aspect = target_w / target_h
            img_aspect = img.width / img.height

            if img_aspect > target_aspect:
                new_w = int(img.height * target_aspect)
                offset_x = (img.width - new_w) // 2
                img = img.crop((offset_x, 0, offset_x + new_w, img.height))
            else:
                new_h = int(img.width / target_aspect)
                offset_y = (img.height - new_h) // 2
                img = img.crop((0, offset_y, img.width, offset_y + new_h))

            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img.save(out_path, 'WEBP', quality=88, method=6)

        if os.path.exists(temp_file):
            os.remove(temp_file)
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False

def main():
    total = 0
    ok = 0
    for slug, items in TARGETS.items():
        out_dir = os.path.join('images', 'districts', slug)
        os.makedirs(out_dir, exist_ok=True)
        for key, queries in items.items():
            total += 1
            out_path = os.path.join(out_dir, f"{key}.webp")
            found_url = None
            for q in queries:
                u = search_query(q)
                if u:
                    found_url = u
                    break
            
            if found_url and download_and_crop(found_url, out_path):
                ok += 1
                print(f"[{ok}/{total}] {slug}/{key}.webp -> OK from {found_url[:55]}...")
            else:
                print(f"[FAIL] {slug}/{key}.webp")

    print(f"\nCOMPLETED: {ok}/{total} images updated with authentic photographs!")

if __name__ == '__main__':
    main()
