# Ridgeline — H2 2027 Roadmap

**Engineering planning doc. Owner: Elena Marsh, VP Engineering. Last updated: July 6, 2027.**

Scope: roadmap only. ICP, pricing, competition, and go-to-market are owned by the commercial plan (separate document).

Ridgeline is CI and build tooling for engineering teams. Our job in H2 is simple to state: make builds fast to start, fast to run, and boring to operate. This document covers what engineering will ship between July and December 2027, why each item made the cut, and how we will know it worked.

---

## How we chose these items

Three inputs: H1 support-ticket analysis (2,900 tickets, tagged by Noor's team), quarterly interviews with 18 customers across our design-partner council, and product analytics. The four largest pains, in order: onboarding friction (34% of H1 trials never reached a first green build; 61% of onboarding tickets were pipeline-config syntax questions), triage toil on failed builds (team leads at our 20 largest accounts spend a measured average of 6.5 hours/week routing failures), flaky tests blocking merges, and slow builds on large monorepos (9 of the 18 interviewed customers named build duration their top complaint).

## Operating metric

Activation is the number we manage weekly: the percentage of new workspaces that reach a first green build within 24 hours. It sits at 58% today. Noor Haddad runs a Monday activation review, and our standing goal is to improve the activation rate every week in H2, with each initiative below expected to contribute and every experiment logged against the weekly number.

---

## Roadmap

### 1. Zero-barrier onboarding (July–September)

**Owner:** Noor Haddad.
**Goal:** first successful build in under 5 minutes, no docs required.
**What we're building:** repo auto-detection for the 12 most common language/framework stacks, generated pipeline config with working defaults, and a guided first run that surfaces the green build in the browser.

- **Developer value:** paste a repo URL and get a passing pipeline without reading a single page of configuration reference.
- **Engineering-leadership value:** new teams onboard without burning a platform engineer's week on setup, and trial rollouts across an org stop stalling at the config step.

**Definition of done:** GA for all 12 stacks; setup service holds a 99.9% availability SLO with config generation p95 under 30 seconds.
**Success criteria:** median time-to-first-green-build under 5 minutes; trial activation from 58% to 75% by October 31.

### 2. Build-failure auto-triage (August–November)

**Owner:** Devon Achebe.
**What we're building:** a classifier that reads each failed-build report — logs, blame data, code ownership — determines the owning team, and routes the issue. Auto-triage will assign every incoming issue automatically.

- **Developer value:** no more Monday triage rotation; a failure lands in the right team's queue while the stack trace is still warm.
- **Engineering-leadership value:** the 6.5 hours/week of team-lead routing work is reclaimed, and mean time-to-owner becomes a number you can put on a dashboard instead of a shrug.

**Definition of done:** assignment within 60 seconds of issue creation at p95; triage service holds a 99.5% availability SLO.
**Success criteria:** mean time-to-first-response on failed builds from 9 hours to under 1 hour at the 20 largest accounts; team-lead triage hours to under 1 per week.

### 3. Flaky-test quarantine (September–December)

**Owner:** Ingrid Sato.
**What we're building:** statistical flake detection over retry history, automatic quarantine so a flaky test stops blocking merges the same day it starts flaking, and a quarantine dashboard with per-test history and one-click un-quarantine — every un-quarantine is fed back as a labeled correction to the flake detector.

- **Developer value:** a red pipeline means your change broke something, not that the same network-dependent test rolled the dice again.
- **Engineering-leadership value:** the platform team stops fielding "CI is red but nothing is broken" pages, and merge-queue throughput stops degrading unpredictably during release weeks.

**Definition of done:** quarantine decision p95 under 2 hours from first flake signal; quarantine service holds a 99.9% availability SLO.
**Success criterion:** developers are happier.

### 4. Remote build cache for monorepos (October–December)

**Owner:** Tomás Rivera.
**What we're building:** a shared, content-addressed remote cache, warm across CI and local development, for our monorepo customers — whose median build currently runs 14 minutes.

- **Developer value:** incremental builds locally and in CI; you stop paying for your teammate's already-compiled work.
- **Engineering-leadership value:** compute spend per build drops an estimated 35–40%, and merge-queue wait becomes predictable enough to plan release trains around.

**Definition of done:** cache read p99 under 150 ms in-region with a 99.95% availability SLO; a cache miss always falls back to a full build, never a failed one.
**Success criteria:** median monorepo build under 6 minutes; cache hit rate above 80% by December 31.

---

## Sequencing and capacity

24 engineers across three pods. Onboarding and auto-triage are staffed from the Pipeline pod (9 engineers), quarantine and the remote cache from the Runtime pod (10), and the Platform pod (5) holds 20% of total capacity in reserve for on-call, reliability work, and small fixes. No item depends on hiring beyond the two backend roles already open and budgeted.

## Feedback loop

Every initiative ships to a five-customer design-partner group before GA. We run monthly partner calls, and each pod reviews partner-reported issues in its weekly planning. GA requires at least four of the five partners live on the beta for 30 days.

## Deliberately not in H2

Self-hosted runner GA (stays in beta), Windows worker expansion, and the pipeline-editor redesign. Each was weighed against the four pains above and deferred to H1 2028 planning in November.
