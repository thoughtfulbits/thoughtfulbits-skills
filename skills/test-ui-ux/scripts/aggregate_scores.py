#!/usr/bin/env python3
"""Validate and aggregate the five test-ui-ux evaluator results."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, NoReturn


METHODS = (
    "spark",
    "nielsen",
    "cognitive_walkthrough",
    "pure",
    "wcag_2_2_aa",
)
SOURCE_KINDS = {"live_url", "screenshot", "spec", "mixed"}
CONFIDENCE_RANK = {"low": 0, "medium": 1, "high": 2}
SEVERITY_RANK = {"critical": 0, "high": 1, "medium": 2, "low": 3}
THRESHOLD = 8.0


def fail(message: str) -> NoReturn:
    raise ValueError(message)


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail(f"{label} must be an object")
    return value


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be an array")
    return value


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        fail(f"{label} must be a non-empty string")
    return value


def validate_method(raw: Any, index: int) -> dict[str, Any]:
    method = require_object(raw, f"methods[{index}]")
    name = require_string(method.get("method"), f"methods[{index}].method")
    if name not in METHODS:
        fail(f"methods[{index}].method has unsupported value {name!r}")

    score = method.get("score")
    if isinstance(score, bool) or not isinstance(score, int) or not 1 <= score <= 10:
        fail(f"methods[{index}].score must be an integer from 1 through 10")

    confidence = require_string(
        method.get("confidence"), f"methods[{index}].confidence"
    )
    if confidence not in CONFIDENCE_RANK:
        fail(f"methods[{index}].confidence must be high, medium, or low")

    evidence = require_list(method.get("evidence"), f"methods[{index}].evidence")
    if not evidence:
        fail(f"methods[{index}].evidence must contain at least one item")
    for evidence_index, raw_item in enumerate(evidence):
        item = require_object(
            raw_item, f"methods[{index}].evidence[{evidence_index}]"
        )
        require_string(
            item.get("ref"), f"methods[{index}].evidence[{evidence_index}].ref"
        )
        require_string(
            item.get("claim"),
            f"methods[{index}].evidence[{evidence_index}].claim",
        )

    findings = require_list(method.get("findings"), f"methods[{index}].findings")
    for finding_index, raw_finding in enumerate(findings):
        finding = require_object(
            raw_finding, f"methods[{index}].findings[{finding_index}]"
        )
        severity = require_string(
            finding.get("severity"),
            f"methods[{index}].findings[{finding_index}].severity",
        )
        if severity not in SEVERITY_RANK:
            fail(
                f"methods[{index}].findings[{finding_index}].severity "
                "must be critical, high, medium, or low"
            )
        for field in ("title", "evidence_ref", "recommendation"):
            require_string(
                finding.get(field),
                f"methods[{index}].findings[{finding_index}].{field}",
            )

    critical_failures = require_list(
        method.get("critical_failures"), f"methods[{index}].critical_failures"
    )
    for critical_index, critical in enumerate(critical_failures):
        require_string(
            critical,
            f"methods[{index}].critical_failures[{critical_index}]",
        )

    limitations = require_list(
        method.get("limitations"), f"methods[{index}].limitations"
    )
    for limitation_index, limitation in enumerate(limitations):
        require_string(
            limitation, f"methods[{index}].limitations[{limitation_index}]"
        )

    require_object(
        method.get("methodology_data"), f"methods[{index}].methodology_data"
    )
    return method


def validate_input(raw: Any) -> dict[str, Any]:
    data = require_object(raw, "input")
    if data.get("schema_version") != "1.0":
        fail("schema_version must be '1.0'")

    run_id = require_string(data.get("run_id"), "run_id")
    context = require_object(data.get("context"), "context")
    for field in ("target", "test_brief", "target_user", "viewport", "build_identity"):
        require_string(context.get(field), f"context.{field}")
    source_kind = require_string(context.get("source_kind"), "context.source_kind")
    if source_kind not in SOURCE_KINDS:
        fail("context.source_kind must be live_url, screenshot, spec, or mixed")
    tasks = require_list(context.get("tasks"), "context.tasks")
    if not tasks:
        fail("context.tasks must contain at least one task")
    for task_index, task in enumerate(tasks):
        require_string(task, f"context.tasks[{task_index}]")
    require_list(context.get("constraints"), "context.constraints")

    interactive = data.get("interactive_test_completed")
    comparable = data.get("comparable_to_previous")
    if not isinstance(interactive, bool):
        fail("interactive_test_completed must be a boolean")
    if not isinstance(comparable, bool):
        fail("comparable_to_previous must be a boolean")
    if interactive and source_kind not in {"live_url", "mixed"}:
        fail("interactive_test_completed can be true only for live_url or mixed input")

    raw_methods = require_list(data.get("methods"), "methods")
    if len(raw_methods) != len(METHODS):
        fail(f"methods must contain exactly {len(METHODS)} evaluator results")
    methods = [validate_method(method, index) for index, method in enumerate(raw_methods)]
    names = [method["method"] for method in methods]
    if len(set(names)) != len(names):
        fail("methods contains duplicate method identifiers")
    missing = sorted(set(METHODS) - set(names))
    extra = sorted(set(names) - set(METHODS))
    if missing or extra:
        fail(f"methods mismatch: missing={missing}, extra={extra}")

    return {
        "schema_version": "1.0",
        "run_id": run_id,
        "context": context,
        "interactive_test_completed": interactive,
        "comparable_to_previous": comparable,
        "methods": methods,
    }


def aggregate(data: dict[str, Any]) -> dict[str, Any]:
    methods_by_name = {method["method"]: method for method in data["methods"]}
    ordered_methods = [methods_by_name[name] for name in METHODS]
    scores = {method["method"]: method["score"] for method in ordered_methods}
    average = round(sum(scores.values()) / len(METHODS), 1)

    critical_failures = []
    for method in ordered_methods:
        for failure in method["critical_failures"]:
            critical_failures.append({"method": method["method"], "failure": failure})

    threshold_met = average >= THRESHOLD
    if critical_failures:
        verdict = "fail"
    elif not data["interactive_test_completed"]:
        verdict = "provisional"
    elif threshold_met:
        verdict = "pass"
    else:
        verdict = "fail"

    confidence = min(
        (method["confidence"] for method in ordered_methods),
        key=CONFIDENCE_RANK.__getitem__,
    )

    ranked_findings = []
    for method_order, method in enumerate(ordered_methods):
        for finding_order, finding in enumerate(method["findings"]):
            ranked_findings.append(
                (
                    SEVERITY_RANK[finding["severity"]],
                    method_order,
                    finding_order,
                    method["method"],
                    finding,
                )
            )
    ranked_findings.sort(key=lambda item: item[:3])

    top_fixes = []
    seen_titles = set()
    for _, _, _, method_name, finding in ranked_findings:
        normalized_title = finding["title"].casefold().strip()
        if normalized_title in seen_titles:
            continue
        seen_titles.add(normalized_title)
        top_fixes.append(
            {
                "method": method_name,
                "severity": finding["severity"],
                "title": finding["title"],
                "evidence_ref": finding["evidence_ref"],
                "recommendation": finding["recommendation"],
            }
        )
        if len(top_fixes) == 3:
            break

    return {
        "schema_version": "1.0",
        "run_id": data["run_id"],
        "context": data["context"],
        "interactive_test_completed": data["interactive_test_completed"],
        "comparable_to_previous": data["comparable_to_previous"],
        "method_scores": scores,
        "average_score": average,
        "threshold": THRESHOLD,
        "threshold_met": threshold_met,
        "critical_failures": critical_failures,
        "verdict": verdict,
        "confidence": confidence,
        "top_fixes": top_fixes,
        "methods": ordered_methods,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate and aggregate five test-ui-ux evaluator results."
    )
    parser.add_argument("input", help="Input JSON file, or - for standard input")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.input == "-":
            raw = json.load(sys.stdin)
        else:
            with Path(args.input).open(encoding="utf-8") as input_file:
                raw = json.load(input_file)
        output = aggregate(validate_input(raw))
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(json.dumps({"error": str(error)}, sort_keys=True), file=sys.stderr)
        return 2

    json.dump(output, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
