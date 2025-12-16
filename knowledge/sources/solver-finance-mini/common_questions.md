<!--
title: Common Solver BI360 Support Questions (Finance and IT)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:faq:common-questions:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Common Solver BI360 Support Questions (Finance and IT)

## FAQ: Report building and running
**Q: How do I create a rolling 12-month report?**  
A: Use an `AsOfPeriod` parameter and define the report period range relative to it (prior 11 periods plus the as-of period). See: Report Designer Basics.

**Q: Why does my report show the wrong period?**  
A: Most cases are parameter binding issues between Excel or the web filter and the report definition. Verify the parameter names and defaults. See: Report Designer Troubleshooting.

**Q: Why does drill-down show blank?**  
A: Drill-down depends on transaction-level tables and permissions. Confirm the detail dataset is refreshed and the user role permits detail access. See: Report Designer Troubleshooting.

## FAQ: Data warehouse and refresh
**Q: Why is my data not refreshing?**  
A: Check the last successful warehouse job, confirm the schedule is enabled, and verify the user filters match the refreshed period. See: Data Warehouse Connectors and Refresh.

**Q: What is the difference between live and static database?**  
A: Live queries the ERP directly; static uses a scheduled warehouse refresh. Month-end workflows typically prefer static for stability. See: Data Warehouse Connectors and Refresh.

**Q: How do I connect QuickBooks to the data warehouse?**  
A: Use a connector profile with credentials and company selection, then run an initial load and validate record counts. Token expiration is a common issue. See: Data Warehouse Connectors and Refresh.

## FAQ: Consolidations and planning
**Q: How do intercompany eliminations work?**  
A: Eliminations offset transactions where entity and partner entity differ, posting to an elimination layer while preserving source detail for audit. See: Consolidations and Intercompany.

**Q: What is the difference between budget version and forecast?**  
A: Budget is the approved plan; forecast is a periodic re-estimate. Versions separate baseline from scenarios. See: Budgeting and Forecasting.

## Out of scope behavior
If a question requires an organization-specific policy that is not in this library (for example, "What is our controller's approval threshold?"), the correct answer is:  
"I cannot answer from this local library. Add your internal policy document to the pack and recompile."
