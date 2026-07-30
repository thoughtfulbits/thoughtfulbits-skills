# Alder — FY27 Product & GTM Plan

Prepared for the January planning offsite. Owners: Maya Lindqvist (CEO), Leo Tran (Product), Jenna Cole (GTM), Dan Brewer (Engineering). Everything below rolls up to the strategy sentence.

---

## 1. Strategy in one sentence

Franchise restaurant groups lose 2-4% of food spend to supplier invoice errors they never catch. Alder reads every invoice, checks it against contract prices and delivery history, and flags overcharges for the bookkeeper to approve — so a 40-location group recovers money every week without adding headcount.

We have read this sentence to operators, bookkeepers, and investors. Nobody has asked us to explain it twice.

---

## 2. What we know about the problem

Since June we have run 62 discovery calls with franchise operators, controllers, and bookkeepers. 48 of the 62 named invoice errors as a top-three pain — ahead of scheduling and hiring in most calls. 31 already pay a manual audit service, typically a contingency-fee recovery firm that samples invoices quarterly and keeps 25-35% of what it finds. The pain is known, prioritized, and already monetized by inferior solutions; our job is to be an order of magnitude faster and cheaper than the incumbent behavior, not to convince anyone the problem exists.

The most common failure mode we heard: the price on the invoice quietly diverges from the negotiated contract price, line by line, vendor by vendor, and no one has time to check 400 invoices a week against a contract PDF.

---

## 3. Constituents

We build for three people, and every roadmap item below names what it does for each.

- **Executor — the bookkeeper.** She approves or rejects every flag Alder raises. Alder never posts an adjustment or files a claim without her explicit approval; her judgment is the product's control loop.
- **Beneficiary — the owner/CFO.** He sees recovered dollars in a monthly report. He does not log in daily and should not have to; the product must prove value to him on a monthly cadence without his effort.
- **Champion — fractional-CFO firms.** They serve 5-30 restaurant groups each and are trusted advisors on exactly this problem. We are launching a partner program to arm them: co-branded recovery audits, a revenue share, and partner API access so they can run Alder across their whole book of clients.

**Ecosystem.** Alder sits on top of QuickBooks and Sage for accounting, ingests delivery data from the major restaurant POS systems (Toast first), consumes supplier EDI feeds where vendors offer them, and exposes a partner API for the fractional-CFO firms and other tools in the operator's stack.

---

## 4. Why now, and why it compounds

Two curves make this plan possible this year and not two years ago.

**The cost curve.** The cost of running a document-extraction model over a scanned invoice fell roughly 8x in 18 months — from about $0.40 per invoice to under $0.05. At the old price, per-invoice extraction broke our unit economics below the enterprise tier; at the new price we can profitably process every invoice for a 10-location group on a credit-card plan. The plan explicitly rides this curve: our COGS model assumes a further 2x decline by year-end, and if it materializes we widen the free audit rather than pocketing the margin.

**The data flywheel.** Every invoice we process feeds an anonymized vendor-price benchmark: what other groups in the network paid for the same case of chicken thighs that week — today our six design partners, wider with every group we add. In design-partner data, flags backed by benchmark evidence get approved by bookkeepers at nearly twice the rate of contract-only flags, because every new customer's invoices make the benchmark sharper for every existing customer. This is the compounding loop the company is built around, and it is also our content engine (Section 8).

---

## 5. FY27 roadmap

Each item states its value to the executor and to the beneficiary.

1. **Approval queue v2.** Every accept/reject the bookkeeper makes retrains the flagging model; her corrections are training data, not exhaust. *Executor:* fewer false flags every week, with a keyboard-first review flow that clears a morning's flags in minutes and a one-click invite that brings the controller or a second bookkeeper into the review queue. *Beneficiary:* rising precision means rising recovered dollars without rising review time.
2. **Proactive weekly price-drift alerts.** Alder watches contract-vs-invoice drift per vendor and alerts before the drift becomes a quarter of overcharges. *Executor:* she opens the week knowing which two vendors to watch. *Beneficiary:* creeping vendor increases surface in weeks, not at the annual contract renegotiation.
3. **Agent-callable API.** Every capability in the app is exposed through an API designed to be called by AI agents as well as humans. *Executor:* her firm's own automations and assistants can query flags, approve within policy, and pull evidence. *Beneficiary:* recovered-dollar data flows into whatever reporting stack the group already runs.
4. **Monthly owner report as a shareable artifact.** A designed, one-page report of dollars recovered, top offending vendors, and benchmark position. *Executor:* generated in one click, no spreadsheet assembly. *Beneficiary:* a monthly proof of value he can forward to franchisees, partners, and his bank — each forward is also distribution for us.

**First-run experience.** A new customer connects QuickBooks and sees their first flagged overcharge within 15 minutes. The designed wow: on first run, Alder scans the last 90 days and surfaces duplicate payments — money the group already lost and can recover this week, before any contract data has been loaded. Six of six design partners audibly reacted to this moment; it is engineered, not incidental.

**Reliability.** We ship with SLOs, not aspirations: 99.9% invoice-ingestion success and sub-60-second processing per invoice at p95. A reliability dashboard covers both server-side SLOs and client-side experience (page-load and approval-queue latency as the bookkeeper actually experiences them), reviewed weekly by engineering.

---

## 6. Metrics

- **Weekly improvement goal:** flag approval rate (share of flags the bookkeeper approves) improves +2% week over week until it plateaus above 85%. This number is reviewed every Monday; when it stalls, the model team's queue reorders around it.
- **Activity metric:** invoices approved per bookkeeper per week, tracked in monthly cohorts so we can see whether the January cohort engages more deeply at week 8 than the October cohort did.
- **Reliability:** the dashboard above, with SLO breaches paged, not filed.

---

## 7. Design partners and feedback loops

We have 6 signed design partners: franchise groups between 12 and 55 locations across QSR and fast-casual. Our go/no-go is written down and pre-agreed: by end of Q1, at least 4 of 6 partners recovering ≥$2,000/month, or we pause expansion hiring. We meet each partner biweekly for structured interviews, and we instrument the product with automated in-product feedback — funnels and heatmaps on the approval queue and first-run flow — so we learn from what partners do, not only what they say.

Beyond the partners: every sales and CS call is transcribed and AI-analyzed to rank unmet needs by frequency and revenue at stake, with a readout every two weeks, shared between product and GTM so both teams argue from the same list.

**Internal operations.** Product, sales, and CS hold a weekly triage on the top-ranked needs and open escalations. Support is trained on every launch two weeks before it ships, with a dry-run against the design partners' real data.

---

## 8. Go-to-market

We model the journey as awareness → entering orbit → engaged → sales funnel, and we run two motions: self-serve with a credit-card tier for smaller groups, and a sales-led motion for multi-location groups where procurement and a fractional CFO are in the room.

**ICP:** 10-80 location US franchise groups on QuickBooks. Named, narrow, and the only segment sales is paid on this year.

**Competition (top 5):**

| Competitor | What they are | How we beat them |
|---|---|---|
| Manual audit firms (the status quo) | Contingency-fee recovery shops sampling invoices quarterly | We check every invoice within a minute of receipt, not a quarterly sample, and cost a fraction of a 30% contingency |
| MarginHawk | AP automation with an error-flagging add-on | They optimize for paying invoices fast; we optimize for recovering dollars, with contract-price and delivery-history matching they lack |
| PlateAudit | Food-cost analytics for independent restaurants | Analytics describe the loss; we recover it, and we are built for multi-entity franchise accounting from day one |
| Invosense | Enterprise invoice matching for grocery and c-store chains | Their six-month, $100K+ implementations exclude our ICP; we onboard in 15 minutes at credit-card prices |
| Quartermast | Horizontal spend-management suite | No supplier catalog, no delivery matching; we win every head-to-head where food-spend depth is tested |

We also track what operators ask ChatGPT or Claude when invoice costs spike; today those answers recommend spreadsheet templates and audit firms, and our benchmark report is built to become the citable answer. We embrace the do-it-yourself path rather than fight it: the free audit ships with our own reconciliation spreadsheet template, offered openly, so DIY operators start on Alder's template and graduate to the product.

**Pricing page:** three tiers, each stated as value, not features. A free 30-day audit ("find out what you lost last quarter — keep the report either way"), a credit-card tier at $99 per location per month ("every invoice checked, every week, no procurement meeting required"), and an enterprise tier ("multi-entity rollups, supplier EDI, partner API, and a named CSM").

**Most-significant metrics, one per funnel stage:** awareness — weekly food-cost benchmark-report subscribers; entering orbit — free-audit completions; engaged-to-close — paid conversions. Nothing else goes on the GTM dashboard.

**Content engine.** The weekly food-cost benchmark report, built from real anonymized platform data, is the authentic self-marketing engine: operators subscribe because the numbers are useful on their own, and every issue demonstrates the exact capability we sell. No purchased lists, no automated outreach sequences.

Community: we will explore an operators' community in H2.

---

## 9. Bets beyond the plan

**Supplier-side financing.** Once we hold verified invoice and payment histories, offering suppliers early-payment financing is a plausible second act, and two design partners' vendors have asked about it unprompted. We are staffing half an engineer and one BD lead to explore it in Q1. This is a bet ahead of evidence; proof point: 5 signed LOIs by March. If the LOIs do not materialize, the exploration ends at the quarter boundary and the headcount returns to the core roadmap.
