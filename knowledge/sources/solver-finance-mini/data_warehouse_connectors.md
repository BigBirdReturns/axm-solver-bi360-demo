<!--
title: BI360 Data Warehouse Connectors and Refresh (Live vs Static, Jobs, and Schedules)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:data-warehouse:connectors:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# BI360 Data Warehouse Connectors and Refresh (Live vs Static, Jobs, and Schedules)

## What the data warehouse is in BI360
BI360 reporting relies on a curated dataset that usually comes from:

- An ERP connector (Dynamics, NetSuite, QuickBooks, or a custom database)
- A transformation layer (mapping accounts, entities, and dimensions)
- A warehouse refresh schedule

Users experience this as: "reports pull from the BI360 Data Warehouse."

## Connecting an ERP source
**Typical connector workflow**
1. Create a connection profile in BI360 (endpoint, credentials, company selection).
2. Choose which modules to ingest (GL, AP, AR, Projects, Inventory, as applicable).
3. Map source fields into the BI360 staging tables.
4. Run an initial load and validate record counts.

**Support signal**
If users can sign in but see empty reports, validate the connector ran successfully and mappings exist for their entity.

## Live database vs static database
Finance users often ask this as: "Is this real time?"

A practical way to explain it:

- **Live**: reports query the source database directly. Changes appear immediately, but performance and permissions depend on the ERP.
- **Static**: BI360 loads data into its warehouse on a schedule. Reports are fast and consistent, but updates appear only after the next refresh.

Most month-end workflows prefer static because it creates a stable snapshot for reconciliation.

## Refresh cadence and what "not refreshing" means
When a user says "my data is not refreshing", one of three things is usually true:

1. The warehouse job did not run.
2. The job ran but failed on a source step.
3. The job completed, but the report is filtered to a different period or scenario.

**Standard checks**
- Check the last successful refresh timestamp for the dataset.
- Confirm the scheduled job is enabled and has not been paused.
- Confirm the user is viewing the intended entity and period.

## Scheduled jobs (what IT typically owns)
IT teams usually control:
- Job schedules (hourly, nightly, close-specific)
- Job sequencing (load, transform, aggregate)
- Failure notifications

**Close-week recommendation**
- Increase refresh frequency early in the day.
- Freeze refreshes during final tie-out windows to avoid moving targets.
- Communicate the "data as of" timestamp to finance users.

## Connector-specific issues (common patterns)
- **QuickBooks**: authentication tokens expiring, company file selection changes.
- **Dynamics**: security roles limiting access to certain ledgers or dimensions.
- **NetSuite**: API throttling during business hours, requiring off-hours loads.

This demo library treats these as patterns rather than vendor-specific instructions.
