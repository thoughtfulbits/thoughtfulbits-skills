# Wren — Feature Spec: Missed-Call Rescue

**Author:** Priya Shah, Head of Product
**Reviewers:** Dan Kowalczyk (Engineering Lead), Rosa Delgado (Compliance), Dr. Amrit Gill (Clinical Advisor)
**Status:** Ready for build — targeting September 8 design-partner GA
**Date:** July 28, 2026

---

## One sentence

When a call to the clinic rings out, Wren texts the caller back within seconds, holds the conversation, and books the appointment directly into the practice-management system — before the front desk is even off the other line.

Every feature we ship has to survive the naming test first: one noun, two verbs, nothing else. Rescue: catches and books. If we can't say it that way, we don't build it.

## Setup

Setup is one conditional call-forwarding change (forward-on-no-answer) from the clinic line to the clinic's Wren number, made from the phone the office manager already uses. No software install, no new login, no training session. The activation bar we hold ourselves to: first rescued call within two minutes of setup, no documentation needed. All three design partners cleared it on their first attempt; the median was 1 minute 40 seconds from starting the forwarding change to Wren's first outbound text.

## The problem, in numbers

From 90 days of call logs across 21 customer clinics (just over 40,000 calls):

- Clinics miss 22% of inbound calls.
- 38% of missed calls are appointment-seeking. The average booked visit across these clinics is $470, so each missed call is worth roughly $180 in bookings.
- 41% of missed calls arrive when the desk is dark: lunch, evenings, Saturdays.
- 74% of missed callers leave no voicemail. They call the next practice on the map.

## Three outcomes the clinic gets paid for

**1. Recovered booking revenue.** In a four-week prototype run at our three design partners, Wren texted back 412 missed calls, held 269 conversations (65% reply rate), and booked 118 appointments worth $55,460 in scheduled visit value — about $4,600 per clinic per week.

**2. After-hours capture.** For the average clinic in our logs (640 calls and 140 missed per month), the 41% of misses outside desk hours are 58 calls a month, roughly $10,400 in at-risk bookings that today go to voicemail or a competitor. Wren answers these by text with no staffing change.

**3. Front-desk time back.** Owners in our interviews estimated 5–8 hours a week of manual callbacks and phone tag; at the midpoint (6.5 hours) and a $26/hour loaded front-desk cost, that is roughly $730 a month in labor, before counting the checkout-counter interruptions it eliminates.

We will price Missed-Call Rescue at $299/month as an add-on. Each outcome independently covers the price, and 28 of the 40 owners we interviewed already pay roughly $400/month for an after-hours answering service that takes messages and books nothing.

## Moments we designed on purpose

**First-day recap.** At 6:00 p.m. on day one, the owner gets an email summarizing what happened while they were chairside. The pilot version reads: "Wren rescued 6 calls and booked 3 appointments while you were with patients", with each line linking to the full conversation transcript. The first-day recap email is currently plain text; design polish is scheduled post-launch.

**Live rescue toast.** When Wren books mid-day, a toast slides into the dashboard the front desk already has open: "Rescued: Maria G., cleaning, Thu 2:10 p.m." Staff watch saves land in real time.

**Monthly recovered-revenue statement.** A one-page statement of dollars recovered, bookings kept, and after-hours saves — designed for the owner to hand to their practice partner. Design partners asked for extra copies unprompted.

## Failure modes and preventions

| Failure mode | Prevention |
| --- | --- |
| Texting a wrong number | Wren only texts numbers that called the clinic line within the previous 10 minutes, and the first message names the clinic and the missed call ("This is Larkspur Dental — sorry we missed you just now"). |
| Double-booking | Bookings write through the practice-management system's live availability, with a conflict re-check immediately before confirmation; if the slot is gone, Wren offers the two nearest alternatives. |
| TCPA / opt-out | Every first message identifies the clinic; texts are sent only in response to a call the patient placed; STOP is honored instantly and the number is permanently suppressed across all Wren features. Reviewed and signed off by Rosa Delgado (TCPA and HIPAA; Wren operates under a BAA with each clinic, and conversation transcripts are stored and access-logged accordingly). |
| Quiet hours | No outbound texts between 9:00 p.m. and 8:00 a.m. clinic-local; late-night missed calls queue and send at 8:01 a.m. |
| Clinical questions or emergencies | Wren never answers clinical questions; pain or emergency keywords trigger an immediate priority alert to the front desk and the caller is given the clinic's emergency line. |

Definition of done for launch: reply within 60 seconds p95; booking-conflict rate under 0.5%. Reply p95 is measured on sends outside quiet hours; conflict rate is double-bookings divided by total Wren bookings, reported weekly. Ship gate: two consecutive green weeks on both numbers at all three design partners before the flag opens.

## Evidence

We ran 40 clinic-owner interviews between March and May 2026 across 11 states, practices from one to six operatories. 34 of 40 named missed calls unprompted as a top-three front-desk problem before we described the feature. In the prototype walk-throughs, 31 of 40 owners said words to the effect of 'can I have this today?' before we reached the pricing slide. Dr. Nia Okafor of Larkspur Dental (Columbus), a design partner, told us: "The Tuesday it went live, it booked a new patient while I was in a 9 a.m. crown prep."

## Scope and build

Two engineers, six weeks, shipped behind a per-clinic flag. v1 is English SMS with write-through booking for the three practice-management systems that cover 89% of our base. Explicitly out of v1: Spanish conversations (Q4), insurance-verification questions (Wren hands these to the front desk as a task with a summarized transcript). Rollout: design partners September 8, full base October 6 if the ship gate holds.
