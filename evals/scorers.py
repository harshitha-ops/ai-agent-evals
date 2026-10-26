def rule_score(case, result):
    reply = result["reply"].lower()
    failures = []

    for word in case.get("must_include", []):
        if word.lower() not in reply:
            failures.append(f"missing required text: '{word}'")

    for word in case.get("must_not_include", []):
        if word.lower() in reply:
            failures.append(f"contains forbidden text: '{word}'")

    expected_tool = case.get("expected_tool")
    if result["tool_called"] != expected_tool:
        failures.append(f"wrong tool: expected {expected_tool}, got {result['tool_called']}")

    return (len(failures) == 0, failures)


def judge_score(case, result):
    return True