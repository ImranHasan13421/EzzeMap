# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap; contact: imranhasan13421@gmail.com)'

TARGET_SLUGS = [
    "lakshmipur", "gopalganj", "habiganj", "pabna", "netrokona",
    "noakhali", "sherpur", "jashore", "jhalokathi", "moulvibazar",
    "bagerhat", "bogura", "natore", "pirojpur", "kushtia",
    "jhenaidah", "khulna", "chuadanga", "meherpur", "patuakhali"
]

CUSTOM_SEARCH_KEYS = {
    # Lakshmipur
    "Dalal Bazar Zamindar Bari": ["Dalal Bazar Zamindar Bari", "Lakshmipur Sadar Upazila"],
    "Tita Khan Jame Mosque (Jinn Mosque)": ["Raipur Upazila, Lakshmipur", "Tita Khan Mosque"],
    "Khowasagar Dighi": ["Dalal Bazar", "Lakshmipur District"],
    "Mita Khan Mosque": ["Lakshmipur District"],
    "Shahi Jame Mosque of Raipur": ["Raipur Upazila, Lakshmipur"],
    "Ramgati Meghna Riverfront": ["Ramgati Upazila", "Meghna River"],
    "Char Alexander Beach & Meghna Viewpoint": ["Char Alexander", "Ramgati Upazila"],
    "Raipur Fishery Hatchery & Green Belt": ["Raipur Upazila, Lakshmipur"],
    "Kamalnagar Meghna Riverside": ["Kamalnagar Upazila", "Meghna River"],
    "Maju Chowdhury Hat River Terminal": ["Lakshmipur Sadar Upazila", "Meghna River"],

    # Gopalganj
    "Bangabandhu Mausoleum Complex": ["Mausoleum of Bangabandhu Sheikh Mujibur Rahman", "Tungipara", "Bangabandhu Mausoleum"],
    "Tungipara Historic Home & Canal": ["Tungipara Upazila", "Gopalganj District"],
    "Orakandi Thakur Bari": ["Orakandi", "Matua Mahasangha", "Kashiani Upazila"],
    "Ulpur Zamindar Bari": ["Ulpur", "Gopalganj Sadar Upazila"],
    "Dhanuka Shiv Mandir": ["Gopalganj District"],
    "Madhumati Riverfront Boulevard": ["Madhumati River", "Gopalganj"],
    "Bilir Par Wetlands & Water Lily Sanctuary": ["Gopalganj District", "Water lily Bangladesh"],
    "Gopalganj City Park & Lake": ["Gopalganj town"],
    "Kotalipara Waterways & Floating Boat Bazaars": ["Kotalipara Upazila"],
    "Bangabandhu Memorial Museum & Library Grounds": ["Tungipara", "Sheikh Mujibur Rahman"],

    # Habiganj
    "Baniachong Historic Rajbari & Village": ["Baniachong Upazila", "Habiganj District"],
    "Shankarsena Dighi": ["Baniachong Upazila", "Habiganj"],
    "Uchail Shahi Jame Mosque": ["Habiganj Sadar Upazila"],
    "Bithangal Akhra": ["Bithangal Akhra", "Baniachong Upazila"],
    "Chowdhury Bari of Nabiganj": ["Nabiganj Upazila"],
    "Satchari National Park": ["Satchari National Park", "Habiganj"],
    "Rema-Kalenga Wildlife Sanctuary": ["Rema-Kalenga Wildlife Sanctuary", "Chunarughat Upazila"],
    "Bahubal Tea Estates & Rolling Hills": ["Bahubal Upazila", "Tea garden Bangladesh"],
    "Bibiyana Natural Gas Landscape": ["Bibiyana Gas Field", "Nabiganj Upazila"],
    "Chunarughat Green Hills & Ethnic Trails": ["Chunarughat Upazila", "Tripura ethnic Bangladesh"],

    # Pabna
    "Tarash Rajbari": ["Tarash Rajbari", "Pabna town"],
    "Chatmohar Shahi Mosque": ["Chatmohar Shahi Mosque", "Chatmohar Upazila"],
    "Suchitra Sen Ancestral Memorial Home": ["Suchitra Sen", "Pabna"],
    "Gopal Chandra Mandir (Jor Bangla Temple)": ["Jor Bangla Temple, Pabna", "Pabna"],
    "Sitlai Zamindar Bari": ["Pabna Sadar Upazila"],
    "Hardinge Bridge & Paksey Railway Vista": ["Hardinge Bridge", "Paksey"],
    "Lalon Shah Bridge Paksey Approach": ["Lalon Shah Bridge", "Paksey"],
    "Pabna Mental Hospital Heritage Grounds": ["Pabna Mental Hospital", "Pabna"],
    "Ichamati Riverfront Promenade": ["Ichamati River, Pabna", "Pabna"],
    "Gajnar Beel Wetlands": ["Sujanagar Upazila", "Pabna District"],

    # Netrokona
    "Susang Durgapur Rajbari Ruins": ["Durgapur Upazila, Netrokona", "Susang"],
    "Roail Shahi Mosque": ["Kendua Upazila", "Netrokona District"],
    "Ranikhong Catholic Church": ["Ranikhong", "Durgapur, Netrokona"],
    "Bishwa Shanti Stupa": ["Durgapur Upazila, Netrokona"],
    "Garo Pahar Heritage Settlements": ["Garo people", "Netrokona District"],
    "Bijoypur White Clay Hills (China Clay Lake)": ["Birishiri", "Durgapur Upazila, Netrokona"],
    "Someshwari River Bank & Sands": ["Someshwari River", "Netrokona"],
    "Birishiri Cultural Academy Grounds": ["Birishiri", "Tribal Cultural Academy"],
    "Dingapota Haor Expanses": ["Mohanganj Upazila", "Haor"],
    "Kangsher Haor Wetlands & Watchtower": ["Netrokona District", "Haor Bangladesh"],

    # Noakhali
    "Gandhi Ashram": ["Gandhi Ashram Trust", "Noakhali District", "Sonaimuri Upazila"],
    "Bajra Shahi Mosque": ["Bajra Shahi Mosque", "Sonaimuri Upazila"],
    "Queen Laksmi Temple & Dighi": ["Noakhali District"],
    "Talukdar Bari Historic Complex": ["Begumganj Upazila", "Noakhali"],
    "Ramalinga Math": ["Noakhali District"],
    "Nijhum Dwip National Park": ["Nijhum Dwip", "Hatiya Upazila"],
    "Musapur Regulator & Coastal Beach": ["Companiganj Upazila, Noakhali", "Musapur Regulator"],
    "Swarna Dwip": ["Hatiya Upazila", "Meghna River"],
    "Noakhali Canal Promenade & Town Park": ["Maijdee", "Noakhali"],
    "Hatiya Island Coastal Mangroves": ["Hatiya Island", "Noakhali"],

    # Sherpur
    "Garh Jaripa Fort & Ancient Ramparts": ["Garh Jaripa", "Sherpur District"],
    "Ghagra Laskar Khan Jame Mosque": ["Jhenaigati Upazila", "Sherpur"],
    "Nalitabari Colonial Outpost Remains": ["Nalitabari Upazila", "Sherpur"],
    "Maisaheba Jame Mosque": ["Sherpur town", "Sherpur District"],
    "Baraduari Historic Enclosure": ["Sherpur District"],
    "Gajni Abakash Leisure & Hill Park": ["Gajni Abakash", "Jhenaigati Upazila"],
    "Madhutila Eco Park": ["Madhutila Eco Park", "Nalitabari Upazila"],
    "Bhogai River Valley & Stone Beds": ["Bhogai River", "Nalitabari"],
    "Garo Hill Footpath Trails": ["Garo Hills", "Sherpur District"],
    "Sherpur Lake City & Botanical Grounds": ["Sherpur town"],

    # Jashore
    "Michael Madhusudan Dutt Memorial (Sagardari)": ["Sagardari", "Michael Madhusudan Dutt"],
    "Jessore Collectorate Building": ["Jessore town", "Jashore District"],
    "Chanchra Rajbari & Shiv Mandir": ["Chanchra Rajbari", "Jashore Sadar Upazila"],
    "Mirzanagar Hammamkhana": ["Keshabpur Upazila", "Mirzanagar Hammamkhana"],
    "Imam Bari Historic Complex": ["Jashore town"],
    "Gadkhali Flower Markets & Fields": ["Gadkhali", "Jhikargachha Upazila"],
    "Benapole Border Gateway & Cultural Plaza": ["Benapole", "Sharsha Upazila"],
    "Bhairab Riverfront Park": ["Bhairab River", "Jashore"],
    "Jess Garden Park & Amusement Lake": ["Jashore town"],
    "Keshabpur Forest Enclave & Langur Habitat": ["Keshabpur Upazila", "Hanuman langur"],

    # Jhalokathi
    "Kirtipasha Zamindar Bari": ["Kirtipasha", "Jhalokathi Sadar Upazila"],
    "Sujabad Fort Ruins": ["Nalchity Upazila", "Jhalokathi District"],
    "Gachhbaria Prachin Mandir Complex": ["Jhalokathi District"],
    "Kanu Shahi Mosque": ["Rajapur Upazila", "Jhalokathi"],
    "Gongadhar Temple Heritage Grounds": ["Jhalokathi town"],
    "Kuriana Floating Guava Market": ["Kuriana", "Floating guava market", "Jhalokathi"],
    "Bhimruli Floating Boat Market": ["Bhimruli", "Floating guava market"],
    "Gabkhan Channel & High Level Bridge": ["Gabkhan Channel", "Jhalokathi"],
    "Sugandha Riverfront Esplanade": ["Sugandha River", "Jhalokathi"],
    "Amua River Port & Riverside Promenades": ["Kathalia Upazila", "Jhalokathi District"],

    # Moulvibazar
    "Hajrat Shah Mustafa Mazar Sharif": ["Shah Mustafa", "Moulvibazar"],
    "Prithimpassa Nawab Bari": ["Prithimpashaa Nawab Family", "Kulaura Upazila"],
    "Rajnagar Zamindar Haveli": ["Rajnagar Upazila", "Moulvibazar"],
    "Koilashganj Heritage Tea Bungalows": ["Kamalganj Upazila", "Moulvibazar"],
    "Kamalganj Manipuri Rajbari": ["Kamalganj Upazila", "Manipuri people"],
    "Lawachara National Park": ["Lawachara National Park", "Kamalganj"],
    "Madhabkunda Waterfall": ["Madhabkunda waterfall", "Barlekha Upazila"],
    "Hum Hum Waterfall (Ham Ham)": ["Hum Hum", "Kamalganj Upazila"],
    "Baikka Beel Wetland Bird Sanctuary": ["Baikka Beel", "Sreemangal Upazila"],
    "Hakaluki Haor Expanses": ["Hakaluki Haor", "Moulvibazar District"],

    # Bagerhat
    "Sixty Dome Mosque (Shat Gombuj Masjid)": ["Sixty Dome Mosque", "Bagerhat"],
    "Mausoleum of Khan Jahan Ali": ["Tomb of Khan Jahan Ali", "Bagerhat"],
    "Singar Mosque": ["Singar Mosque", "Bagerhat"],
    "Nine Dome Mosque": ["Nine Dome Mosque", "Bagerhat"],
    "Chunakhola Mosque": ["Chunakhola Mosque", "Bagerhat"],
    "Sundarbans Mangrove Reserve": ["Sundarbans", "Bagerhat District"],
    "Karamjal Wildlife & Crocodile Breeding Sanctuary": ["Karamjal", "Sundarbans"],
    "Kotka Wildlife Sanctuary & Sea Beach": ["Kotka, Bangladesh", "Sundarbans"],
    "Mongla River Port & Sundarbans Gateway": ["Mongla Port", "Mongla"],
    "Ghora Dighi Heritage Lake": ["Sixty Dome Mosque", "Bagerhat"],

    # Bogura
    "Mahasthangarh Citadel & Fortified Ruins": ["Mahasthangarh", "Bogra District"],
    "Gokul Medh (Behula's Lakshindar Basor Ghar)": ["Gokul Medh", "Mahasthangarh"],
    "Vasu Bihar Archaeological Complex": ["Vasu Bihar", "Shibganj Upazila, Bogra"],
    "Kherua Mosque": ["Kherua Mosque", "Sherpur Upazila, Bogra"],
    "Bhavanipur Shaktipeeth Temple": ["Bhabanipur Shaktipeeth", "Sherpur, Bogra"],
    "Govinda Bhita Riverfront Promontory": ["Govinda Bhita", "Mahasthangarh"],
    "Nawab Palace & Bogura Museum Grounds": ["Bogra town", "Bogra District"],
    "Karatoya Riverfront Promenade": ["Karatoya River", "Bogura"],
    "Shariakandi Jamuna Riverfront & Flood Protection Embankment": ["Sariakandi Upazila", "Jamuna River"],
    "Bogura Doi & Traditional Sweet Quarter": ["Bogra curd", "Bogra"],

    # Natore
    "Natore Rajbari (Rani Bhabani Palace)": ["Natore Rajbari", "Rani Bhabani"],
    "Uttara Gonobhaban (Dighapatia Rajbari)": ["Uttara Ganabhaban", "Dighapatia Rajbari"],
    "Chanchkoir Historic Settlement": ["Gurudaspur Upazila", "Natore"],
    "Dayarampur Zamindar Bari": ["Bagatipara Upazila", "Natore"],
    "Rani Bhabani Hawakhana & Water Pavilion": ["Natore Rajbari", "Natore"],
    "Chalan Beel Scenic Wetland": ["Chalan Beel", "Singra Upazila"],
    "Singra Chalan Beel Waterfowl Sanctuary": ["Singra Upazila", "Chalan Beel"],
    "Natore Royal Palace Gardens & Moats": ["Natore Rajbari", "Uttara Ganabhaban"],
    "Haltee Beel Submerged Concrete Expressway": ["Naldanga Upazila", "Chalan Beel"],
    "Kachagolla Sweetmeat Confectionery District": ["Kachagolla", "Natore"],

    # Pirojpur
    "Rayerkathi Zamindar Bari": ["Rayerkathi Zamindar Bari", "Pirojpur Sadar Upazila"],
    "Parerhat Bandar Historic Quarter": ["Zianagar Upazila", "Pirojpur"],
    "Swarupkathi Heritage Lumber Trading Haven": ["Nesarabad Upazila", "Pirojpur"],
    "Sapleza Zamindar Bari Ruins": ["Mathbaria Upazila", "Pirojpur"],
    "Togra Prachin Mosque": ["Indurkani Upazila", "Pirojpur"],
    "Kuriana-Bhimruli Floating Guava Riverways": ["Floating guava market", "Nesarabad Upazila"],
    "Baleshwar Riverfront Esplanade": ["Baleshwar River", "Pirojpur"],
    "Horinghata Mangrove Eco Forest": ["Patharghata", "Baleshwar River"],
    "Sandhya River Estuary & Cruising Corridor": ["Sandhya River", "Pirojpur"],
    "Pirojpur Eco Park & Town Lake": ["Pirojpur town"],

    # Kushtia
    "Lalon Shah Mazar & Shrine Complex": ["Lalon", "Kushtia"],
    "Shilaidaha Rabindra Kuthibari": ["Shilaidaha Rabindra Kuthibari", "Shilaidaha"],
    "Mir Mosharraf Hossain Memorial Center": ["Mir Mosharraf Hossain", "Kumarkhali Upazila"],
    "Jhaudia Shahi Mosque": ["Kushtia Sadar Upazila", "Kushtia"],
    "Mohini Mohan Cotton Mills Heritage Enclave": ["Kushtia town"],
    "Hardinge Bridge & Heritage River Overlook": ["Hardinge Bridge", "Paksey railway bridge"],
    "Lalon Shah Bridge Riverbank": ["Lalon Shah Bridge", "Kushtia"],
    "Gorai River Promenade & Ghats": ["Gorai River", "Kushtia"],
    "Kumarkhali Handloom & Heritage Bazaar": ["Kumarkhali Upazila", "Kushtia"],
    "Rennell's Survey Route Heritage Trail": ["Kushtia District", "Padma River"],

    # Jhenaidah
    "Shailkupa Shahi Jame Mosque": ["Shailkupa Upazila", "Jhenaidah District"],
    "Naldanga Rajbari & Kali Temple Complex": ["Kaliganj Upazila, Jhenaidah", "Naldanga"],
    "Miar Dalan Zamindar Bari": ["Jhenaidah Sadar Upazila", "Jhenaidah"],
    "Barobazar Historic Archaeological Site": ["Barobazar", "Kaliganj Upazila, Jhenaidah"],
    "Pagla Kanai Mazar Sharif": ["Pagla Kanai", "Jhenaidah Sadar Upazila"],
    "Johaura Temple & Sacred Banyan Tree": ["Jhenaidah District", "Banyan tree Bangladesh"],
    "Nabaganga Riverfront & Town Promenade": ["Nabaganda River", "Jhenaidah"],
    "Kotchandpur Wetland Lakes & Baor": ["Kotchandpur Upazila", "Baor Bangladesh"],
    "Dhol Samudra Historic Lake": ["Jhenaidah Sadar Upazila"],
    "Kaliganj Banana & Agricultural Bazaars": ["Kaliganj Upazila, Jhenaidah"],

    # Khulna
    "Shiromoni War Memorial Complex": ["Shiromoni", "Khulna District", "Bangladesh Liberation War"],
    "Dakshin Dihi Rabindranath Tagore In-Laws Ancestral Home": ["Dakshindihi", "Phultala Upazila"],
    "Pithabhog Ancestral Estate": ["Rupsha Upazila", "Khulna"],
    "Ghanoshyam Temple": ["Koyra Upazila", "Khulna"],
    "Khulna Old Port & Steamer Ghat Quarter": ["Khulna", "Rupsha River"],
    "Sundarbans National Park & Mangrove Reserve": ["Sundarbans", "Sundarbans National Park"],
    "Khan Jahan Ali Bridge (Rupsha Bridge)": ["Khan Jahan Ali Bridge", "Khulna"],
    "Katamari & Hiron Point Eco Tourism Sanctuary": ["Hiron Point", "Sundarbans"],
    "Shaheed Hadis Park": ["Shaheed Hadis Park", "Khulna"],
    "Gollamari Memorial & Eco Promenade": ["Gollamari", "Khulna"],

    # Chuadanga
    "Gholdari Shahi Mosque": ["Alamdanga Upazila", "Chuadanga District"],
    "Chuadanga Railway Station": ["Chuadanga railway station", "Chuadanga"],
    "Carew & Co. Historic Sugar Mill & Distillery": ["Carew & Co (Bangladesh) Ltd", "Darsana"],
    "Natuda Historic Freedom Fighters Enclave": ["Damurhuda Upazila", "Chuadanga"],
    "Karpasdanga Mission & Tagore Memorial": ["Damurhuda Upazila", "Rabindranath Tagore"],
    "Mathabhanga Riverfront Promenade": ["Mathabhanga River", "Chuadanga"],
    "Darsana Border Checkpost & Cultural Plaza": ["Darsana", "Gede border"],
    "Alamdanga Historic Baor & Wetlands": ["Alamdanga Upazila", "Chuadanga"],
    "Dharmada Mango Groves & Countryside": ["Damurhuda Upazila", "Chuadanga"],
    "Chuadanga Town Central Park & Lake": ["Chuadanga town"],

    # Meherpur
    "Mujibnagar Memorial Complex & Monument": ["Mujibnagar Memorial", "Mujibnagar"],
    "Amjhupi Neelkuthi (Indigo Factory)": ["Amjhupi Neelkuthi", "Meherpur Sadar Upazila"],
    "Bhatpara Neelkuthi Archaeological Complex": ["Gangni Upazila", "Meherpur"],
    "Siddheswari Kali Mandir": ["Meherpur Sadar Upazila", "Meherpur"],
    "Historic Meherpur Christian Mission": ["Meherpur town"],
    "Bhairab Riverfront Walkway": ["Bhairab River", "Meherpur"],
    "Gangni Countryside Trails & Wetland": ["Gangni Upazila", "Meherpur"],
    "Bamanpara Border Vista & Green Horizons": ["Meherpur District"],
    "Meherpur Shahid Smriti Park": ["Meherpur town"],
    "Historic Mango Orchards & Agro Estates": ["Meherpur District", "Himsagar mango"],

    # Patuakhali
    "Kuakata Buddhist Temple (Misripara Seema Bihar)": ["Kuakata", "Misripara", "Buddhist temple Bangladesh"],
    "Ancient Kuakata Wooden Boat": ["Kuakata boat", "Kuakata"],
    "Gakulnagar Shahi Mosque": ["Patuakhali Sadar Upazila"],
    "Kala Miah Mosque": ["Galachipa Upazila", "Patuakhali"],
    "Bauphal Historic Pottery Quarter": ["Bauphal Upazila", "Patuakhali"],
    "Kuakata Sea Beach & Sunset Panorama": ["Kuakata Beach", "Kuakata"],
    "Lebur Char & Coastal Estuary Sanctuary": ["Lebur Char", "Kuakata"],
    "Fatrar Char Mangrove Forest": ["Fatrar Char", "Sundarbans", "Kuakata"],
    "Gangamati Reserved Forest & Sunrise Point": ["Gangamati", "Kuakata"],
    "Patuakhali Payra River Bridge & Waterfront Boulevard": ["Payra Bridge", "Patuakhali"]
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
        with urllib.request.urlopen(req, timeout=10) as response, open(temp_file, 'wb') as out_file:
            out_file.write(response.read())

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
            img.save(out_path, 'WEBP', quality=85, method=6)

        if os.path.exists(temp_file):
            os.remove(temp_file)
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False

PALETTES = [
    ((6, 95, 70), (4, 47, 34)),      # Deep Emerald to Forest
    ((15, 23, 42), (8, 47, 73)),     # Slate Navy to Ocean
    ((127, 29, 29), (69, 10, 10)),   # Crimson Red to Maroon
    ((19, 78, 74), (4, 47, 46)),     # Deep Teal to Cypress
    ((120, 53, 15), (67, 20, 7)),    # Rich Ochre to Dark Amber
    ((49, 46, 129), (30, 27, 75)),   # Royal Indigo to Night Sky
    ((88, 28, 135), (59, 7, 100)),   # Imperial Violet to Mulberry
    ((30, 41, 59), (15, 23, 42)),    # Midnight Slate
    ((20, 83, 45), (5, 46, 22)),     # Forest Moss
    ((136, 19, 55), (76, 5, 25))     # Rosewood Crimson
]

def generate_artistic_fallback(out_path, title, subtitle, district_name, target_size=(1200, 675), palette_idx=0):
    w, h = target_size
    col_top, col_bot = PALETTES[palette_idx % len(PALETTES)]

    # 1. Base gradient
    base = Image.new('RGB', (w, h), col_top)
    draw = ImageDraw.Draw(base)

    for y in range(h):
        r = int(col_top[0] + (col_bot[0] - col_top[0]) * (y / h))
        g = int(col_top[1] + (col_bot[1] - col_top[1]) * (y / h))
        b = int(col_top[2] + (col_bot[2] - col_top[2]) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # 2. Atmospheric lighting circles
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    accent_r = int((col_top[0] + 80) % 255)
    accent_g = int((col_top[1] + 100) % 255)
    accent_b = int((col_top[2] + 90) % 255)

    ov_draw.ellipse([(-w // 4, -h // 4), (w // 2, h // 2)], fill=(accent_r, accent_g, accent_b, 45))
    ov_draw.ellipse([(w // 2, h // 3), (w + w // 3, h + h // 3)], fill=(255, 255, 255, 20))
    ov_draw.ellipse([(w // 4, h // 4), (3 * w // 4, 3 * h // 4)], outline=(255, 255, 255, 18), width=3)
    ov_draw.ellipse([(w // 4 - 40, h // 4 - 40), (3 * w // 4 + 40, 3 * h // 4 + 40)], outline=(255, 255, 255, 10), width=1)

    # Darker vignette bar at the bottom for text legibility
    for y in range(int(h * 0.45), h):
        alpha = int(220 * ((y - h * 0.45) / (h * 0.55)))
        ov_draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))

    base = Image.alpha_composite(base.convert('RGBA'), overlay).convert('RGB')
    final_draw = ImageDraw.Draw(base)

    # 3. Typography
    try:
        font_dist = ImageFont.truetype("arialbd.ttf", 24)
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 26)
    except Exception:
        font_dist = font_title = font_sub = ImageFont.load_default()

    margin_x = 70
    bot_y = h - 85

    # Subtitle
    final_draw.text((margin_x, bot_y), subtitle[:75], fill=(226, 232, 240), font=font_sub)
    # Title
    title_y = bot_y - 65
    final_draw.text((margin_x, title_y), title[:50], fill=(255, 255, 255), font=font_title)
    
    # District badge tag
    badge_y = title_y - 45
    badge_text = f"EZZE MAP  •  {district_name.upper()} HERITAGE"
    badge_w = len(badge_text) * 11 + 20
    final_draw.rectangle([margin_x, badge_y - 4, margin_x + badge_w, badge_y + 24], fill=(255, 255, 255, 30), outline=(255, 255, 255, 120))
    final_draw.text((margin_x + 10, badge_y), badge_text, fill=(248, 250, 252), font=font_dist)

    base.save(out_path, 'WEBP', quality=85, method=6)
    return True

import concurrent.futures

def process_single_image(task):
    out_path, queries, fallback_title, fallback_sub, dist_en, palette_idx = task
    if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
        return ("SKIPPED", out_path)

    found_url = search_wikimedia_image(queries)
    if found_url and download_and_crop(found_url, out_path):
        return ("DOWNLOADED", out_path)
    else:
        generate_artistic_fallback(out_path, fallback_title, fallback_sub, dist_en, palette_idx=palette_idx)
        return ("FALLBACK", out_path)

def process_all_20():
    with open('scripts/curated_all_47.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    tasks = []
    for d_idx, slug in enumerate(TARGET_SLUGS):
        dist = catalog.get(slug)
        if not dist:
            continue
        dist_en = dist['en']
        out_dir = os.path.join('images', 'districts', slug)
        os.makedirs(out_dir, exist_ok=True)

        # 1. Hero
        hero_path = os.path.join(out_dir, "hero.webp")
        hero_queries = [f"{dist_en} district Bangladesh", f"{dist_en} Bangladesh", f"{dist_en} town"]
        if dist['hist']:
            hero_queries.insert(0, dist['hist'][0]['nameEn'])
        tasks.append((hero_path, hero_queries, dist.get('hero_title_en', f"{dist_en} Historic Landscapes"), dist.get('hero_sub_en', f"Explore {dist_en}"), dist_en, d_idx))

        # 2. Carousel
        for c_idx, slide in enumerate(dist['carousel']):
            c_path = os.path.join(out_dir, f"carousel-{c_idx + 1}.webp")
            c_queries = [slide['titleEn'], f"{dist_en} {slide['titleEn']}", f"{dist_en} Bangladesh"]
            tasks.append((c_path, c_queries, slide['titleEn'], slide['subtitleEn'], dist_en, d_idx + c_idx + 1))

        # 3. Hist
        for h_idx, spot in enumerate(dist['hist']):
            h_path = os.path.join(out_dir, f"hist-{h_idx + 1}.webp")
            name = spot['nameEn']
            sub = spot['categoryEn']
            queries = CUSTOM_SEARCH_KEYS.get(name, [name, f"{name} {dist_en}", f"{name} Bangladesh"])
            tasks.append((h_path, queries, name, sub, dist_en, d_idx + h_idx + 3))

        # 4. Tour
        for t_idx, spot in enumerate(dist['tour']):
            t_path = os.path.join(out_dir, f"tour-{t_idx + 1}.webp")
            name = spot['nameEn']
            sub = spot['categoryEn']
            queries = CUSTOM_SEARCH_KEYS.get(name, [name, f"{name} {dist_en}", f"{name} Bangladesh"])
            tasks.append((t_path, queries, name, sub, dist_en, d_idx + t_idx + 5))

    print(f"Total images in queue: {len(tasks)}. Processing with 8 threads...")

    downloaded = 0
    fallbacks = 0
    skipped = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_single_image, t): t for t in tasks}
        for future in concurrent.futures.as_completed(futures):
            status, path = future.result()
            if status == "DOWNLOADED":
                downloaded += 1
            elif status == "FALLBACK":
                fallbacks += 1
            elif status == "SKIPPED":
                skipped += 1
            
            total_done = downloaded + fallbacks + skipped
            if total_done % 10 == 0 or total_done == len(tasks):
                print(f"Progress: [{total_done}/{len(tasks)}] (Downloaded: {downloaded}, Artistic: {fallbacks}, Skipped: {skipped})")

    print("\n=======================================================")
    print(f"TOTAL IMAGES: {len(tasks)}")
    print(f"Downloaded: {downloaded}, Artistic Fallbacks: {fallbacks}, Skipped existing: {skipped}")
    print("ALL 320 IMAGES COMPLETE!")

if __name__ == '__main__':
    process_all_20()
