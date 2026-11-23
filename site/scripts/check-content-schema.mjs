/**
 * Lightweight front-matter contract for lab content entities.
 */
import { readdirSync, readFileSync, statSync, existsSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const content = join(root, "content");
const errors = [];

function walkMd(dir, out = []) {
  if (!existsSync(dir)) return out;
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walkMd(p, out);
    else if (/\.(md|html)$/i.test(name) && !name.startsWith("_")) out.push(p);
    else if (name === "index.md" || name === "index.en.md") out.push(p);
  }
  return out;
}

function frontMatter(src) {
  if (!src.startsWith("---")) return null;
  const end = src.indexOf("\n---", 3);
  if (end < 0) return null;
  return src.slice(3, end);
}

function hasKey(fm, key) {
  return new RegExp(`^${key}\\s*:`, "m").test(fm);
}

// Authors (people)
for (const dir of readdirSync(join(content, "authors"))) {
  const p = join(content, "authors", dir, "_index.md");
  if (!existsSync(p) || dir === ".git") continue;
  if (dir === "admin") continue;
  const fm = frontMatter(readFileSync(p, "utf8"));
  if (!fm) {
    errors.push(`authors/${dir}: missing front matter`);
    continue;
  }
  for (const k of ["title", "user_groups", "weight"]) {
    if (!hasKey(fm, k)) errors.push(`authors/${dir}: missing ${k}`);
  }
}

// Publications
function checkSection(section, required) {
  const base = join(content, section);
  if (!existsSync(base)) return;
  for (const dir of readdirSync(base)) {
    const p = join(base, dir, "index.md");
    if (!existsSync(p)) continue;
    const fm = frontMatter(readFileSync(p, "utf8"));
    if (!fm) {
      errors.push(`${section}/${dir}: missing front matter`);
      continue;
    }
    for (const k of required) {
      if (!hasKey(fm, k)) errors.push(`${section}/${dir}: missing ${k}`);
    }
  }
}

checkSection("publications", ["title", "authors", "date"]);
checkSection("projects", ["title"]);
checkSection("patent", ["title"]);
checkSection("award", ["title"]);

// Dual-authority guard: outcomes hubs must not own entity bundles
for (const sub of ["patents", "awards"]) {
  const hub = join(content, "outcomes", sub);
  if (!existsSync(hub)) continue;
  for (const name of readdirSync(hub)) {
    const p = join(hub, name);
    if (statSync(p).isDirectory() && !name.startsWith(".")) {
      errors.push(`outcomes/${sub}/${name}: entity bundle not allowed — keep entities in content/patent or content/award`);
    }
  }
}

if (errors.length) {
  console.error("content schema FAILED:\n" + errors.slice(0, 80).join("\n"));
  if (errors.length > 80) console.error(`... +${errors.length - 80} more`);
  process.exit(1);
}
console.log("content schema OK");
