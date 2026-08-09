#!/usr/bin/env node

import { existsSync, readFileSync, readdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const readJson = (path) => JSON.parse(readFileSync(join(repoRoot, path), "utf8"));
const fail = (message) => {
  throw new Error(message);
};

const claude = readJson(".claude-plugin/plugin.json");
const marketplace = readJson(".claude-plugin/marketplace.json");
const openai = readJson(".codex-plugin/plugin.json");
const marketplaceEntry = marketplace.plugins?.find(
  (candidate) => candidate.name === claude.name,
);

if (!marketplaceEntry) fail(`Claude marketplace is missing ${claude.name}`);

for (const [label, value] of [
  ["Claude plugin", claude],
  ["Claude marketplace", marketplaceEntry],
  ["OpenAI plugin", openai],
]) {
  if (value.name !== "thoughtfulbits-skills") {
    fail(`${label} has unexpected name ${JSON.stringify(value.name)}`);
  }
  if (!/^\d+\.\d+\.\d+$/.test(value.version)) {
    fail(`${label} has invalid stable semantic version ${JSON.stringify(value.version)}`);
  }
}

if (
  claude.version !== marketplaceEntry.version ||
  claude.version !== openai.version
) {
  fail(
    `Version mismatch: Claude=${claude.version}, marketplace=${marketplaceEntry.version}, OpenAI=${openai.version}`,
  );
}

if (openai.author?.name !== "ThoughtfulBits Consulting") {
  fail("OpenAI author must be ThoughtfulBits Consulting");
}
if (openai.author.name !== openai.interface?.developerName) {
  fail("OpenAI author.name and interface.developerName must match");
}
if (openai.skills !== "./skills/") fail("OpenAI skills path must be ./skills/");
if (openai.mcpServers || openai.apps || openai.interface?.screenshots) {
  fail("Skills-only submissions cannot include MCP, app, or screenshot configuration");
}

const { interface: ui } = openai;
if (!ui || typeof ui !== "object") fail("OpenAI interface metadata is required");
if (!ui.displayName || ui.displayName.length > 30) {
  fail("interface.displayName is required and must be 30 characters or fewer");
}
if (!ui.shortDescription || ui.shortDescription.length > 30) {
  fail("interface.shortDescription is required and must be 30 characters or fewer");
}
if (!ui.longDescription || ui.longDescription.length > 4000) {
  fail("interface.longDescription is required and must be 4,000 characters or fewer");
}
if (ui.category !== "Business & Operations") {
  fail("interface.category must be Business & Operations");
}
if (!Array.isArray(ui.capabilities) || ui.capabilities.length !== 4) {
  fail("Exactly four plugin capabilities are required");
}
if (!Array.isArray(ui.defaultPrompt) || ui.defaultPrompt.length > 3) {
  fail("interface.defaultPrompt must contain no more than three prompts");
}
for (const prompt of ui.defaultPrompt) {
  if (!prompt || prompt.length > 128) {
    fail("Each default prompt must be non-empty and 128 characters or fewer");
  }
}
if (!/^#[0-9A-F]{6}$/i.test(ui.brandColor)) {
  fail("interface.brandColor must be a six-digit hex color");
}
if (ui.brandColor.toUpperCase() !== "#2864FF") {
  fail("interface.brandColor must use the ThoughtfulBits cobalt #2864FF");
}

for (const field of [
  "websiteURL",
  "privacyPolicyURL",
  "termsOfServiceURL",
  "supportURL",
]) {
  const value = ui[field];
  if (!value || !value.startsWith("https://") || value.length > 1024) {
    fail(`interface.${field} must be an HTTPS URL no longer than 1,024 characters`);
  }
}

for (const field of ["composerIcon", "logo"]) {
  const value = ui[field];
  if (!value?.startsWith("./")) fail(`interface.${field} must use a ./ path`);
  if (!existsSync(join(repoRoot, value))) fail(`Missing interface.${field}: ${value}`);
}

const png = readFileSync(join(repoRoot, ui.logo));
if (!png.subarray(0, 8).equals(Buffer.from("89504e470d0a1a0a", "hex"))) {
  fail("interface.logo must be a valid PNG");
}
const width = png.readUInt32BE(16);
const height = png.readUInt32BE(20);
if (width !== height || width < 48 || width > 4096) {
  fail(`interface.logo must be square and 48-4096px; received ${width}x${height}`);
}

for (const [assetPath, minimum] of [
  ["assets/openai/directory-icon-light.png", 256],
  ["assets/openai/directory-icon-dark.png", 256],
  ["assets/openai/composer-icon-light.png", 48],
  ["assets/openai/composer-icon-dark.png", 48],
]) {
  const asset = readFileSync(join(repoRoot, assetPath));
  if (!asset.subarray(0, 8).equals(Buffer.from("89504e470d0a1a0a", "hex"))) {
    fail(`${assetPath} must be a valid PNG`);
  }
  const assetWidth = asset.readUInt32BE(16);
  const assetHeight = asset.readUInt32BE(20);
  if (assetWidth !== assetHeight || assetWidth < minimum || assetWidth > 4096) {
    fail(`${assetPath} must be square and ${minimum}-4096px; received ${assetWidth}x${assetHeight}`);
  }
}

const skillRoot = join(repoRoot, "skills");
const skillDirs = readdirSync(skillRoot, { withFileTypes: true })
  .filter((entry) => entry.isDirectory())
  .map((entry) => entry.name)
  .sort();

if (skillDirs.length !== 5) fail(`Expected five skills; found ${skillDirs.length}`);

for (const skillName of skillDirs) {
  const skillPath = join(skillRoot, skillName, "SKILL.md");
  const agentPath = join(skillRoot, skillName, "agents/openai.yaml");
  if (!existsSync(skillPath)) fail(`Missing ${skillPath}`);
  if (!existsSync(agentPath)) fail(`Missing ${agentPath}`);

  const skill = readFileSync(skillPath, "utf8");
  const frontmatter = skill.match(/^---\n([\s\S]*?)\n---/);
  if (!frontmatter) fail(`${skillName}/SKILL.md is missing YAML frontmatter`);
  if (!new RegExp(`^name:\\s*${skillName}$`, "m").test(frontmatter[1])) {
    fail(`${skillName}/SKILL.md has a mismatched name`);
  }
  if (!/^description:\s*\S/m.test(frontmatter[1])) {
    fail(`${skillName}/SKILL.md is missing a description`);
  }

  const agent = readFileSync(agentPath, "utf8");
  for (const required of [
    /^interface:$/m,
    /^\s+display_name:\s*\S/m,
    /^\s+short_description:\s*\S/m,
    /^\s+default_prompt:\s*\S/m,
    /^policy:$/m,
    /^\s+allow_implicit_invocation:\s*true$/m,
  ]) {
    if (!required.test(agent)) fail(`${skillName}/agents/openai.yaml is incomplete`);
  }
  const policy = agent.match(/^policy:\n((?:[ \t]+.*(?:\n|$))*)/m)?.[1] ?? "";
  const policyKeys = [...policy.matchAll(/^\s+([a-z_]+):/gm)].map((match) => match[1]);
  if (
    policyKeys.length !== 1 ||
    policyKeys[0] !== "allow_implicit_invocation"
  ) {
    fail(
      `${skillName}/agents/openai.yaml policy may contain only allow_implicit_invocation`,
    );
  }
}

console.log(
  `Validated ${openai.name} ${openai.version}: ${skillDirs.length} skills, native OpenAI metadata, and submission assets.`,
);
