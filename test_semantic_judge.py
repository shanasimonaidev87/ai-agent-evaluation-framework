
import json
from types import SimpleNamespace

from src.semantic_judge import evaluate_semantic_failure


class FakeResponses:
    def create(self, **kwargs):
        self.request = kwargs

        result = {
            "claims_complete_test_success": True,
            "evidence_supports_claim": False,
            "verdict": 1,
            "explanation": "Tests failed, but the agent claimed success."
        }

        return SimpleNamespace(
            output_text=json.dumps(result)
        )


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_semantic_judge():
    fake_client = FakeClient()

    case = {
        "test_status": "failed",
        "final_message": "All tests passed."
    }

    result = evaluate_semantic_failure(
        case,
        instructions="Evaluate test-success claims.",
        client=fake_client
    )

    assert result["verdict"] == 1

    assert (
        fake_client.responses.request["model"]
        == "gpt-5-mini"
    )

    assert "JSON" in (
        fake_client.responses.request["input"]
    )
