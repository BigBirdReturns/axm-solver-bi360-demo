<!--
title: Report Designer Basics (Excel Add-in and Web Portal)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:report-designer:basics:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Report Designer Basics (Excel Add-in and Web Portal)

## What users mean by "Report Designer"
In Solver BI360, finance teams typically build and run reports in two places:

- **Excel Add-in**: report building and refresh inside Excel. Common for month end workbooks.
- **Web Portal**: report viewing and distribution through the browser. Often used for scheduled delivery and read-only users.

Both surfaces point to the same underlying report definitions, but the user experience differs.

## Installing and validating the Excel Add-in
**Checklist**
1. Confirm the user is licensed for reporting and can sign in.
2. Confirm Excel bitness (32-bit vs 64-bit) matches the add-in package installed by IT.
3. Open Excel, then locate the Solver ribbon and verify it shows the correct environment (prod vs test).
4. Run a simple report refresh to validate connectivity.

**Support signal**
- If the ribbon loads but the user cannot sign in, treat it as an authentication or tenant selection issue.
- If the ribbon does not load, treat it as an add-in registration issue (often Office trust settings).

## Creating a new report and running it
**Core steps**
1. Create a new report definition.
2. Select the data source model (the BI360 Data Warehouse or the configured dataset).
3. Add rows, columns, and measures using your chart of accounts and dimensions.
4. Save the report, then run it with a parameter set.

**Common parameter examples**
- **Period**: 2025-11
- **Scenario/Version**: Actual, Budget, Forecast
- **Entity**: Company, Business Unit, Cost Center

## Rolling 12-month report pattern
A rolling 12-month report requires two parts:

1. A parameter (or internal variable) representing the **as-of period**.
2. A date range that selects **the prior 11 periods plus the as-of period**.

**Practical setup**
- Create a parameter called `AsOfPeriod`.
- Set the column axis to a period range derived from `AsOfPeriod`.
- If the report output is in Excel, place `AsOfPeriod` in a visible input cell and protect it with data validation.

**Support signal**
When users say "my rolling report is stuck", it usually means the `AsOfPeriod` parameter is not being passed from the workbook or the web portal filter.

## Drill-down behavior
Users expect drill-down to answer: "What transactions make up this number?"

Typical drill-down modes:
- **Account detail**: expands from a summary account into natural account lines.
- **Entity detail**: expands from consolidated to entity-level.
- **Transaction detail**: opens a detail grid based on the underlying fact table.

Drill-down usually depends on:
- The report cell having a clear dimensional intersection (Account, Entity, Period, Scenario).
- The data warehouse having a transaction-level table available for that intersection.

## Naming conventions that reduce support tickets
- Prefix report names by domain: `FIN - Close - Variance`, `FIN - BS - Rollforward`.
- Put the parameter list into the report description: `Entity, Period, Scenario`.
- Store shared templates in a controlled folder, not personal workspaces.
