#!/usr/bin/env python3

import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[2] / "skills/test-ui-ux/scripts/aggregate_scores.py"
SPEC = importlib.util.spec_from_file_location("aggregate_scores", SCRIPT)
aggregate_scores = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(aggregate_scores)


def valid_action_analysis(evidence_status="observed", known_counts=True):
    counts = {
        "logical_steps": 3,
        "clicks_taps": 3,
        "required_fields": 2,
        "optional_fields": 0,
    }
    if not known_counts:
        counts = {field: None for field in counts}
    return {
        "screens": [
            {
                "id": "project-form",
                "evidence_ref": "step-1",
                "purpose": "Collect the minimum project setup information.",
                "important_action_ids": ["create-project"],
            }
        ],
        "actions": [
            {
                "id": "create-project",
                "label": "Create a project",
                "importance": "primary",
                "outcome": "A saved project is ready for work.",
                "evidence_status": evidence_status,
                "steps": [
                    {
                        "order": 1,
                        "screen_id": "project-form",
                        "description": "Enter the project name.",
                        "interaction": "field_entry",
                        "pointer_activations": 1,
                        "difficulty": 1,
                        "avoidable": False,
                    },
                    {
                        "order": 2,
                        "screen_id": "project-form",
                        "description": "Enter the desired outcome.",
                        "interaction": "field_entry",
                        "pointer_activations": 1,
                        "difficulty": 2,
                        "avoidable": True,
                    },
                    {
                        "order": 3,
                        "screen_id": "project-form",
                        "description": "Create the project.",
                        "interaction": "click_tap",
                        "pointer_activations": 1,
                        "difficulty": 1,
                        "avoidable": False,
                    },
                ],
                "current_counts": counts,
                "inputs": [
                    {
                        "name": "Project name",
                        "current_requirement": "required",
                        "recommendation": "keep_user_required",
                        "confirmation_required": False,
                        "sensitive_or_consequential": False,
                        "rationale": "The user owns the project identity.",
                    },
                    {
                        "name": "Desired outcome",
                        "current_requirement": "required",
                        "recommendation": "ai_draft_confirm",
                        "confirmation_required": True,
                        "sensitive_or_consequential": False,
                        "rationale": "Offer an editable draft from known project context.",
                    },
                ],
                "simplest_safe_path": {
                    "logical_steps": 2,
                    "clicks_taps": 2,
                    "required_fields": 1,
                    "optional_fields": 1,
                    "changes": ["Make the outcome optional and offer an editable draft."],
                    "safeguards": ["Require confirmation before project creation."],
                },
            }
        ],
    }


def method(name, score=8, confidence="high", critical_failures=None):
    methodology_data = {}
    if name == "pure":
        methodology_data["action_analysis"] = valid_action_analysis()
    return {
        "method": name,
        "score": score,
        "confidence": confidence,
        "evidence": [{"ref": "step-1", "claim": "Observed state"}],
        "findings": [],
        "critical_failures": critical_failures or [],
        "limitations": [],
        "methodology_data": methodology_data,
    }


def payload(*, interactive=True, source_kind="live_url", scores=None):
    scores = scores or [8, 9, 8, 7, 8]
    return {
        "schema_version": "2.0",
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
        self.assertEqual(
            output["action_analysis"],
            output["methods"][3]["methodology_data"]["action_analysis"],
        )

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

    def test_missing_action_analysis_is_rejected(self):
        data = payload()
        del data["methods"][3]["methodology_data"]["action_analysis"]
        with self.assertRaisesRegex(ValueError, "action_analysis must be an object"):
            aggregate_scores.validate_input(data)

    def test_unknown_action_reference_is_rejected(self):
        data = payload()
        analysis = data["methods"][3]["methodology_data"]["action_analysis"]
        analysis["screens"][0]["important_action_ids"] = ["missing-action"]
        with self.assertRaisesRegex(ValueError, "unknown actions"):
            aggregate_scores.validate_input(data)

    def test_negative_count_is_rejected(self):
        data = payload()
        analysis = data["methods"][3]["methodology_data"]["action_analysis"]
        analysis["actions"][0]["current_counts"]["clicks_taps"] = -1
        with self.assertRaisesRegex(ValueError, "nonnegative integer"):
            aggregate_scores.validate_input(data)

    def test_static_unknown_counts_are_accepted(self):
        data = payload(interactive=False, source_kind="screenshot")
        data["methods"][3]["methodology_data"]["action_analysis"] = (
            valid_action_analysis(evidence_status="visible_only", known_counts=False)
        )
        output = aggregate_scores.aggregate(aggregate_scores.validate_input(data))
        self.assertEqual(output["verdict"], "provisional")
        self.assertIsNone(
            output["action_analysis"]["actions"][0]["current_counts"]["logical_steps"]
        )

    def test_unconfirmed_ai_draft_is_rejected(self):
        data = payload()
        analysis = data["methods"][3]["methodology_data"]["action_analysis"]
        analysis["actions"][0]["inputs"][1]["confirmation_required"] = False
        with self.assertRaisesRegex(ValueError, "AI drafts must require confirmation"):
            aggregate_scores.validate_input(data)

    def test_schema_one_is_rejected(self):
        data = payload()
        data["schema_version"] = "1.0"
        with self.assertRaisesRegex(ValueError, "schema_version must be '2.0'"):
            aggregate_scores.validate_input(data)


if __name__ == "__main__":
    unittest.main()
