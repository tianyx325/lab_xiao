/**
 * Scan lab SCSS consumers for raw hex outside _tokens.scss.
 * Rem/px in non-token files are reported as warnings (except allowlist comments).
 */
import { readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const labDir = join(root, "assets/scss/lab");

function walk(dir, out = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, out);
    else if (name.endsWith(".scss")) out.push(p);
  }
  return out;
}

const hexRe = /#[0-9A-Fa-f]{3,8}\b/g;
const errors = [];
const files = walk(labDir);

for (const file of files) {
  const rel = relative(labDir, file).replace(/\\/g, "/");
  if (rel === "_tokens.scss") continue;
  const src = readFileSync(file, "utf8");
  const lines = src.split(/\r?\n/);
  lines.forEach((line, i) => {
    const code = line.replace(/\/\/.*$/, "").replace(/\/\*.*?\*\//g, "");
    if (/!important/.test(code)) {
      errors.push(`${rel}:${i + 1}: !important forbidden in lab consumers`);
    }
    const matches = code.match(hexRe);
    if (!matches) return;
    for (const m of matches) {
      errors.push(`${rel}:${i + 1}: raw hex ${m} — use tokens`);
    }
  });
}

if (errors.length) {
  console.error("hardcode scan FAILED:\n" + errors.slice(0, 50).join("\n"));
  if (errors.length > 50) console.error(`... +${errors.length - 50} more`);
  process.exit(1);
}
console.log("hardcode scan OK", { files: files.length });
