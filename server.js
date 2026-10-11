/**
 * Local Host — Native Zero-Dependency Streaming Assets Server
 * Built with native Node.js HTTP & Stream engines for ultra-performance local-first delivery.
 */
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.PORT || 3000;
const ROOT_DIR = __dirname;

// Exhaustive MIME type dictionary
const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.js': 'application/javascript; charset=UTF-8',
  '.mjs': 'application/javascript; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.json': 'application/json; charset=UTF-8',
  '.webp': 'image/webp',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml; charset=UTF-8',
  '.ico': 'image/x-icon',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf',
  '.otf': 'font/otf',
  '.txt': 'text/plain; charset=UTF-8'
};

const server = http.createServer((req, res) => {
  // CORS & Security Headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');
  res.setHeader('X-Content-Type-Options', 'nosniff');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    res.end();
    return;
  }

  // Parse safe relative pathname
  let safeUrl = req.url.split('?')[0].split('#')[0];
  try {
    safeUrl = decodeURIComponent(safeUrl);
  } catch (e) {
    res.writeHead(400, { 'Content-Type': 'text/plain' });
    res.end('400 Bad Request');
    return;
  }

  if (safeUrl === '/' || safeUrl === '') {
    safeUrl = '/index.html';
  }

  // Normalize path and prevent directory traversal
  const normalizedPath = path.normalize(safeUrl).replace(/^(\.\.[\/\\])+/, '');
  const filePath = path.join(ROOT_DIR, normalizedPath);

  // Verify file within ROOT_DIR
  if (!filePath.startsWith(ROOT_DIR)) {
    res.writeHead(403, { 'Content-Type': 'text/plain' });
    res.end('403 Forbidden');
    return;
  }

  fs.stat(filePath, (err, stats) => {
    if (err) {
      if (err.code === 'ENOENT') {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
      } else {
        res.writeHead(500, { 'Content-Type': 'text/plain' });
        res.end(`500 Internal Error: ${err.code}`);
      }
      return;
    }

    if (stats.isDirectory()) {
      const indexFile = path.join(filePath, 'index.html');
      fs.stat(indexFile, (indexErr, indexStats) => {
        if (!indexErr && indexStats.isFile()) {
          streamFile(indexFile, indexStats, req, res);
        } else {
          res.writeHead(403, { 'Content-Type': 'text/plain' });
          res.end('403 Directory Listing Denied');
        }
      });
      return;
    }

    streamFile(filePath, stats, req, res);
  });
});

function streamFile(filePath, stats, req, res) {
  const ext = path.extname(filePath).toLowerCase();
  const contentType = MIME_TYPES[ext] || 'application/octet-stream';
  
  // Set cache headers — Fast revalidation for local dev
  res.setHeader('Content-Type', contentType);
  res.setHeader('Content-Length', stats.size);
  res.setHeader('Accept-Ranges', 'bytes');
  res.setHeader('Cache-Control', 'no-cache, must-revalidate');

  if (req.method === 'HEAD') {
    res.writeHead(200);
    res.end();
    return;
  }

  const readStream = fs.createReadStream(filePath);
  readStream.on('error', (streamErr) => {
    if (!res.headersSent) {
      res.writeHead(500, { 'Content-Type': 'text/plain' });
      res.end('Stream Error');
    }
  });

  readStream.pipe(res);
}

server.listen(PORT, () => {
  console.log(`[Local Host Streaming Engine] Server active at http://localhost:${PORT}`);
});
