/**
 * Verify every internal href/src/srcset in the built site resolves to a
 * file (and, for "#fragment" links, an existing id).
 *
 * Run after `npm run build`. Uses only Node built-ins.
 */
import { existsSync, readFileSync, readdirSync, statSync } from "node:fs";
import { dirname, extname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const publicDir = join(root, "public");
const basePath = "/lab_xiao/";

if (!existsSync(publicDir)) {
  console.error("public/ not found — run `npm run build` first.");
  process.exit(1);
}

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (name.endsWith(".html")) out.push(p);
  }
  return out;
}

function attrValues(html, attr) {
  const re = new RegExp(`${attr}=(?:"([^"]*)"|'([^']*)'|([^\\s>]+))`, "gi");
  const out = [];
  let m;
  while ((m = re.exec(html))) out.push(m[1] ?? m[2] ?? m[3]);
  return out;
}

function idsOf(html) {
  const out = new Set();
  const re = /\bid=(?:"([^"]*)"|'([^']*)'|([^\s>]+))/gi;
  let m;
  while ((m = re.exec(html))) out.add(m[1] ?? m[2] ?? m[3]);
  return out;
}

const pages = new Map();
for (const file of walk(publicDir)) {
  const html = readFileSync(file, "utf8");
  const links = [...attrValues(html, "href"), ...attrValues(html, "src")];
  for (const srcset of attrValues(html, "srcset")) {
    for (const part of srcset.split(",")) {
      const url = part.trim().split(/\s+/)[0];
      if (url) links.push(url);
    }
  }
  pages.set(file, { links, ids: idsOf(html) });
}

function localTarget(pageFile, url) {
  if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(url)) return null;
  const hashIndex = url.indexOf("#");
  const fragment = hashIndex >= 0 ? decodeURIComponent(url.slice(hashIndex + 1)) : "";
  let path = (hashIndex >= 0 ? url.slice(0, hashIndex) : url).split("?")[0];
  if (!path) return { fragment };
  path = decodeURI(path);
  if (path.startsWith(basePath)) path = "/" + path.slice(basePath.length);
  if (!path.startsWith("/")) {
    const pageDir = relative(publicDir, dirname(pageFile)).replace(/\\/g, "/");
    path = resolve("/" + pageDir, path).replace(/\\/g, "/");
  }
  let target = join(publicDir, path.replace(/^\//, ""));
  if (path.endsWith("/") || !extname(target)) target = join(target, "index.html");
  return { target, fragment };
}

const broken = [];
for (const [page, { links, ids }] of pages) {
  for (const url of links) {
    if (url.startsWith("#")) {
      if (url.length > 1 && !ids.has(decodeURIComponent(url.slice(1)))) {
        broken.push([relative(publicDir, page), url, "anchor"]);
      }
      continue;
    }
    const target = localTarget(page, url);
    if (!target) continue;
    if (target.target && !existsSync(target.target)) {
      broken.push([relative(publicDir, page), url, "file"]);
    } else if (target.fragment && target.target) {
      const dest = pages.get(target.target);
      if (dest && !dest.ids.has(target.fragment)) {
        broken.push([relative(publicDir, page), url, "anchor"]);
      }
    }
  }
}

if (broken.length) {
  console.error(`broken internal links: ${broken.length}`);
  for (const [page, url, kind] of broken.slice(0, 50)) {
    console.error(`  ${kind}: ${url} (in ${page})`);
  }
  process.exit(1);
}
console.log(`internal links OK (${pages.size} pages)`);