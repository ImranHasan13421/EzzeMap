/**
 * District Data Schema — Feni (ফেনী)
 * Offline-first static metadata
 */
const FENI_DATA = {
  "id": 20,
  "slug": "feni",
  "en": "Feni",
  "bn": "ফেনী",
  "div": "Chattogram",
  "lat": 23.0032,
  "lng": 91.4127,
  "coordinates": "23.0032, 91.4127",
  "est": 1984,
  "area": "928.34 km²",
  "pop": "1.5M",
  "dist": "150 km",
  "route": "Via Dhaka-Chittagong Highway N1 (approx. 2.5 - 3 hours by express bus or intercity train).",
  "tagline": "Feni (ফেনী) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
  "heroImage": "images/districts/feni/hero.webp",
  "carousel": [
    {
      "id": 1,
      "image": "images/districts/feni/carousel-1.webp",
      "title": "Feni Heritage & Landscapes",
      "subtitle": "Panoramic beauty across Chattogram Division"
    },
    {
      "id": 2,
      "image": "images/districts/feni/carousel-2.webp",
      "title": "Historic Monuments of Feni",
      "subtitle": "Ancient landmarks dating back across generations"
    },
    {
      "id": 3,
      "image": "images/districts/feni/carousel-3.webp",
      "title": "Riverine Corridors & Nature",
      "subtitle": "Verdant waters and lush environmental biodiversity"
    },
    {
      "id": 4,
      "image": "images/districts/feni/carousel-4.webp",
      "title": "Cultural Life & Traditions",
      "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
    },
    {
      "id": 5,
      "image": "images/districts/feni/carousel-5.webp",
      "title": "Scenic Trails & Landmarks",
      "subtitle": "Famous travel destinations and peaceful viewpoints"
    }
  ],
  "hist": [
    {
      "id": 1,
      "image": "images/districts/feni/hist-1.webp",
      "name": "Bijoy Singh Dighi",
      "nameBn": "Bijoy Singh Dighi (ফেনী)",
      "category": "Royal Heritage",
      "desc": "Massive historic water tank dating back to the Sena dynasty surrounded by grand shade trees.",
      "location": "Feni Sadar, Chattogram"
    },
    {
      "id": 2,
      "image": "images/districts/feni/hist-2.webp",
      "name": "Shamsher Gazi Fort",
      "nameBn": "Shamsher Gazi Fort (ফেনী)",
      "category": "Historic Mosque",
      "desc": "Remnants of the 18th-century rebel ruler Shamsher Gazi who fought colonial expansion.",
      "location": "Old Town, Feni"
    },
    {
      "id": 3,
      "image": "images/districts/feni/hist-3.webp",
      "name": "Feni Colonial Court & Mint",
      "nameBn": "ফেনী ঔপনিবেশিক আদালত ও টাকশাল",
      "category": "Colonial Architecture",
      "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Court Road, Feni"
    },
    {
      "id": 4,
      "image": "images/districts/feni/hist-4.webp",
      "name": "Feni Archeological Mound",
      "nameBn": "ফেনী প্রত্নতাত্ত্বিক ঢিবি",
      "category": "Ancient Archaeology",
      "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Archaeological Site, Feni"
    },
    {
      "id": 5,
      "image": "images/districts/feni/hist-5.webp",
      "name": "Feni Liberation War Memorial",
      "nameBn": "ফেনী মুক্তিযুদ্ধ স্মৃতিসৌধ",
      "category": "National Memorial",
      "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Central Park, Feni"
    }
  ],
  "tour": [
    {
      "id": 1,
      "image": "images/districts/feni/tour-1.webp",
      "name": "Muhuri Irrigation Project & Dam",
      "nameBn": "Muhuri Irrigation Project & Dam (ফেনী)",
      "category": "Eco-Tourism",
      "desc": "Second-largest water control project in Bangladesh with mangrove trees and winter waterbirds.",
      "location": "Feni Riverfront, Chattogram"
    },
    {
      "id": 2,
      "image": "images/districts/feni/tour-2.webp",
      "name": "Chandgazi Mosque",
      "nameBn": "Chandgazi Mosque (ফেনী)",
      "category": "Mughal Architecture",
      "desc": "Chandgazi Mosque stands as an iconic tourist highlight in Feni district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
      "location": "Forest Range, Feni"
    },
    {
      "id": 3,
      "image": "images/districts/feni/tour-3.webp",
      "name": "Feni Cultural Heritage Museum",
      "nameBn": "ফেনী লোকশিল্প ও ঐতিহ্য জাদুঘর",
      "category": "Cultural Center",
      "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Town Center, Feni"
    },
    {
      "id": 4,
      "image": "images/districts/feni/tour-4.webp",
      "name": "Feni Scenic Lake & Boating Resort",
      "nameBn": "ফেনী মনোরম হ্রদ ও রিসোর্ট",
      "category": "Lakeside Resort",
      "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Lake View, Feni"
    },
    {
      "id": 5,
      "image": "images/districts/feni/tour-5.webp",
      "name": "Feni Sunset Hilltop Viewpoint",
      "nameBn": "ফেনী সূর্যাস্ত ভিউপয়েন্ট",
      "category": "Panoramic Vista",
      "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Hill Ridge, Feni"
    }
  ]
};

if (typeof window !== 'undefined') {
  if (!window.LOCAL_DISTRICTS) window.LOCAL_DISTRICTS = [];
  const idx = window.LOCAL_DISTRICTS.findIndex(item => item.id === FENI_DATA.id || item.slug === FENI_DATA.slug);
  if (idx >= 0) {
    window.LOCAL_DISTRICTS[idx] = Object.assign({}, window.LOCAL_DISTRICTS[idx], FENI_DATA);
  } else {
    window.LOCAL_DISTRICTS.push(FENI_DATA);
  }
  if (!window.DISTRICT_MODULES) window.DISTRICT_MODULES = {};
  window.DISTRICT_MODULES['feni'] = FENI_DATA;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { FENI_DATA };
}
