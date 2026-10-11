
from src.trajectory_analyzer import analyze_agent


def make_step(number, action, status, observation):
    return {
        "step": number,
        "action": action,
        "tool": "pytest" if action == "run_tests" else None,
        "status": status,
        "observation": observation
    }


def test_successful_agent():
    trajectory = [
        make_step(1, "run_tests", "success", "5 passed"),
        make_step(2, "final_response", "success",
                  "All tests passed.")
    ]

    result = analyze_agent("Agent_A", trajectory)

    assert result["false_success_claim"] is False
    assert result["latest_test_status"] == "success"


def test_false_success_claim():
    trajectory = [
        make_step(1, "run_tests", "failed", "2 failed"),
        make_step(2, "final_response", "success",
                  "All tests passed.")
    ]

    result = analyze_agent("Agent_C", trajectory)

    assert result["false_success_claim"] is True


def test_recovery():
    trajectory = [
        make_step(1, "run_tests", "failed", "2 failed"),
        make_step(2, "run_tests", "success", "5 passed")
    ]

    result = analyze_agent("Agent_B", trajectory)

    assert result["recovered"] is True


def test_repeated_failures():
    trajectory = [
        make_step(1, "run_tests", "failed", "2 failed"),
        make_step(2, "run_tests", "failed", "2 failed")
    ]

    result = analyze_agent("Agent_D", trajectory)

    assert result["repeated_failures"] is True
