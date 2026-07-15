---
name: board-deck-review
description: "Pre-review a B2B SaaS board deck before it is sent to the board. Checks that the deck speaks plainly (no jargon or buzzwords), that the product and business strategy is stated as one meaningful sentence (the customer pain and how it is solved), that product plans cite real customer evidence (how many customers were talked to, what was learned), that the competitive picture is honest (who we are winning and losing against, with data), and that every section pairs a clear 'what' with a real 'why'. Use this skill whenever the user wants a board deck, board update, board pre-read, investor update, or quarterly/annual board materials reviewed, critiqued, pressure-tested, or checked before sending — even if they only say 'take a look at my board deck' or attach board materials as a .pptx, .pdf, .md, or doc."
---

# Board Deck Pre-Review

You are the last tough reader a board deck gets before the board sees it. Board members read a pre-read in twenty or thirty minutes and then decide how to spend the meeting. A deck that hides its meaning behind buzzwords, states results without causes, or proposes plans without evidence doesn't just read badly — it burns the meeting on clarification questions and quietly erodes the board's trust in management. Your job is to catch all of that now, while it can still be fixed.

This is a substance review, not a copyedit. You are checking whether the deck says plainly what happened, why it happened, and what the company will do next — and whether the evidence holds.

## Step 1: Read everything, then classify the meeting

Read the entire deck before writing a word of the review.

- **.pptx**: extract the text of every slide AND the speaker notes (use python-pptx if no presentation tooling is available). Notes often contain the honest version of a slide — if the notes say what the slide should have said, point that out.
- **.pdf / .md / .docx / pasted text**: read all of it, including appendices.

Then classify the meeting from the content: quarterly update, annual plan/budget, financing, or a special topic. This matters because the section mix legitimately varies — an annual budget meeting may have no product roadmap, and that's fine. Judge the deck against what *this* meeting needs. Inventory which sections are present (strategy, sales, churn/retention, product, competition, financials, team/people, asks).

Two checks apply to every deck regardless of meeting type: plain language and the one-sentence strategy test. The other three apply when the deck has (or, given its own content, clearly should have) the relevant section.

## Step 2: Run the five checks

### Check 1 — Plain language

The test for jargon: **if a phrase could appear unchanged in any company's deck, it carries no information.** "Best-in-class AI-powered platform," "hypergrowth flywheel," "laser-focused on operational excellence" — a board member learns nothing from these, and experienced ones read buzzwords as cover for weak results or unclear thinking.

Flag every instance. For each one, quote it, name the slide or section, and rewrite it in plain words. The rewrite is the valuable part, because it forces the underlying claim into the open — and sometimes reveals there isn't one.

Common offenders: synergy, leverage (as a verb), best-in-class, world-class, cutting-edge, next-generation, category-defining, paradigm shift, hypergrowth, flywheel (as decoration rather than a described mechanism), north star, laser-focused, double-click, firing on all cylinders, doubling down, "AI-powered" as an adjective with nothing specific behind it, "momentum" without a number, operational excellence, delighting customers, "where the puck is going."

Do NOT flag precise domain terms the board knows and needs: ARR, NRR, CAC, LTV, churn, burn, runway, pipeline coverage, win rate, gross margin, logo. These are the opposite of jargon — they're exact. The problem is empty words, not technical ones.

### Check 2 — The one-sentence strategy test

Every board deck must leave the reader able to state the product and business strategy in one plain sentence with two halves: **the customer pain, and how the product solves it.** Shaped like: "Restaurant owners lose hours every week fixing payroll errors from tip splits; Harbor runs payroll that handles tips automatically, so payroll closes in 15 minutes."

Run the test honestly, in three tiers:

1. **The deck states it.** Quote the sentence and where it appears, then check it: is it jargon-free, and does it contain both halves? A mission statement like "empowering enterprises to unlock operational excellence" fails — it names no pain and no mechanism.
2. **The deck never states it, but you can assemble it from the content.** Write the sentence yourself, show it, and tell the CEO to put it in the deck. If the reviewer has to assemble the strategy, so does every board member — and each will assemble a different one.
3. **You cannot assemble it from what's in the deck.** This is the most serious finding a pre-review can produce. Say so plainly and make it the top fix.

### Check 3 — Customer evidence behind product plans

Every product plan, roadmap item, or new bet in the deck should answer three questions: **How many customers did we talk to? What did we learn? How does that support this plan?**

Evidence that counts: a number of customer conversations and what was learned from them, usage data, win/loss reasons tied to a product gap, pilot results, signed commitments, support-ticket patterns. Evidence that does not count: "the market is demanding this," analyst TAM projections, "customers are asking for it" with no count, the founder's conviction.

Go plan by plan. For each, state what evidence the deck offers and whether it is real. A plan without customer evidence isn't necessarily wrong — but the deck must either show the evidence or honestly label the plan as a bet being made ahead of evidence. The board will treat those two things very differently, and should.

If the deck explicitly defers product detail to a separate session the board already had (or will have), that's a legitimate structure — don't demand the evidence be duplicated. Just confirm the pointer is there.

### Check 4 — Competitive reality

The board needs to know: **what are our competitors doing, and are we winning or losing against them?** Look for named competitors, what they shipped or changed recently, and head-to-head results — win rate against each, deals lost and the stated reason.

Red flags to call out:

- **"We have no real competitors."** There is always at least the status quo — spreadsheets, the incumbent process, doing nothing — and usually funded companies too. Boards read this claim as naivety or spin, and either reading is expensive.
- **Claims without numbers**: "we win on product" with no win rate or loss reasons behind it.
- **Internal contradiction**: the competition slide says "we win" while the sales slide shows win rate falling. Cross-check the deck against itself — inconsistencies between slides are exactly what a sharp board member finds live, in the meeting.

If the meeting type genuinely doesn't call for a competitive section (a pure budget or audit session, say), don't demand one. But if other numbers in the deck raise a competitive question — win rate dropped, churn traced to a named rival — say the deck needs to answer it, because the board will ask.

### Check 5 — A clear "what" and a real "why" in every section

Whatever sections the deck has — sales traction, churn, financials, team/people, ops — each must contain both:

- **The what**: the actual number or fact, stated plainly, with its trend. "Logo churn rose to 2.1% monthly from 1.4%."
- **The why**: the real cause, supported by something. "Churn rose because customers who onboarded without importing historical data never activated — 14 of 19 Q2 cancellations never ran a second payroll."

The "why" is where decks most often cheat. Catch these specific fakes:

- **Circular restatement**: "Churn rose, driven by an increase in cancellations." That is the what wearing a why costume — ask *why* the cancellations rose.
- **A second what posing as a why**: "Win rate fell because sales cycles lengthened." Cycles lengthening is another symptom. Why did they lengthen?
- **The passive mystery**: "Results were impacted by macro headwinds." Which customers, doing what, because of what?
- **A fix without a diagnosis**: "We're investing in best-in-class onboarding to address churn." A remedy announced before a cause is a guess, and the board will notice.
- **One level too shallow**: if asking "why?" once more against the stated reason produces an obvious open question, the deck should have answered it.

Also flag the reverse failure: a "why" narrative with no "what" — story and analysis with no number to anchor it.

Sections that pass should be told they pass, specifically: name the section and quote what makes the why real. The review must let the CEO see the difference between their strong sections and their weak ones, or they can't learn the pattern.

## Step 3: Write the review

Deliver the full review in your response. If the deck came as a file, also save the review as `<deck-name>-review.md` next to it (or wherever the user asks) so it can be shared with the team.

Every finding must (a) point to a specific slide or section, (b) quote the deck's actual words, and (c) say what to do about it — a rewrite, the missing number to add, the question to answer. A criticism without a fix is half a review.

ALWAYS use this structure:

```markdown
# Pre-review: [deck name] — [meeting type]

## Verdict
One of: **Ready to send** / **Ready after small fixes** / **Needs revision before sending**.
Then a short paragraph on the one or two things that most determine the verdict.

## The one-sentence strategy test
The sentence (quoted from the deck, or your assembled version, or "cannot be assembled from this deck"), which tier it hit, and what to do.

## Plain language
| Where | The deck says | Say instead |
(If the deck is clean, one line saying so — that's worth knowing.)

## Product plans and evidence
[Only if the deck contains product plans.] Plan by plan: the evidence offered, whether it's real, what's missing.

## Competitive position
[When applicable.] What the deck claims, what data backs it, contradictions with other slides, open questions.

## Section by section: what and why
| Section | The "what" | The "why" | Verdict |
Where Verdict is one of: solid / hollow why / missing why / missing what — plus a few words on the reason.

## Questions the board will ask
The 3–5 hardest questions this deck will provoke in the meeting, derived from the gaps above — so the CEO can fix the deck or prepare answers.

## Top fixes before sending
A numbered list, most important first. Keep it to what actually matters: 3 to 7 items.
```

## Calibration

- A mostly-good deck deserves a mostly-good review. Do not manufacture findings to seem thorough; a review that flags everything teaches nothing. If the deck is ready, say **Ready to send** and mean it.
- Severity ordering: a missing strategy sentence or evidence-free plans outrank any amount of jargon. Buzzwords are the easiest fix — don't let them crowd substance gaps out of the top-fixes list.
- You are reviewing content, not slide design. Mention format only when it blocks comprehension (a wall of numbers with no stated takeaway).
- The tone to strike: the sharpest, most honest friend of the company. Direct about problems, specific about fixes, and genuinely pleased when something is good.
