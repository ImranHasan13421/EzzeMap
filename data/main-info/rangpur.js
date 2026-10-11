/**
 * District Data Schema — Rangpur (রংপুর)
 * Offline-first static metadata
 */
const RANGPUR_DATA = {
  "id": 59,
  "slug": "rangpur",
  "en": "Rangpur",
  "bn": "রংপুর",
  "div": "Rangpur",
  "lat": 25.6497,
  "lng": 89.2368,
  "coordinates": "25.6497, 89.2368",
  "est": 1772,
  "area": "2,370.45 km²",
  "pop": "3.1M",
  "dist": "300 km",
  "route": "Via Jamuna Bridge 4-lane Highway N5 (approx. 6 hrs), Rangpur Express train, or 45-min flight to Saidpur.",
  "tagline": "Rangpur (রংপুর) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
  "heroImage": "images/districts/rangpur/hero.webp",
  "carousel": [
    {
      "id": 1,
      "image": "images/districts/rangpur/carousel-1.webp",
      "title": "Rangpur Heritage & Landscapes",
      "subtitle": "Panoramic beauty across Rangpur Division"
    },
    {
      "id": 2,
      "image": "images/districts/rangpur/carousel-2.webp",
      "title": "Historic Monuments of Rangpur",
      "subtitle": "Ancient landmarks dating back across generations"
    },
    {
      "id": 3,
      "image": "images/districts/rangpur/carousel-3.webp",
      "title": "Riverine Corridors & Nature",
      "subtitle": "Verdant waters and lush environmental biodiversity"
    },
    {
      "id": 4,
      "image": "images/districts/rangpur/carousel-4.webp",
      "title": "Cultural Life & Traditions",
      "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
    },
    {
      "id": 5,
      "image": "images/districts/rangpur/carousel-5.webp",
      "title": "Scenic Trails & Landmarks",
      "subtitle": "Famous travel destinations and peaceful viewpoints"
    }
  ],
  "hist": [
    {
      "id": 1,
      "image": "images/districts/rangpur/hist-1.webp",
      "name": "Tajhat Palace",
      "nameBn": "Tajhat Palace (রংপুর)",
      "category": "Royal Heritage",
      "desc": "Spectacular early 20th-century neoclassical royal palace now housing a magnificent antiquities museum.",
      "location": "Rangpur Sadar, Rangpur"
    },
    {
      "id": 2,
      "image": "images/districts/rangpur/hist-2.webp",
      "name": "Carmichael College Historic Campus",
      "nameBn": "Carmichael College Historic Campus (রংপুর)",
      "category": "Historic Mosque",
      "desc": "Architectural landmark built in 1916 blending Indo-Saracenic and colonial architecture.",
      "location": "Old Town, Rangpur"
    },
    {
      "id": 3,
      "image": "images/districts/rangpur/hist-3.webp",
      "name": "Rangpur Colonial Court & Mint",
      "nameBn": "রংপুর ঔপনিবেশিক আদালত ও টাকশাল",
      "category": "Colonial Architecture",
      "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Court Road, Rangpur"
    },
    {
      "id": 4,
      "image": "images/districts/rangpur/hist-4.webp",
      "name": "Rangpur Archeological Mound",
      "nameBn": "রংপুর প্রত্নতাত্ত্বিক ঢিবি",
      "category": "Ancient Archaeology",
      "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Archaeological Site, Rangpur"
    },
    {
      "id": 5,
      "image": "images/districts/rangpur/hist-5.webp",
      "name": "Rangpur Liberation War Memorial",
      "nameBn": "রংপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
      "category": "National Memorial",
      "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Central Park, Rangpur"
    }
  ],
  "tour": [
    {
      "id": 1,
      "image": "images/districts/rangpur/tour-1.webp",
      "name": "Chikli Beel Water Leisure",
      "nameBn": "Chikli Beel Water Leisure (রংপুর)",
      "category": "Urban Water Park",
      "desc": "Vibrant city lake featuring speedboats, floating walkways, and illuminated gardens.",
      "location": "Rangpur Riverfront, Rangpur"
    },
    {
      "id": 2,
      "image": "images/districts/rangpur/tour-2.webp",
      "name": "Vinnya Jagat Eco Amusement Park",
      "nameBn": "Vinnya Jagat Eco Amusement Park (রংপুর)",
      "category": "Family Theme Park",
      "desc": "Expansive countryside amusement and eco resort with landscaped gardens and rides.",
      "location": "Forest Range, Rangpur"
    },
    {
      "id": 3,
      "image": "images/districts/rangpur/tour-3.webp",
      "name": "Rangpur Cultural Heritage Museum",
      "nameBn": "রংপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
      "category": "Cultural Center",
      "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Town Center, Rangpur"
    },
    {
      "id": 4,
      "image": "images/districts/rangpur/tour-4.webp",
      "name": "Rangpur Scenic Lake & Boating Resort",
      "nameBn": "রংপুর মনোরম হ্রদ ও রিসোর্ট",
      "category": "Lakeside Resort",
      "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Lake View, Rangpur"
    },
    {
      "id": 5,
      "image": "images/districts/rangpur/tour-5.webp",
      "name": "Rangpur Sunset Hilltop Viewpoint",
      "nameBn": "রংপুর সূর্যাস্ত ভিউপয়েন্ট",
      "category": "Panoramic Vista",
      "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Hill Ridge, Rangpur"
    }
  ]
};

if (typeof window !== 'undefined') {
  if (!window.LOCAL_DISTRICTS) window.LOCAL_DISTRICTS = [];
  const idx = window.LOCAL_DISTRICTS.findIndex(item => item.id === RANGPUR_DATA.id || item.slug === RANGPUR_DATA.slug);
  if (idx >= 0) {
    window.LOCAL_DISTRICTS[idx] = Object.assign({}, window.LOCAL_DISTRICTS[idx], RANGPUR_DATA);
  } else {
    window.LOCAL_DISTRICTS.push(RANGPUR_DATA);
  }
  if (!window.DISTRICT_MODULES) window.DISTRICT_MODULES = {};
  window.DISTRICT_MODULES['rangpur'] = RANGPUR_DATA;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { RANGPUR_DATA };
}
