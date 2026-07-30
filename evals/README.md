# Evals

Each skill has its own suite: `evals/<skill-name>/evals.json`, with fixtures under `evals/<skill-name>/files/`. All `files` paths (in the `files` arrays and inside prompt text) are repo-root-relative.

## Shared fixtures

The board-deck fixtures under `evals/board-deck-audit/files/` are shared: the `board-feedback` suite references them directly instead of keeping copies, because both suites' expectations quote the same planted facts (specific churn numbers, cash math, metric definitions). **Editing any fixture in `evals/board-deck-audit/files/` requires re-checking the expectations of both the board-deck-audit and board-feedback suites.**

The two product suites (`product-plan-feedback`, `product-feature-feedback`) own their fixtures outright. Their fixtures contain planted verbatim lines that expectations quote — keep quoted lines exactly in sync when editing either side.
