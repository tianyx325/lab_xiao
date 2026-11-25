/**
 * Ensure zh.yaml and en.yaml define the same translation keys.
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

function keys(file) {
  const out = new Set();
  for (const line of readFileSync(join(root, "i18n", file), "utf8").split(/\r?\n/)) {
    const m = line.match(/^\s*-\s*id:\s*([A-Za-z0-9_.-]+)/);
    if (m) out.add(m[1]);
  }
  return out;
}

const zh = keys("zh.yaml");
const en = keys("en.yaml");
const missingEn = [...zh].filter((k) => !en.has(k));
const missingZh = [...en].filter((k) => !zh.has(k));

if (missingEn.length || missingZh.length) {
  console.error("i18n key mismatch");
  if (missingEn.length) console.error(`  missing in en.yaml: ${missingEn.join(", ")}`);
  if (missingZh.length) console.error(`  missing in zh.yaml: ${missingZh.join(", ")}`);
  process.exit(1);
}
console.log(`i18n keys OK (${zh.size})`);