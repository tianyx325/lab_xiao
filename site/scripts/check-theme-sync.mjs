/**
 * Ensure data/themes/* primary/ink match lab/_tokens.scss seeds.
 */
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const tokens = readFileSync(join(root, "assets/scss/lab/_tokens.scss"), "utf8");
const toml = readFileSync(join(root, "data/themes/minimal.toml"), "utf8");
const yaml = readFileSync(join(root, "data/themes/lab.yaml"), "utf8");

function scssVar(name) {
  const m = tokens.match(new RegExp(`\\$${name}:\\s*#([0-9A-Fa-f]{3,8})`));
  if (!m) throw new Error(`missing $${name} in _tokens.scss`);
  let h = m[1].toUpperCase();
  if (h.length === 3) h = h.split("").map((c) => c + c).join("");
  return `#${h}`;
}

const blue = scssVar("lab-blue");
const ink = scssVar("lab-ink");
const page = scssVar("lab-page-bg");
const errors = [];

function mustInclude(label, text, value) {
  const ok = text.toUpperCase().includes(value.toUpperCase());
  if (!ok) errors.push(`${label} missing ${value}`);
}

mustInclude("minimal.toml light primary", toml, blue);
mustInclude("minimal.toml menu_text", toml, ink === "#000000" || ink === "#000" ? "#000000" : ink);
mustInclude("minimal.toml home_section", toml, page);
mustInclude("lab.yaml primary", yaml, blue);
mustInclude("lab.yaml foreground", yaml, ink === "#000000" || ink === "#000" ? "#000000" : ink);
mustInclude("lab.yaml background", yaml, page);

if (errors.length) {
  console.error("theme sync FAILED:\n" + errors.map((e) => " - " + e).join("\n"));
  process.exit(1);
}
console.log("theme sync OK", { blue, ink, page });
