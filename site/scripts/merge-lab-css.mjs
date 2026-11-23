/**
 * Offline guard — keeps assets/css/custom.css empty.
 * Live CSS = Hugo Sass only: main.scss → template.scss → lab/*
 */
import { writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
writeFileSync(
  join(root, "assets/css/custom.css"),
  `/* EMPTY — Hugo owns the lab cascade (main.scss → template.scss → lab/*).
 * Do not put lab styles here.
 */
`,
  "utf8"
);
console.log("custom.css kept empty (Hugo owns lab cascade)");
