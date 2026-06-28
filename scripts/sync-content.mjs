// Mirrors the study material from the repo root into public/content so Vite can
// serve it statically. The root folders are the single source of truth; this
// generated copy is git-ignored. Runs automatically via the predev/prebuild
// npm hooks, and can be run manually with `npm run sync-content`.
//
// Only .md and .py files are copied. Anything in public/content that no longer
// exists at the source is removed, so the copy can never silently drift.

import { cp, mkdir, rm, readdir, stat } from 'node:fs/promises';
import { existsSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const APP_ROOT = resolve(__dirname, '..');
const REPO_ROOT = resolve(APP_ROOT, '..');
const DEST = join(APP_ROOT, 'public', 'content');

// Topic source folders at the repo root: the python fundamentals bundle plus
// every NN_* DSA chapter. Excludes the app folder itself.
async function topicFolders() {
  const entries = await readdir(REPO_ROOT, { withFileTypes: true });
  return entries
    .filter((e) => e.isDirectory() && /^\d{2}_/.test(e.name))
    .map((e) => e.name)
    .sort();
}

async function copyContentFiles(srcDir, destDir) {
  await mkdir(destDir, { recursive: true });
  const entries = await readdir(srcDir, { withFileTypes: true });
  for (const entry of entries) {
    const src = join(srcDir, entry.name);
    const dest = join(destDir, entry.name);
    if (entry.isDirectory()) {
      await copyContentFiles(src, dest);
    } else if (/\.(md|py)$/.test(entry.name)) {
      await cp(src, dest);
    }
  }
}

async function main() {
  if (existsSync(DEST)) {
    await rm(DEST, { recursive: true, force: true });
  }
  await mkdir(DEST, { recursive: true });

  const folders = await topicFolders();
  let copied = 0;
  for (const folder of folders) {
    const src = join(REPO_ROOT, folder);
    if (!(await stat(src)).isDirectory()) continue;
    await copyContentFiles(src, join(DEST, folder));
    copied += 1;
  }

  console.log(`sync-content: mirrored ${copied} topic folders into public/content`);
}

main().catch((err) => {
  console.error('sync-content failed:', err);
  process.exit(1);
});
