/**
 * Run Hugo with a Dart Sass binary on PATH.
 *
 * Hugo's dartsass transpiler executes a `sass` executable. The pure-JS
 * `sass` npm package cannot serve it, so this wrapper finds the Dart Sass
 * binary bundled with `sass-embedded` (installed by `npm ci`) — or the
 * optional repo-local copy under tools/dart-sass — and prepends it to PATH.
 *
 * Usage: node scripts/hugo.mjs <hugo args...>
 *   npm run build
 *   npm run dev
 */
import { spawn } from "node:child_process";
import { existsSync, readdirSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = join(dirname(fileURLToPath(import.meta.url)), "..");
const repoRoot = join(siteRoot, "..");
const args = process.argv.slice(2);

function sassDirs() {
  const dirs = [];
  const local = join(repoRoot, "tools", "dart-sass", "dart-sass");
  if (existsSync(local)) dirs.push(local);

  const modules = join(siteRoot, "node_modules");
  if (existsSync(modules)) {
    for (const name of readdirSync(modules)) {
      if (!name.startsWith("sass-embedded-")) continue;
      const dir = join(modules, name, "dart-sass");
      if (existsSync(dir)) dirs.push(dir);
    }
  }
  return dirs;
}

if (args[0] === "server") {
  rmSync(join(siteRoot, "resources", "_gen"), { recursive: true, force: true });
  // Keep the dev server away from a stale production public/ directory,
  // which Hugo serves statically and would shadow the in-memory pages.
  rmSync(join(siteRoot, "resources", "_dev-server"), { recursive: true, force: true });
}

const sep = process.platform === "win32" ? ";" : ":";
const path = [...sassDirs(), process.env.PATH || ""].join(sep);
const child = spawn("hugo", args, {
  cwd: siteRoot,
  stdio: "inherit",
  env: { ...process.env, PATH: path },
});

child.on("error", (err) => {
  console.error(`Failed to start hugo: ${err.message}`);
  console.error("Install Hugo Extended 0.168+ and Dart Sass (npm ci provides sass-embedded).");
  process.exit(1);
});
child.on("exit", (code) => process.exit(code ?? 1));