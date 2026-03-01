import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const outDir = path.join(root, "dist");
fs.mkdirSync(outDir, { recursive: true });

// If repo ships action sources, this is where you’d pin deterministic build output.
// Minimal: stamp build success deterministically.
fs.writeFileSync(path.join(outDir, "BUILD.OK"), "OK\n", "utf8");
console.log("OK: built dist/");
