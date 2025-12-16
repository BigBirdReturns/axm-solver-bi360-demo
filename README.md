# Solver BI360 AXM Demo

Purpose-built demo for Allan Bacero (Senior IT Manager at Solver) showing how AXM eliminates Copilot-style hallucinations for Solver BI360 workflow questions by using compiled, source-cited knowledge.

## What this demo proves

- Deterministic answers from a local compiled library (no generation at query time)
- Every answer includes a source citation (provenance)
- Out-of-scope questions return: `I cannot answer from this local library.`
- Runs locally and in Docker

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app/app.py
```

## Run with Docker

```bash
docker build -t solver-bi360-axm-demo .
docker run --rm -p 8501:8501 solver-bi360-axm-demo
```

## Sample questions

- How do I set up drill-down in my report?
- How do I create a rolling 12-month report?
- Why is my data not refreshing?
- What's the difference between live and static database?
- How do intercompany eliminations work?
- How do I connect QuickBooks to the data warehouse?
- How do I lock a period after month-end close?
- What's the recommended month-end close sequence?

## Repo contents

- `knowledge/sources/solver-finance-mini/` synthetic Solver BI360 knowledge notes
- `knowledge/compiled/solver-finance-mini/` compiled library used by the demo
- `axm_core/` minimal offline retrieval + provenance enforcement
- `app/app.py` Streamlit UI

## Notes

This repo intentionally contains only the Solver BI360 demo. It does not include other apps or tutor modules.
