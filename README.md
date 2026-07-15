# Board Deck Review — a Claude skill

Pre-reviews a B2B SaaS board deck **before** it goes to the board, so the board never sees the weak version. Point Claude at your deck (`.pptx`, `.pdf`, `.md`, or pasted text) and it reviews the deck the way your toughest board member would — then tells you exactly what to fix.

## What it checks

1. **Plain language** — flags jargon and buzzwords ("best-in-class", "hypergrowth flywheel") and rewrites them in plain words.
2. **The one-sentence strategy test** — can the product and business strategy be stated in a single meaningful sentence: the customer pain, and how it's solved? If the deck doesn't say it, the review makes that the top fix.
3. **Customer evidence behind product plans** — every roadmap item should answer: how many customers did we talk to, and what did we learn? TAM projections don't count.
4. **Competitive reality** — what are competitors doing, and are we winning or losing against them, with win/loss data. "We have no real competitors" gets called out.
5. **A clear "what" and a real "why" in every section** — sales, churn, financials, team, whatever the meeting needs. "Churn rose because cancellations increased" is a what wearing a why costume, and the review says so.
6. **Accountability** — plan vs. actual on every headline number, consistent metrics with no selective-disclosure games, and closed loops on last meeting's commitments. Bad news early, plainly, with a diagnosis.
7. **Cash clarity** — burn, runway, and the next-raise date math stated plainly, so the board never has to do the subtraction themselves.
8. **The asks** — explicit decisions needed vs. help wanted, each decision decidable from the deck, and discussion topics that match the deck's own biggest problems.

The output is a structured report: a verdict (ready / ready after small fixes / needs revision), a jargon table with rewrites, section-by-section what/why analysis, an accountability-and-cash readout, the questions the board will ask, and a prioritized fix list.

## Install

### Claude Code — from this repo's URL

```
/plugin marketplace add thoughtfulbits/board-deck-review-skill
/plugin install board-deck-review@board-deck-review
```

### Or paste the URL into a Claude chat

Paste `https://github.com/thoughtfulbits/board-deck-review-skill` into Claude Code and ask it to install the skill — it will copy `skills/board-deck-review/` into `~/.claude/skills/`.

### Manual

```bash
git clone https://github.com/thoughtfulbits/board-deck-review-skill.git
cp -r board-deck-review-skill/skills/board-deck-review ~/.claude/skills/
```

### claude.ai

Zip the `skills/board-deck-review/` folder and upload it under **Settings → Capabilities → Skills**.

## Use

> "Our Q3 board meeting is Thursday — review my board deck before I send it. It's at ~/Desktop/q3-board-deck.pptx"

> "Pre-review this board deck like a tough board member. Anything in here that gets us grilled?"

## Repo layout

```
skills/board-deck-review/SKILL.md   # the skill
.claude-plugin/                     # plugin + marketplace manifests (one-URL install)
evals/                              # test decks and eval definitions used to develop the skill
```
