<!--
title: Budgeting and Forecasting (Versions, Spreading, and What-if)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:planning:budgeting-forecasting:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Budgeting and Forecasting (Versions, Spreading, and What-if)

## Budget vs forecast: how to explain it to users
- **Budget**: the approved plan, often built once per year, sometimes revised.
- **Forecast**: a periodic re-estimate based on actuals and new assumptions.

In BI360 planning, users typically select a **Version** (Budget 2026, Forecast Q1, etc.) and enter values by account, cost center, and period.

## Budget versions (why they exist)
Multiple versions allow:
- Baseline budget vs working budget
- Department submissions vs approved final
- Scenario analysis (base, conservative, aggressive)

Support tip: when users say "my numbers disappeared", confirm they are in the correct version.

## Spreading methods (common patterns)
Users often ask: "How do I spread this across months?"

Typical spreading behaviors:
- Even spread across selected periods
- Based on prior year actual proportions
- Weighted seasonal curve (front-loaded, back-loaded)

A good help desk answer names the method and the exact period range affected.

## What-if analysis workflow
A safe what-if workflow avoids overwriting approved numbers:
1. Copy the baseline version to a new scenario version.
2. Apply changes in the scenario version only.
3. Run variance reports comparing scenario vs baseline.
4. Promote the scenario to approved only after review.

## Driver-based budgeting (common misconception)
Some users expect "drivers" to auto-calculate every line. In many deployments, BI360 supports driver-style templates, but the organization still defines:
- Which accounts are driver-based
- Where drivers live (headcount, units, rates)
- How drivers roll up to accounts

If these definitions are not configured, users end up doing driver math in Excel.
