<!--
title: Report Designer Troubleshooting (Parameters, Drill-down, and Refresh)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:report-designer:troubleshooting:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Report Designer Troubleshooting (Parameters, Drill-down, and Refresh)

## First questions to ask on any ticket
1. Is the user in **Excel Add-in** or **Web Portal**?
2. Is the issue on **open**, on **refresh**, or only on **drill-down**?
3. What are the parameter values (Entity, Period, Scenario) at the time of failure?
4. Does the same report work for another user?

These four questions usually isolate whether you have a permissions issue, a parameter mapping issue, or a data refresh issue.

## Parameters not applying (the "wrong period" problem)
**Symptoms**
- The report shows last month even after the user changed the period filter.
- The report runs, but numbers do not match expectations.

**Likely causes**
- The workbook cell that should pass the period is not bound to the report parameter.
- The web portal filter is set, but the report uses a different parameter name.
- The report definition uses a default parameter value that overrides the UI.

**Fix pattern**
- Verify the parameter name in the report definition.
- Verify the workbook or portal passes the same name.
- Remove conflicting defaults and rely on UI inputs.

## Drill-down shows blank or errors
**Symptoms**
- User clicks drill-down and sees an empty list.
- Drill-down opens but returns "no data" even though the summary has a value.

**Likely causes**
- Security filtering: user can see summary totals but cannot see transaction-level detail.
- Dimensional mismatch: summary uses mapped accounts, detail table uses natural accounts.
- The detail table is not refreshed, so it lags behind the summary cube.

**Fix pattern**
- Confirm the user has access to the transaction detail dataset.
- Confirm account and entity mappings between summary and detail.
- Confirm the data warehouse job that populates transaction detail completed.

## Excel Add-in ribbon missing
**Symptoms**
- Solver ribbon does not appear after Excel starts.

**Likely causes**
- Office add-in disabled after a crash.
- Excel trust center blocked the add-in.
- Add-in installed for the wrong Office bitness.

**Fix pattern**
- Check Excel add-ins list and re-enable.
- Validate the installed package matches Office bitness.
- If the add-in repeatedly disables, review crash logs and Office updates.

## Refresh fails intermittently
**Symptoms**
- Same report refresh works sometimes and fails other times.

**Likely causes**
- Network path instability (VPN, proxy, SSL inspection).
- Concurrency limits on the reporting service.
- Long-running queries timing out when the warehouse is busy.

**Fix pattern**
- Try the same refresh from a stable network segment.
- Schedule heavy refreshes outside close hours.
- Reduce the report scope (fewer entities or fewer periods) and confirm it completes.

## Common support messages and what they usually mean
- "I cannot see the company I need"  
  Usually a security role or dimension membership issue.
- "The numbers do not match the GL"  
  Usually the warehouse has not refreshed, or mappings differ between reports.
- "The drill-down does not work in Excel but works on the web"  
  Usually workbook parameter binding or a local add-in issue.
