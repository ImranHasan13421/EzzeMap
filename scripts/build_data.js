const fs = require('fs');
const path = require('path');
const { DISTRICTS_DATA, BANGLADESH_MAP_VIEWBOX } = require('../district-data.js');

// 1. Generate data/map-paths.js
const mapPaths = {};
DISTRICTS_DATA.forEach(d => {
  mapPaths[d.id] = d.svgPath;
  mapPaths[d.slug] = d.svgPath;
});

const mapPathsContent = `/**
 * Bangladesh 64 Districts SVG Vector Paths
 * Houses the core heavy SVG path polygon vector arrays
 */
const MAP_PATHS = ${JSON.stringify(mapPaths, null, 2)};

if (typeof window !== 'undefined') {
  window.MAP_PATHS = MAP_PATHS;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { MAP_PATHS };
}
`;

fs.writeFileSync(path.join(__dirname, '../data/map-paths.js'), mapPathsContent, 'utf8');
console.log('Generated data/map-paths.js');
