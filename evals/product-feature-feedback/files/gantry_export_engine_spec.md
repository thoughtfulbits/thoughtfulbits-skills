# Gantry — Feature Spec: Ledger Export (v1)

**Owner:** Sofia Brandt, Engineering Lead, Data Platform
**Reviewers:** Marcus Webb (VP Engineering), Dana Ortiz (Head of Enterprise Sales), Tom Feld (Compliance)
**Status:** Approved for build — targeting GA October 15
**Last updated:** July 22, 2026

---

## 1. Why now

Gantry runs payroll for 3,900 companies. Enterprise (500+ employees) is where our 2026 growth plan lives, and every enterprise evaluation now includes the same requirement: an audit-grade export of payroll ledger data that the customer's auditors will accept without manual reconciliation.

- **14 open enterprise deals are blocked on this feature.** Combined first-year contract value: $2.6M. Dana's team tracks each one; nine name Ledger Export as the sole remaining blocker.
- **Auditors require it.** Big Four and regional audit firms ask for period-complete, immutable ledger extracts with a manifest they can tie to our SOC 1 report. Screenshots and ad-hoc CSVs assembled by support do not pass.
- **Customers say it plainly.** Beacon Staffing (2,400 employees, in contract review): "we need this to pass our audit". Their fiscal year closes January 31; we must be live by mid-October so they can run a parallel test in November.

Today "export" means a support ticket and a 3–5 day turnaround while a data engineer hand-runs queries. Q2: 61 such tickets, roughly 9 hours of engineering time per week.

## 2. What it is

One sentence: Export: selects and delivers.

The admin selects an entity, a date range, and a data set (payroll register, GL summary, tax remittance detail, or all three); Ledger Export delivers a period-complete, checksummed extract to their configured destination (S3, SFTP, or direct download).

First export completes in under two minutes without documentation. We validated the flow with five pilot admins on a clickable prototype; all five completed an export unaided, median 1m 25s. There is nothing to learn: three selections and a Run button.

## 3. Reliability is the feature

An export that might be incomplete is worse than no export — an auditor who catches a missing pay run once will never trust our extracts again. We are building this the way we built the pay engine.

### 3.1 Failure modes and preventions

| Failure mode | Prevention |
|---|---|
| Partial export (job dies mid-write) | Write to staging; atomic publish only after row count and checksum reconcile against the source ledger snapshot. Nothing partial is ever visible to the customer. |
| Schema drift (ledger migration breaks column mapping) | Versioned export schema contract; CI fails any ledger migration that does not ship a matching export-mapping update. Nightly contract test against production schema. |
| Credential expiry (customer S3/SFTP credentials go stale) | Credentials validated at configuration time and re-validated 24 hours before each scheduled run; expiry warning to the admin 7 days out; a failed delivery parks the completed file for 30 days rather than discarding it. |
| Large-file timeout (500K+ row extracts) | Chunked, resumable writes with per-chunk checksums; no single request exceeds 60 seconds; tested to 2M rows in the load environment. |

### 3.2 Idempotent retries

Every export job carries a client-supplied idempotency key. Retries — ours or the customer's — return the original artifact, never a duplicate or a re-computed variant. Re-running an export for a closed period is guaranteed byte-identical. This is what lets an auditor reproduce a number six months later.

### 3.3 Chaos-test plan

Two weeks before GA we run a scheduled chaos suite in staging: kill the worker mid-write, revoke destination credentials mid-delivery, inject a ledger schema migration during an active export, and drop the network for 30 seconds at random offsets. Exit criterion: zero partial artifacts visible and zero silent failures across 500 injected-fault runs. Marcus signs off on the results personally.

### 3.4 Definition of done

p95 export completion under 5 minutes at 100K rows; ≥99.5% export success; zero silent partial exports

Every failed export pages the on-call and emails the customer admin a plain statement of what happened and when we will retry.

## 4. Scope and v1 interface

The v1 UI is a configuration form. Formatting and presentation polish are out of scope for v1. Entity picker, date-range picker, data-set checkboxes, destination dropdown, Run button. On completion the admin receives a notification email containing a link to the CSV. That is the entire surface.

Out of scope for v1: scheduling UI (API only), XLSX or PDF output, column customization, in-app export history beyond 90 days.

## 5. Pricing and packaging

Included in the Enterprise tier; no new SKU. Dana's read: this unblocks the 14 deals and removes the top objection in enterprise security reviews.

## 6. Milestones

- **Aug 8** — schema contract frozen; export mapping enforced in CI
- **Sep 5** — staging end-to-end with pilot design partners (Beacon, Coastline Foods)
- **Sep 26** — chaos suite passes exit criterion
- **Oct 15** — GA

## 7. Risks

- Beacon's parallel test slips if we miss October 15; their audit window does not move. Mitigation: design-partner staging access from September 5.
- Tax remittance detail has state-by-state edge cases; Tom's team is enumerating them by August 15.

We believe this is the most rigorously specified feature Gantry has shipped. The pay engine earned enterprise trust by never being wrong; Ledger Export will earn auditor trust the same way.
