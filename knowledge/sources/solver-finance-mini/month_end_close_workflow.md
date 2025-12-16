<!--
title: Month-End Close Workflow (Refresh, Reconcile, Lock, and Variance)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:close:workflow:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Month-End Close Workflow (Refresh, Reconcile, Lock, and Variance)

## Recommended close sequence (BI360 perspective)
This sequence keeps finance users from chasing moving numbers.

1. **Pre-close refresh**: load GL, AP, AR, and subledgers into the warehouse.
2. **Reconcile totals**: tie BI360 trial balance to the ERP trial balance.
3. **Post adjustments**: record accruals, reclasses, and eliminations.
4. **Final refresh**: update warehouse after adjustments.
5. **Run close package**: financial statements, rollforwards, and variance reports.
6. **Review and sign-off**: controller review and approvals.
7. **Lock the period**: prevent further changes for the closed month.
8. **Distribute reports**: publish to web portal and schedule delivery.

## Period lock: what it should do
A locked period means:
- Users cannot write planning entries to that period (if planning is enabled)
- Reports for that period represent a stable snapshot
- Any late adjustments require an explicit unlock and audit trail

In practice, organizations implement this through a combination of:
- ERP period controls
- BI360 planning permissions
- Reporting governance (who can refresh and when)

## Variance analysis workflow (supportable)
A variance workflow that reduces confusion:
- Compare Actual vs Budget for the same period.
- Compare Actual vs Prior Year for the same period.
- Explain variances using account groups and drill-down to transactions.

If drill-down does not show transactions, treat it as a warehouse detail access issue or a mapping issue.

## Close-week help desk rules of thumb
- Publish a daily "data as of" timestamp.
- Keep a short window for refresh changes and communicate it.
- If the controller signs off, freeze refresh until after reporting distribution.
