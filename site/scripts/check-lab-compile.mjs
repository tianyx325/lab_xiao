/**
 * Offline Sass compile check — does NOT write into assets/css.
 * Live cascade remains Hugo: main.scss → template.scss → lab/*
 */
import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const outDir = mkdtempSync(join(tmpdir(), "lab-css-"));
const outFile = join(outDir, "lab-check.css");
const entry = join(root, "assets/scss/lab-entry.scss");

const r = spawnSync(
  "npx",
  ["sass", entry, outFile, "--style=compressed", "--no-source-map"],
  { cwd: root, shell: true, encoding: "utf8" }
);
rmSync(outDir, { recursive: true, force: true });

if (r.status !== 0) {
  console.error(r.stderr || r.stdout || "sass failed");
  process.exit(r.status || 1);
}
console.log("lab-entry.scss compiles OK (offline check; Hugo owns live CSS)");
