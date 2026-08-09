#!/usr/bin/env python3

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[2] / "skills/test-ui-ux/scripts/aggregate_scores.py"
SPEC = importlib.util.spec_from_file_location("aggregate_scores", SCRIPT)
aggregate_scores = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(aggregate_scores)


def method(name, score=8, confidence="high", critical_failures=None):
    return {
        "method": name,
        "score": score,
        "confidence": confidence,
        "evidence": [{"ref": "step-1", "claim": "Observed state"}],
        "findings": [],
        "critical_failures": critical_failures or [],
        "limitations": [],
        "methodology_data": {},
    }


def payload(*, interactive=True, source_kind="live_url", scores=None):
    scores = scores or [8, 9, 8, 7, 8]
    return {
        "schema_version": "1.0",
        "run_id": "run-001",
        "context": {
            "target": "https://example.test",
            "source_kind": source_kind,
            "test_brief": "Create a project",
            "target_user": "first-time team lead",
            "tasks": ["Create a project"],
            "viewport": "desktop 1440x900",
            "build_identity": "abc123",
            "constraints": [],
        },
        "interactive_test_completed": interactive,
        "comparable_to_previous": True,
        "methods": [
            method(name, score)
            for name, score in zip(aggregate_scores.METHODS, scores, strict=True)
        ],
    }


class AggregateScoresTest(unittest.TestCase):
    def test_equal_average_and_pass(self):
        output = aggregate_scores.aggregate(aggregate_scores.validate_input(payload()))
        self.assertEqual(output["average_score"], 8.0)
        self.assertEqual(output["verdict"], "pass")
        self.assertTrue(output["threshold_met"])

    def test_static_source_is_provisional(self):
        data = payload(interactive=False, source_kind="spec", scores=[10] * 5)
        output = aggregate_scores.aggregate(aggregate_scores.validate_input(data))
        self.assertEqual(output["average_score"], 10.0)
        self.assertEqual(output["verdict"], "provisional")

    def test_critical_failure_overrides_high_average(self):
        data = payload(scores=[10] * 5)
        data["methods"][0]["critical_failures"] = ["Core task destroys work"]
        output = aggregate_scores.aggregate(aggregate_scores.validate_input(data))
        self.assertEqual(output["average_score"], 10.0)
        self.assertEqual(output["verdict"], "fail")

    def test_missing_method_is_rejected(self):
        data = payload()
        data["methods"].pop()
        with self.assertRaisesRegex(ValueError, "exactly 5"):
            aggregate_scores.validate_input(data)

    def test_duplicate_method_is_rejected(self):
        data = payload()
        data["methods"][-1]["method"] = "spark"
        with self.assertRaisesRegex(ValueError, "duplicate"):
            aggregate_scores.validate_input(data)

    def test_out_of_range_score_is_rejected(self):
        data = payload()
        data["methods"][0]["score"] = 11
        with self.assertRaisesRegex(ValueError, "integer from 1 through 10"):
            aggregate_scores.validate_input(data)

    def test_non_live_interactive_claim_is_rejected(self):
        data = payload(interactive=True, source_kind="screenshot")
        with self.assertRaisesRegex(ValueError, "only for live_url or mixed"):
            aggregate_scores.validate_input(data)


if __name__ == "__main__":
    unittest.main()
