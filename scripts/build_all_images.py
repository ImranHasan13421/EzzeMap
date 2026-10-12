# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw, ImageFont
import importlib

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))

USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap; contact: imranhasan13421@gmail.com)'

# Custom curated search keywords for places that have specific Wikipedia/Wikimedia article names
CUSTOM_SEARCH_KEYS = {
    # Narayanganj
    "Panam Nagar": ["Panam Nagar", "Sonargaon"],
    "Bangladesh Folk Art and Crafts Foundation": ["Bangladesh Folk Art and Crafts Foundation", "Sonargaon"],
    "Goaldi Mosque": ["Goaldi Mosque", "Sonargaon"],
    "Hajiganj Fort": ["Hajiganj Fort", "Narayanganj"],
    "Sonakanda Fort": ["Sonakanda Fort", "Bandar, Narayanganj"],
    "Murapara Rajbari": ["Murapara Rajbari", "Murapara"],
    "Zinda Park": ["Zinda Park", "Rupganj"],
    "Langalbandh": ["Langalbandh", "Old Brahmaputra River"],
    "Mary Anderson Floating Restaurant": ["Mary Anderson Floating Restaurant", "Fatullah, Narayanganj"],
    "DC Theme Park": ["Narayanganj District", "Narayanganj"],

    # Feni
    "Bijoy Singh Dighi": ["Bijoy Singh Dighi", "Feni, Bangladesh"],
    "Rajajhir Dighi": ["Rajajhir Dighi", "Feni, Bangladesh"],
    "Shamsher Gazi's Dighi": ["Shamsher Gazi", "Chhagalnaiya"],
    "Feni Government College": ["Feni Government College", "Feni, Bangladesh"],
    "Trunk Road town centre": ["Feni, Bangladesh", "Grand Trunk Road"],
    "Muhuri Project": ["Muhuri Project", "Muhuri Dam", "Sonagazi Upazila"],
    "Feni River": ["Feni River", "Feni District"],
    "Sonagazi coastal area": ["Sonagazi Upazila", "Feni District"],
    "Feni Children's Park": ["Feni, Bangladesh"],
    "Chhagalnaiya countryside": ["Chhagalnaiya Upazila", "Feni District"],

    # Cumilla
    "Shalban Vihara": ["Shalban Vihara", "Mainamati"],
    "Mainamati Museum": ["Mainamati", "Shalban Vihara"],
    "Itakhola Mura": ["Itakhola Mura", "Mainamati"],
    "Rupban Mura": ["Rupban Mura", "Mainamati"],
    "Ananda Vihara": ["Ananda Vihara", "Mainamati"],
    "Dharmasagar": ["Dharmasagar", "Comilla"],
    "Lalmai Hills": ["Lalmai Hills", "Mainamati"],
    "Magic Paradise Park": ["Kotbari, Comilla", "Comilla"],
    "Bangladesh Academy for Rural Development (BARD)": ["Bangladesh Academy for Rural Development", "Comilla model"],
    "Cumilla City Park": ["Comilla", "Dharmasagar"],

    # Bhola
    "Char Fasson town centre": ["Char Fasson Upazila", "Jacob Tower"],
    "Bhola Government High School": ["Bhola Government High School", "Bhola, Bangladesh"],
    "Bhola Government College": ["Bhola Government College", "Bhola, Bangladesh"],
    "Tazumuddin settlement area": ["Tazumuddin Upazila", "Bhola District"],
    "Daulatkhan river-port area": ["Daulatkhan Upazila", "Bhola District"],
    "Char Kukri Mukri Wildlife Sanctuary": ["Char Kukri Mukri Wildlife Sanctuary", "Char Kukri Mukri"],
    "Monpura Island": ["Monpura Island", "Monpura Upazila"],
    "Dhal Char": ["Dhal Char", "Char Fasson Upazila"],
    "Tarua Beach": ["Tarua Beach", "Dhal Char", "Char Fasson"],
    "Tulatuli riverbank": ["Bhola District", "Meghna River"],

    # Barishal
    "Oxford Mission Church": ["Oxford Mission Church", "Epiphany Church, Barisal"],
    "Lakutia Zamindar Bari": ["Lakutia Zamindar Bari", "Barisal"],
    "Kasba Mosque": ["Kasba Mosque", "Gournadi Upazila"],
    "Satyendra Smriti Gandhi Ashram": ["Bakerganj Upazila", "Barisal District"],
    "Mukunda Das Kali Temple": ["Mukunda Das", "Barisal"],
    "Baitul Aman Jame Masjid Complex (Guthia Mosque)": ["Baitul Aman Jame Masjid Complex", "Guthia Mosque"],
    "Durga Sagar Dighi": ["Durga Sagar", "Madhabpasha"],
    "Bell's Park": ["Bangabandhu Udyan", "Barisal"],
    "Barishal Muktijoddha Park": ["Barisal", "Kirtankhola"],
    "Kirtankhola riverfront": ["Kirtankhola", "Barisal launch terminal"],

    # Chattogram
    "Anderkilla Shahi Jame Mosque": ["Anderkilla Shahi Jame Mosque", "Anderkilla"],
    "Chandanpura Mosque": ["Chandanpura Mosque", "Chittagong"],
    "Chattogram War Cemetery": ["Chittagong War Cemetery", "Chittagong"],
    "Chattogram Court Building": ["Chittagong Court Building", "Parir Pahar"],
    "Ethnological Museum": ["Ethnological Museum of Chittagong", "Agrabad"],
    "Patenga Sea Beach": ["Patenga", "Chittagong"],
    "Foy's Lake": ["Foy's Lake", "Pahartali"],
    "Batali Hill": ["Batali Hill", "Tigerpass, Chittagong"],
    "Bhatiari Lake": ["Bhatiari", "Sitakunda"],
    "CRB (Central Railway Building) area": ["Central Railway Building", "Chittagong"],

    # Sylhet
    "Hazrat Shah Jalal Mazar Sharif": ["Shah Jalal Dargah", "Shah Jalal"],
    "Hazrat Shah Paran Mazar Sharif": ["Shah Paran", "Sylhet"],
    "Ali Amjad's Clock": ["Ali Amjad's Clock", "Keane Bridge"],
    "Keane Bridge": ["Keane Bridge", "Surma River"],
    "Shahi Eidgah": ["Shahi Eidgah, Sylhet", "Sylhet"],
    "Ratargul Swamp Forest": ["Ratargul Swamp Forest", "Sylhet"],
    "Jaflong": ["Jaflong", "Piyain River"],
    "Bichanakandi": ["Bichanakandi", "Sylhet"],
    "Lalakhal": ["Lalakhal", "Jaintiapur"],
    "Malnicherra Tea Estate": ["Malnicherra Tea Estate", "Tea production in Bangladesh"],

    # Noakhali
    "Bajra Shahi Mosque": ["Bajra Shahi Mosque", "Sonaimuri"],
    "Gandhi Ashram Trust": ["Gandhi Ashram Trust", "Noakhali"],
    "Noakhali Zilla School": ["Noakhali Zilla School", "Maijdee"],
    "Noakhali Government College": ["Noakhali Government College", "Maijdee"],
    "Noakhali District Collectorate": ["Maijdee", "Noakhali District"],
    "Nijhum Dweep National Park": ["Nijhum Dweep National Park", "Nijhum Dweep"],
    "Musapur Sea Beach": ["Musapur, Companiganj", "Companiganj Upazila, Noakhali"],
    "Chairman Ghat": ["Hatiya Upazila", "Noakhali District"],
    "Noakhali Science and Technology University campus": ["Noakhali Science and Technology University", "Sonapur"],
    "Noakhali Khal (canal) area": ["Noakhali District", "Maijdee"],

    # Rajshahi
    "Bagha Mosque": ["Bagha Mosque", "Bagha Upazila"],
    "Varendra Research Museum": ["Varendra Research Museum", "Rajshahi"],
    "Puthia Rajbari": ["Puthia Rajbari", "Puthia Temple Complex"],
    "Puthia Bara Ahnik Mandir": ["Bara Ahnik Mandir", "Puthia Temple Complex"],
    "Puthia Shiva Temple": ["Puthia Shiva Temple", "Bhubaneshwar Shiva Mandir"],
    "Padma Garden": ["Padma River", "Rajshahi"],
    "T-Badh": ["Padma River", "Rajshahi"],
    "Shah Makhdum Ruposh Mazar Sharif": ["Shah Makhdum Ruposh", "Rajshahi"],
    "Rajshahi Central Park and Zoo": ["Shaheed A.H.M. Qamaruzzaman Central Park and Zoo", "Rajshahi"],
    "Padma Riverfront": ["Padma River", "Rajshahi"],

    # Cox's Bazar
    "Aggmeda Khyang": ["Aggmeda Khyang", "Cox's Bazar"],
    "Ramu Central Seema Bihar": ["Ramu Upazila", "Cox's Bazar"],
    "Adinath Temple": ["Adinath Temple, Maheshkhali", "Maheshkhali"],
    "Ramu Buddhist Temple": ["Ramu Upazila", "Cox's Bazar"],
    "Dulahazara Buddhist temple area": ["Dulahazara Safari Park", "Chakaria Upazila"],
    "Laboni Point Sea Beach": ["Cox's Bazar Beach", "Laboni Beach"],
    "Inani Beach": ["Inani Beach", "Cox's Bazar"],
    "Himchari National Park": ["Himchari National Park", "Cox's Bazar"],
    "Marine Drive Road": ["Marine Drive, Cox's Bazar", "Cox's Bazar"],
    "Sonadia Island": ["Sonadia Island", "Maheshkhali"],

    # Kurigram
    "Chilmari River Port": ["Chilmari Upazila", "Brahmaputra River"],
    "Ulipur Munshi Bari": ["Ulipur Upazila", "Kurigram District"],
    "Balarhat Mosque": ["Nageshwari Upazila", "Kurigram District"],
    "Dharla Bridge": ["Dharla River", "Kurigram District"],
    "Sona Hat Bridge": ["Bhurungamari Upazila", "Dudhkumar River"],
    "Dharla Riverbank": ["Dharla River", "Kurigram District"],
    "Brahmaputra Riverbank, Chilmari": ["Chilmari Upazila", "Brahmaputra River"],
    "Dudhkumar River": ["Dudhkumar River", "Kurigram District"],
    "Jatrapur Hat": ["Kurigram Sadar Upazila", "Kurigram District"],
    "Char Rajibpur riverine area": ["Char Rajibpur Upazila", "Kurigram District"],

    # Dinajpur
    "Kantajew Temple (Kantaji Temple)": ["Kantajew Temple", "Kaharole Upazila"],
    "Dinajpur Rajbari": ["Dinajpur Rajbari", "Dinajpur, Bangladesh"],
    "Nayabad Mosque": ["Nayabad Mosque", "Kaharole Upazila"],
    "Sura Mosque": ["Sura Mosque", "Ghoraghat Upazila"],
    "Chehelgazi Mosque and Shrine": ["Chehelgazi", "Dinajpur, Bangladesh"],
    "Ramsagar National Park": ["Ramsagar", "Dinajpur, Bangladesh"],
    "Swapnapuri Amusement Park": ["Swapnapuri", "Nawabganj Upazila, Dinajpur"],
    "Singra National Park": ["Singra National Park", "Birganj Upazila"],
    "Dinajpur Town Park": ["Dinajpur, Bangladesh"],
    "Ghughu-Danga Zamindar Bari": ["Dinajpur Sadar Upazila", "Dinajpur, Bangladesh"],
}

def search_wikimedia_image(query_list):
    for q in query_list:
        clean = q.replace(' ', '_')
        # 1. Direct pageimage query
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(clean)}&prop=pageimages&format=json&pithumbsize=1600"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'thumbnail' in pdata:
                        return pdata['thumbnail']['source']
        except Exception:
            pass

        # 2. Generator search query
        url2 = f"https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&prop=pageimages&format=json&pithumbsize=1600"
        try:
            req2 = urllib.request.Request(url2, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req2, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'thumbnail' in pdata:
                        return pdata['thumbnail']['source']
        except Exception:
            pass

        # 3. Commons image search
        url3 = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
        try:
            req3 = urllib.request.Request(url3, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req3, timeout=5) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                        info = pdata['imageinfo'][0]
                        return info.get('thumburl') or info.get('url')
        except Exception:
            pass
            
    return None

def download_and_crop(url, out_path, target_size=(1200, 675)):
    temp_file = out_path + ".temp"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=12) as response, open(temp_file, 'wb') as out_file:
            out_file.write(response.read())

        with Image.open(temp_file) as img:
            img = img.convert('RGB')
            # Center crop to target aspect ratio
            target_w, target_h = target_size
            target_aspect = target_w / target_h
            img_aspect = img.width / img.height

            if img_aspect > target_aspect:
                # Image is wider: crop width
                new_w = int(img.height * target_aspect)
                offset_x = (img.width - new_w) // 2
                img = img.crop((offset_x, 0, offset_x + new_w, img.height))
            else:
                # Image is taller: crop height
                new_h = int(img.width / target_aspect)
                offset_y = (img.height - new_h) // 2
                img = img.crop((0, offset_y, img.width, offset_y + new_h))

            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img.save(out_path, 'WEBP', quality=85, method=6)

        if os.path.exists(temp_file):
            os.remove(temp_file)
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        print(f"  Failed download: {e}")
        return False

# Palette definitions for artistic fallback
PALETTES = [
    ((6, 95, 70), (4, 47, 34)),      # Deep Emerald to Forest
    ((15, 23, 42), (8, 47, 73)),     # Slate Navy to Ocean
    ((127, 29, 29), (69, 10, 10)),   # Crimson Red to Maroon
    ((19, 78, 74), (4, 47, 46)),     # Deep Teal to Cypress
    ((49, 46, 129), (17, 24, 39)),   # Indigo to Obsidian
    ((120, 53, 15), (69, 26, 3)),    # Warm Amber to Rust
]

def generate_artistic_fallback(out_path, title, subtitle, tag, palette_idx=0, target_size=(1200, 675)):
    width, height = target_size
    color_start, color_end = PALETTES[palette_idx % len(PALETTES)]
    img = Image.new("RGB", (width, height), color=color_start)
    draw = ImageDraw.Draw(img)

    # Vertical gradient
    r1, g1, b1 = color_start
    r2, g2, b2 = color_end
    for y in range(height):
        ratio = y / height
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Decorative geometric arcs
    draw.ellipse([width - 350, -100, width + 150, 400], outline=(255, 255, 255, 25), width=3)
    draw.ellipse([width - 280, -50, width + 100, 350], outline=(16, 185, 129, 60), width=2)
    draw.ellipse([-100, height - 300, 300, height + 100], outline=(244, 42, 65, 40), width=2)

    # Tag Badge
    draw.rounded_rectangle([60, height - 170, 260, height - 130], radius=8, fill=(16, 185, 129))
    draw.text((75, height - 160), tag, fill=(255, 255, 255))

    # Titles
    draw.text((60, height - 115), title, fill=(255, 255, 255))
    draw.text((60, height - 75), subtitle, fill=(203, 213, 225))
    draw.text((width - 240, 40), "EZZE MAP • BD 64", fill=(148, 163, 184))

    img.save(out_path, "WEBP", quality=85, method=6)

print("build_all_images helper loaded successfully.")
