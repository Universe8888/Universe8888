from pathlib import Path


README = Path(__file__).resolve().parents[1] / "README.md"


def readme_text() -> str:
    return README.read_text(encoding="utf-8")


def test_wikilens_copy_uses_current_honest_benchmark_language() -> None:
    text = readme_text()

    required_phrases = [
        "8 shipped agents. Six hand-labeled evals. One Markdown vault.",
        "8 agents, with honest per-run benchmark status:",
        "Harness + targets; not yet benchmarked",
        "six agents have hand-labeled evals",
        "attribution rate = 0.90-1.00",
    ]
    for phrase in required_phrases:
        assert phrase in text


def test_wikilens_copy_does_not_reintroduce_old_overclaims() -> None:
    text = readme_text()

    stale_phrases = [
        "8 evaluated agents. One command. Any Markdown vault.",
        "8 agents, each with published benchmarks:",
        "every agent ships with hand-labeled fixtures",
        "attribution rate = 1.00",
        "P >= 0.80 target",
        "P ≥ 0.80 target",
        "F1 >= 0.70 target",
        "F1 ≥ 0.70 target",
    ]
    for phrase in stale_phrases:
        assert phrase not in text


def test_profile_links_core_public_projects() -> None:
    text = readme_text()

    required_links = [
        "https://github.com/Universe8888/wikilens",
        "https://github.com/Universe8888/mcp-govcheck",
        "https://github.com/Universe8888/job-hunt-automator",
        "https://github.com/Universe8888/pre-viral",
    ]
    for link in required_links:
        assert link in text
