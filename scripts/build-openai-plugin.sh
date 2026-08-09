#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "${script_dir}/.." && pwd)"

node "${repo_root}/scripts/validate-openai-plugin.mjs"

plugin_name="$(node -p "require('${repo_root}/.codex-plugin/plugin.json').name")"
plugin_version="$(node -p "require('${repo_root}/.codex-plugin/plugin.json').version")"
output_path="${1:-${repo_root}/dist/${plugin_name}-${plugin_version}-openai.zip}"

if [[ "${output_path}" != /* ]]; then
  output_path="$(pwd)/${output_path}"
fi

mkdir -p "$(dirname "${output_path}")"
temp_root="$(mktemp -d "${TMPDIR:-/tmp}/${plugin_name}.XXXXXX")"
trap 'rm -rf "${temp_root}"' EXIT

package_root="${temp_root}/${plugin_name}"
mkdir -p "${package_root}"
cp -R "${repo_root}/.codex-plugin" "${package_root}/.codex-plugin"
cp -R "${repo_root}/skills" "${package_root}/skills"
cp -R "${repo_root}/assets" "${package_root}/assets"
cp "${repo_root}/LICENSE" "${package_root}/LICENSE"

# Keep local interpreter and operating-system artifacts out of the submitted ZIP.
find "${package_root}" -type d -name '__pycache__' -prune -exec rm -rf {} +
find "${package_root}" -type f \( -name '*.pyc' -o -name '.DS_Store' \) -delete

rm -f "${output_path}"
(
  cd "${package_root}"
  zip -q -r "${output_path}" .
)

echo "Built ${output_path}"
unzip -l "${output_path}"
