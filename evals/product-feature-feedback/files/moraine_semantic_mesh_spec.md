# Moraine — Adaptive Semantic Mesh

## Product Specification v1.4 — Approved for Build

**Product owner:** Sana Qureshi · **Engineering lead:** Tomas Keller · **Design:** Wes Calloway · **Last updated:** July 21, 2026

---

## 1. Summary

The Adaptive Semantic Mesh is the most ambitious product Moraine has built. It is an enterprise knowledge-graph overlay that connects documents, tickets, and chat into a single, continuously updated semantic layer. Where our current search product indexes content, the Mesh understands it: every document in Google Drive or SharePoint, every Jira and Zendesk ticket, and every Slack and Teams thread becomes a node in a living graph, linked by extracted entities, inferred topics, and organizational context.

We have spent nine months on the underlying entity-resolution research, and the results are strong: 91.4% F1 on our internal cross-source entity benchmark, up from 78.2% a year ago. This spec covers the v1 scope for general availability in Q1 2027.

We pressure-tested the one-line description across three positioning workshops and landed on the following. Mesh: ingests, aligns, harmonizes, and surfaces. That sentence now anchors the website hero, the sales deck, and the demo script.

## 2. Problem statement

Our thesis is that organizations underutilize latent knowledge assets. Knowledge work fragments across an average of 11 SaaS tools per company (Okta 2025 Businesses at Work), and the connective tissue between those tools — who decided what, where the supporting material lives, which ticket relates to which document — exists only in employees' heads. The Mesh makes that connective tissue explicit, queryable, and durable.

## 3. Concept and architecture

### 3.1 Ingestion layer

Connectors at GA: Google Drive, SharePoint, Confluence, Notion, Jira, Zendesk, Slack, Microsoft Teams. Each connector runs incremental sync on a 15-minute cadence with full-crawl backfill on install. Target ingest throughput is 2M objects per tenant per day.

### 3.2 Alignment layer

The alignment layer performs cross-source entity resolution: "A. Chen" in a Jira ticket, "achen@" in Slack, and "Alice Chen" in a Drive doc resolve to one node. Alignment runs on our in-house resolver ensemble and writes candidate edges with confidence scores; edges below 0.72 confidence are queued for admin adjudication in the Mesh Console.

### 3.3 Harmonization layer

Harmonization maps each tenant's content into their organizational ontology — the taxonomy of teams, projects, products, and processes that gives the graph its meaning. Tenants can start from one of four industry ontology templates (software, financial services, healthcare, manufacturing) and customize from there. The ontology editor supports versioning, branching, and rollback.

### 3.4 Surface layer

Three surfaces at GA: the Graph Explorer (interactive visualization), the Mesh API (Cypher-compatible query endpoint), and in-context panels inside Slack and Jira showing the semantic neighborhood of the current ticket or thread.

## 4. Deployment and onboarding

Enterprise knowledge graphs succeed or fail on ontology quality, so we have designed onboarding to be thorough rather than fast. For each tenant, onboarding includes two taxonomy workshops and a six-week ontology-alignment phase, led by a Moraine solutions architect working with the customer's knowledge-management owner. During alignment we iterate on the tenant ontology against a sample corpus until harmonization precision exceeds 85% on a 500-object labeled sample.

To keep graph quality high after handoff, administrators complete a certification module before rollout. The module is roughly four hours of self-paced material covering ontology stewardship, edge adjudication, and connector hygiene, with a 20-question assessment at the end. Ines Fontaine's customer-success team owns the curriculum and will certify the first cohort of design-partner admins in October.

## 5. Research notes

Between March and June, Sana and our two sales engineers ran discovery conversations with prospects in our target segment (500–5,000 employees, knowledge-heavy industries). Summary of findings, from the April 30 research readout:

- Prospects consistently confirmed tool fragmentation: the median prospect reported content spread across 9 systems.
- In 12 discovery calls, no prospect described this problem unprompted; 9 of 12 asked us to explain what the product does. We view this as an education gap typical of category-creating products, and it confirms the need for the analyst-relations and content program Marketing has scoped for Q4.
- Once walked through the demo storyboard, 7 of 12 prospects agreed a unified semantic layer "would be useful" for onboarding new employees and for compliance discovery.
- Two prospects asked whether the Mesh could replace their existing enterprise search contract; we believe the answer will be yes by v2.

These calls sharpened our conviction that the category needs a defining product, and that we are furthest along in building it.

## 6. Demo plan

The centerpiece of our launch demo is the Graph Explorer visualization: a force-directed rendering of the customer's own knowledge graph, animating from an empty canvas to 50,000 nodes in about 40 seconds as connectors backfill. At our internal demo day on June 12, the visualization drew a spontaneous round of applause from the go-to-market team. Wes's team is polishing the animation easing and node-clustering colors for the launch build. The demo script runs 25 minutes end to end.

## 7. Reliability and rollout

Tomas's team has committed to the following service levels for GA:

- **Ingestion pipeline uptime:** 99.5% monthly, measured per connector.
- **Query latency:** p95 ≤ 700ms for two-hop neighborhood queries on graphs up to 10M nodes.
- **Freshness:** 95% of source changes reflected in the graph within 30 minutes.

Connector syncs retry with exponential backoff (three attempts, then dead-letter queue). The DLQ is reviewed daily by the on-call engineer, and objects that fail three consecutive sync cycles raise a PagerDuty alert. If a source API rate-limits us mid-crawl, the sync checkpoints and resumes on the next scheduled run. If entity resolution produces a bad merge, admins can split the node in the Mesh Console and the correction propagates to downstream edges within one sync cycle.

Rollout proceeds in three stages: internal dogfood on Moraine's own workspace (August), three design partners (September–November), then GA (Q1 2027). Each stage has a go/no-go review against the SLOs above. Runbooks for the twelve most common connector failure classes are drafted and will be exercised during dogfood.

## 8. Success metrics

- 10M+ nodes ingested per design partner by end of November.
- 40% of licensed seats issuing at least one Mesh query per week by GA + 90 days.
- Harmonization precision ≥ 85% sustained post-handoff.
- Admin edge-adjudication queue under 200 items per tenant per week.

## 9. Pricing and packaging

Platform fee model, priced per connected source system plus a per-seat component. Finance is modeling tiers against a target ACV of $76K; final pricing lands in September.

## 10. Timeline

- **August:** Dogfood begins; certification curriculum finalized.
- **September:** Design partner 1 onboarding starts (taxonomy workshops week 1).
- **November:** Design partner go/no-go against SLOs.
- **January 2027:** GA launch with Graph Explorer demo as the centerpiece of our field event in Austin.

The team is proud of this one. It is the product we set out to build when we founded Moraine, and the craftsmanship shows at every layer of the stack.
