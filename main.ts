// gta6-meme-x-01 entry program (Node 22, standard library only).
// The entry itself is the X post named in POST.json: my agent made a GTA 6
// "WANTED — DEAD OR DELAYED" poster meme with make.fun's ghost in it, and the
// post carries the bounty link plus my play code. This program's only job is
// to hand that address to the grader: validate POST.json, then copy it to
// the output directory as POST.json (mode 0644, readable by every user).
//
// Local run:  mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { chmodSync, copyFileSync, mkdirSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

process.umask(0o022);

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const POST_FILE = join(BOT_DIR, 'POST.json');

let post: { url?: unknown };
try {
  post = JSON.parse(readFileSync(POST_FILE, 'utf8'));
} catch (err) {
  console.error(`POST.json unreadable at ${POST_FILE}: ${(err as Error).message}`);
  process.exit(1);
}

const url = typeof post.url === 'string' ? post.url : '';
if (!/^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/.test(url)) {
  console.error(`POST.json does not name an X post: ${JSON.stringify(post)}`);
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
const out = join(OUTPUT_DIR, 'POST.json');
copyFileSync(POST_FILE, out);
chmodSync(out, 0o644);

// Read the copy back and verify it names the same post before reporting
// success: a truncated or swapped output would hand the grader a bad
// address, so fail loudly instead of exiting 0 on a bad copy.
const written = JSON.parse(readFileSync(out, 'utf8')) as { url?: unknown };
if (written.url !== url) {
  console.error(`POST.json verification failed: wrote ${JSON.stringify(written)}, expected ${url}`);
  process.exit(1);
}
console.log(`POST.json -> ${out} (${url})`);
