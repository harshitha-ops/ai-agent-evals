# AI Agent Evals Starter

A small Python eval harness for testing an AI agent against a golden dataset.

## What it does
- Runs 10 golden cases: normal, tool use, auth, security, out-of-scope, ambiguous and hallucination
- Scores each reply with rules: required text, forbidden text, correct tool called
- Has a placeholder for an LLM-as-judge scorer
- Applies a release gate: 90% overall pass rate and 100% on security and auth cases

## Structure
- `evals/dataset.json`: golden test cases
- `evals/agent.py`: fake agent, to be replaced with a real API call
- `evals/scorers.py`: rule and judge scorers
- `evals/run_evals.py`: runner and release gate

## Run
    cd evals
    python3 run_evals.py

## Next steps
- Connect a real LLM agent with a pinned model version
- Implement the LLM-as-judge with a written rubric
- Track pass rate per run to detect drift
- Run in CI on every change and nightly
