import fs from "node:fs";
import assert from "node:assert";

assert(fs.existsSync("README.md"), "E_MISSING_README");
assert(fs.existsSync("LICENSE"), "E_MISSING_LICENSE");

// If this is a GitHub Action, enforce manifest presence.
const hasAction = fs.existsSync("action.yml") || fs.existsSync("action.yaml");
if (hasAction) {
  const yml = fs.existsSync("action.yml") ? "action.yml" : "action.yaml";
  const txt = fs.readFileSync(yml, "utf8");
  assert(/runs:/m.test(txt), "E_ACTION_MISSING_RUNS");
  assert(/name:/m.test(txt), "E_ACTION_MISSING_NAME");
}

console.log("OK: sanity");
