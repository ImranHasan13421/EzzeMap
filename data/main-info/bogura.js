/**
 * District Data Schema — Bogura (বগুড়া)
 * Offline-first static metadata
 */
const BOGURA_DATA = {
  "id": 45,
  "slug": "bogura",
  "en": "Bogura",
  "bn": "বগুড়া",
  "div": "Rajshahi",
  "lat": 24.8245,
  "lng": 89.3788,
  "coordinates": "24.8245, 89.3788",
  "est": 1821,
  "area": "2,898.68 km²",
  "pop": "3.7M",
  "dist": "200 km",
  "route": "Via Jamuna Bridge and Dhaka-Bogura 4-lane Highway N5 (approx. 4.5 hours by bus/train).",
  "tagline": "Bogura (বগুড়া) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
  "heroImage": "images/districts/bogura/hero.webp",
  "carousel": [
    {
      "id": 1,
      "image": "images/districts/bogura/carousel-1.webp",
      "title": "Bogura Heritage & Landscapes",
      "subtitle": "Panoramic beauty across Rajshahi Division"
    },
    {
      "id": 2,
      "image": "images/districts/bogura/carousel-2.webp",
      "title": "Historic Monuments of Bogura",
      "subtitle": "Ancient landmarks dating back across generations"
    },
    {
      "id": 3,
      "image": "images/districts/bogura/carousel-3.webp",
      "title": "Riverine Corridors & Nature",
      "subtitle": "Verdant waters and lush environmental biodiversity"
    },
    {
      "id": 4,
      "image": "images/districts/bogura/carousel-4.webp",
      "title": "Cultural Life & Traditions",
      "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
    },
    {
      "id": 5,
      "image": "images/districts/bogura/carousel-5.webp",
      "title": "Scenic Trails & Landmarks",
      "subtitle": "Famous travel destinations and peaceful viewpoints"
    }
  ],
  "hist": [
    {
      "id": 1,
      "image": "images/districts/bogura/hist-1.webp",
      "name": "Mahasthangarh (Ancient Pundranagara)",
      "nameBn": "Mahasthangarh (Ancient Pundranagara) (বগুড়া)",
      "category": "Royal Heritage",
      "desc": "Oldest fortified urban archaeological city in Bangladesh, dating from 3rd century BCE.",
      "location": "Bogura Sadar, Rajshahi"
    },
    {
      "id": 2,
      "image": "images/districts/bogura/hist-2.webp",
      "name": "Gokul Medh (Behula’s Basor Ghar)",
      "nameBn": "Gokul Medh (Behula’s Basor Ghar) (বগুড়া)",
      "category": "Historic Mosque",
      "desc": "Terraced stupa structure linked to the legendary folklore of Behula and Lakhindar.",
      "location": "Old Town, Bogura"
    },
    {
      "id": 3,
      "image": "images/districts/bogura/hist-3.webp",
      "name": "Bogura Colonial Court & Mint",
      "nameBn": "বগুড়া ঔপনিবেশিক আদালত ও টাকশাল",
      "category": "Colonial Architecture",
      "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Court Road, Bogura"
    },
    {
      "id": 4,
      "image": "images/districts/bogura/hist-4.webp",
      "name": "Bogura Archeological Mound",
      "nameBn": "বগুড়া প্রত্নতাত্ত্বিক ঢিবি",
      "category": "Ancient Archaeology",
      "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Archaeological Site, Bogura"
    },
    {
      "id": 5,
      "image": "images/districts/bogura/hist-5.webp",
      "name": "Bogura Liberation War Memorial",
      "nameBn": "বগুড়া মুক্তিযুদ্ধ স্মৃতিসৌধ",
      "category": "National Memorial",
      "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Central Park, Bogura"
    }
  ],
  "tour": [
    {
      "id": 1,
      "image": "images/districts/bogura/tour-1.webp",
      "name": "Vasu Vihara & Museum",
      "nameBn": "Vasu Vihara & Museum (বগুড়া)",
      "category": "Archaeology",
      "desc": "Exquisite excavated Buddhist monastery complex and collection of ancient terracotta plaques.",
      "location": "Bogura Riverfront, Rajshahi"
    },
    {
      "id": 2,
      "image": "images/districts/bogura/tour-2.webp",
      "name": "Bogura Sweet Culture",
      "nameBn": "Bogura Sweet Culture (বগুড়া)",
      "category": "Culinary Landmark",
      "desc": "World-famous destination for rich traditional Bogura Curd (Doi) served in clay pots.",
      "location": "Forest Range, Bogura"
    },
    {
      "id": 3,
      "image": "images/districts/bogura/tour-3.webp",
      "name": "Bogura Cultural Heritage Museum",
      "nameBn": "বগুড়া লোকশিল্প ও ঐতিহ্য জাদুঘর",
      "category": "Cultural Center",
      "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Town Center, Bogura"
    },
    {
      "id": 4,
      "image": "images/districts/bogura/tour-4.webp",
      "name": "Bogura Scenic Lake & Boating Resort",
      "nameBn": "বগুড়া মনোরম হ্রদ ও রিসোর্ট",
      "category": "Lakeside Resort",
      "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Lake View, Bogura"
    },
    {
      "id": 5,
      "image": "images/districts/bogura/tour-5.webp",
      "name": "Bogura Sunset Hilltop Viewpoint",
      "nameBn": "বগুড়া সূর্যাস্ত ভিউপয়েন্ট",
      "category": "Panoramic Vista",
      "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Hill Ridge, Bogura"
    }
  ]
};

if (typeof window !== 'undefined') {
  if (!window.LOCAL_DISTRICTS) window.LOCAL_DISTRICTS = [];
  const idx = window.LOCAL_DISTRICTS.findIndex(item => item.id === BOGURA_DATA.id || item.slug === BOGURA_DATA.slug);
  if (idx >= 0) {
    window.LOCAL_DISTRICTS[idx] = Object.assign({}, window.LOCAL_DISTRICTS[idx], BOGURA_DATA);
  } else {
    window.LOCAL_DISTRICTS.push(BOGURA_DATA);
  }
  if (!window.DISTRICT_MODULES) window.DISTRICT_MODULES = {};
  window.DISTRICT_MODULES['bogura'] = BOGURA_DATA;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BOGURA_DATA };
}
