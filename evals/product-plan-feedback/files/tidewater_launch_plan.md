# Tidewater — Launch Plan

**v4 — July 2026. Approved at the July 20 launch review.**
Owners: Alicia Navarro (CEO), Owen Reyes (CTO), Dana Whitfield (Head of Product), Cole Jarrett (Head of Growth)

---

## 1. Strategy

Residential HVAC companies lose two jobs a day to slow scheduling; Tidewater's AI answers the phone and books the crew's route automatically, so the dispatcher confirms instead of juggles.

That sentence is the test for everything below it. If a workstream does not make the phone get answered or the route get booked, it is not in this launch.

---

## 2. Who we build for

- **Executor: the dispatcher.** She is in Tidewater all day. The product succeeds only if her worst hour — the 7:30–9:00am surge when three lines blink while she re-drags the route board — gets measurably calmer in week one.
- **Beneficiary: the owner.** He rarely opens the app, but he sees the outcome: jobs that used to ring out now show up on trucks, and the first-day replay (Section 4) puts a dollar figure on it.
- **Champion: HVAC ops consultants.** Owners already pay firms like Crosswind Trade Advisors and Toolbelt Ops Group to fix their scheduling. Two consultants sat in on our design-partner onboardings; both now open their engagements with our missed-call audit. They carry us into rooms we could never cold-call.

---

## 3. The problem, evidenced

Between February and May we ran 34 dispatcher ride-alongs across 11 HVAC companies in Florida, Texas, and Colorado. Every ride-along produced the same picture: the dispatcher holding one call, two more on hold, and the route board going stale while she juggles.

We then pulled 90 days of phone logs from nine of the eleven companies — 41,200 inbound calls:

- 26% of business-hours calls went unanswered during peak weeks; 44% after 4:30pm.
- Mystery-shopper callbacks to a sample of 180 missed callers found 58% had booked with a competitor by the end of the same day.
- For the median six-truck company that is 2.3 lost jobs per weekday at a $412 average ticket. The "two jobs a day" in our strategy sentence is measured, not rhetorical.

---

## 4. The product at launch

**Answering.** Tidewater picks up on the first ring, handles diagnosis-adjacent questions from the company's own service history, and quotes arrival windows from live route capacity — not a generic calendar.

**Booking queue with human control.** Nothing goes on a truck without a person. Every AI-booked job lands in the dispatcher's confirmation queue, where she confirms with one tap or overrides the time, tech, or duration. Every override is captured as a labeled correction and fed into weekly model retraining, so each dispatcher is training her own instance. In the design-partner cohort, override rate fell from 22% in week one to 9% by week five.

**The first-day wow.** At 6:00pm on day one, the owner and the dispatcher get a replay: every call Tidewater answered, what each caller needed, and the jobs it booked onto tomorrow's routes, with revenue attached. Two of five design-partner owners forwarded it to other owners unprompted. This moment is engineered — the replay is a launch deliverable with its own owner (Dana), not a byproduct.

---

## 5. Metrics

- **Core activity metric: jobs auto-booked per dispatcher per week, cohort-analyzed monthly** by activation month, reviewed at Monday product review. Current design-partner median: 31.
- **Confirmation rate:** share of queued bookings confirmed within 10 minutes. Target ≥ 85%.
- **Override rate:** healthy band is 5–15%. Below 5% means dispatchers have stopped checking; above 15% means the model is not ready for that shop.
- **Weekly improvement goal:** cut median time from call answered to booking confirmed, week over week, published to the whole team.

---

## 6. Design partners and go/no-go

Five design partners are live: Gulf Wind Air (Tampa), Sundowner Heating & Cooling (Tucson), Front Range Comfort (Loveland), Bayou Air Services (Baton Rouge), and Cedar Peak Mechanical (Boise) — four to fourteen trucks each, chosen for call volume and dispatcher tenure.

**Go/no-go hurdle:** by the end of week 8, at least four of the five partners must have sustained 25+ jobs auto-booked per dispatcher per week for two consecutive weeks, with override rate under 15% in those same weeks. If we miss, GA moves and we fix before we launch. Owen owns the call; decision date is September 4.

---

## 7. Definition of done

Launch does not ship until all of the following hold:

- **Call-path uptime: 99.95% monthly**, measured at the telephony edge. A breach pages on-call within 60 seconds.
- **Answer latency: first spoken word within 1.2 seconds median, 2.5 seconds p95.** Beyond p95, the call auto-forwards to the dispatcher's cell so no caller ever waits on our failure.
- Route writes are idempotent; the double-booking guard is load-tested at 20x expected call volume.
- Fourteen consecutive green days across all five design partners.

---

## 8. Post-launch roadmap (Q4)

- **After-hours mode.** Tidewater answers overnight and stages bookings for the dispatcher's 7:00am queue — nothing confirms until she starts her day. Aimed at the 44% after-4:30pm miss rate; owner sees it as revenue recovered while the shop sleeps.
- **Parts pre-staging.** When a call describes a likely capacitor or blower failure, the booked job carries a suggested parts list the dispatcher can edit; her edits feed the same correction loop as booking overrides.
- **Spanish-language answering.** Requested by three of five design partners; ships behind the same confirmation queue and latency SLOs as English calls.

Each item keeps the launch discipline: dispatcher in control, corrections feeding the model, and a measurable line back to jobs booked.

---

## 9. Go-to-market

Cole's plan for the sell side is built on reach and repetition.

**Target market.** Target market: any business that sends technicians to customers. HVAC is where the product is proven first; the playbook applies anywhere a truck rolls.

**Acquisition.** We will acquire a 50,000-contact email list and run automated outreach sequences, plus AI-personalized LinkedIn DMs at scale. Sequences run seven touches over three weeks; replies route to an SDR for a demo. Distribution is a volume problem, and we intend to win it on volume.

**Content.** Content: AI-generated posts published daily across all channels to maximize impressions. The pipeline drafts, schedules, and publishes without founder time, so output never dips during launch crunch.

**Competitive positioning.** The market is fragmented with no clear leader, so we do not focus on competitors. We tell our own story and let the product speak.

**Pricing.** Pricing: custom quotes; contact sales. Every inbound conversation becomes a discovery call, and quoting deal by deal lets us price to value from day one.

**Marketing success metric:** 1M impressions per quarter.

---

## 10. Timeline

- **Aug 15** — design-partner cohort completes week 8; metrics locked for review.
- **Sept 4** — go/no-go review (Owen). GA date confirmed or moved.
- **Sept 15** — GA: self-onboarding for the booking queue, replay, and retraining loop.
- **Oct 1** — outreach sequences and content pipeline running at full volume (Cole).
- **Nov 10** — first monthly cohort review of jobs auto-booked per dispatcher per week across GA customers (Dana).
