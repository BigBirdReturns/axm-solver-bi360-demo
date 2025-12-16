<!--
title: Consolidations and Intercompany (Entities, Eliminations, and Currency)
origin: Solver BI360 Knowledge Base (synthetic)
origin_id: solver-kb:consolidations:intercompany:v1
license: CC0-1.0
retrieved_from: local
prepared_by: gpt-5.2-thinking
prepared_at: 2025-12-16T21:44:48Z
-->

# Consolidations and Intercompany (Entities, Eliminations, and Currency)

## What consolidation means in BI360 terms
A consolidated financial statement combines multiple legal entities into one set of financials.

Key inputs:
- Entity hierarchy (parent, subsidiaries)
- Ownership percentages
- Intercompany partner mappings
- Currency and translation rules

## Multi-entity reporting setup (high level)
1. Define entity dimension members for each legal entity.
2. Define a hierarchy that reflects consolidation rollups.
3. Ensure each transaction record carries an entity identifier.
4. Validate that the same chart of accounts structure is used consistently.

If any one of these is missing, consolidated reports either double count or omit entities.

## Intercompany eliminations: what users expect
Finance users expect eliminations to remove:
- Intercompany revenue and expense
- Intercompany AR and AP
- Intercompany loans and interest
- Intercompany inventory profit (if tracked)

In practice, the elimination process relies on a consistent partner field, sometimes called:
- Intercompany Partner
- Trading Partner
- Due To / Due From Entity

## Elimination rule pattern (auditable)
A safe elimination rule has three parts:
1. Select transactions where `Entity != PartnerEntity`
2. Post an offset to an elimination entity (or elimination layer)
3. Preserve the original transactions for drill-down, but exclude them from consolidated totals after elimination

This keeps detail auditable while allowing consolidated statements to net to zero for intercompany accounts.

## Currency conversion and translation
Users typically see three currencies:
- Local currency (per entity)
- Reporting currency (group currency)
- Transaction currency (for certain source systems)

A common policy:
- Income statement uses average rate for the period
- Balance sheet uses ending rate
- Equity uses historical rates

## Common support questions
**"Why do eliminations not net to zero?"**
- Partner mapping is missing on one side.
- Transactions are posted to different periods.
- Accounts used by one entity are not flagged as intercompany accounts.

**"Why is one entity missing from the consolidation?"**
- Entity is not included in the hierarchy rollup.
- User security excludes the entity.
- The warehouse load filtered out that company code.
