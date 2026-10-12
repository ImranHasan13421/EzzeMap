const { LOCAL_DISTRICTS } = require('../data/main-info/catalog.js');
const fs = require('fs');
const path = require('path');

const TARGET_SLUGS = [
  'narayanganj', 'feni', 'cumilla', 'bhola',
  'barishal', 'chattogram', 'sylhet', 'noakhali',
  'rajshahi', 'coxs-bazar', 'kurigram', 'dinajpur',
  'munshiganj', 'gazipur', 'narsingdi', 'manikganj',
  'shariatpur', 'madaripur', 'tangail', 'brahmanbaria',
  'rajbari', 'chandpur', 'mymensingh', 'kishoreganj',
  'sirajganj', 'faridpur', 'jamalpur'
];

let allOk = true;

TARGET_SLUGS.forEach(slug => {
  const d = LOCAL_DISTRICTS.find(x => x.slug === slug || (slug === 'coxs-bazar' && x.slug === 'cox-s-bazar'));
  if (!d) {
    console.error(`ERROR: Missing district ${slug} in catalog!`);
    allOk = false;
    return;
  }

  // Check hero image
  if (!d.heroImage || !fs.existsSync(path.join(__dirname, '..', d.heroImage))) {
    console.error(`ERROR: Missing hero image for ${slug}: ${d.heroImage}`);
    allOk = false;
  }

  // Check carousel (5 items)
  if (!Array.isArray(d.carousel) || d.carousel.length !== 5) {
    console.error(`ERROR: ${slug} carousel count is ${d.carousel ? d.carousel.length : 0}`);
    allOk = false;
  } else {
    d.carousel.forEach(c => {
      if (!fs.existsSync(path.join(__dirname, '..', c.image))) {
        console.error(`ERROR: Missing carousel image for ${slug}: ${c.image}`);
        allOk = false;
      }
    });
  }

  // Check hist (5 items)
  if (!Array.isArray(d.hist) || d.hist.length !== 5) {
    console.error(`ERROR: ${slug} hist count is ${d.hist ? d.hist.length : 0}`);
    allOk = false;
  } else {
    d.hist.forEach(h => {
      if (!fs.existsSync(path.join(__dirname, '..', h.image))) {
        console.error(`ERROR: Missing hist image for ${slug}: ${h.image}`);
        allOk = false;
      }
      if (!h.mapUrl || !h.mapUrl.includes('google.com/maps')) {
        console.error(`ERROR: Invalid mapUrl in ${slug} hist: ${h.nameEn}`);
        allOk = false;
      }
      if (!h.descEn || h.descEn.length < 150) {
        console.error(`ERROR: Description too short for ${slug} hist: ${h.nameEn}`);
        allOk = false;
      }
      if (!h.descBn || h.descBn.length < 100) {
        console.error(`ERROR: Bengali description too short for ${slug} hist: ${h.nameBn}`);
        allOk = false;
      }
    });
  }

  // Check tour (5 items)
  if (!Array.isArray(d.tour) || d.tour.length !== 5) {
    console.error(`ERROR: ${slug} tour count is ${d.tour ? d.tour.length : 0}`);
    allOk = false;
  } else {
    d.tour.forEach(t => {
      if (!fs.existsSync(path.join(__dirname, '..', t.image))) {
        console.error(`ERROR: Missing tour image for ${slug}: ${t.image}`);
        allOk = false;
      }
      if (!t.mapUrl || !t.mapUrl.includes('google.com/maps')) {
        console.error(`ERROR: Invalid mapUrl in ${slug} tour: ${t.nameEn}`);
        allOk = false;
      }
      if (!t.descEn || t.descEn.length < 150) {
        console.error(`ERROR: Description too short for ${slug} tour: ${t.nameEn}`);
        allOk = false;
      }
      if (!t.descBn || t.descBn.length < 100) {
        console.error(`ERROR: Bengali description too short for ${slug} tour: ${t.nameBn}`);
        allOk = false;
      }
    });
  }

  console.log(`PASS: ${d.en} (${d.bn}) -> Hero OK, 5 Carousel OK, 5 Hist OK, 5 Tour OK`);
});

if (allOk) {
  console.log('\nALL 12 DISTRICTS PERFECTLY VERIFIED AND INTEGRATED!');
}
