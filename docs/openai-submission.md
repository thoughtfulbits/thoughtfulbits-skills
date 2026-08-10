# OpenAI plugin submission packet

Use this packet to submit the skills-only ZIP produced by:

```bash
./scripts/build-openai-plugin.sh
```

## Listing

- **Name:** ThoughtfulBits Skills
- **Publisher:** ThoughtfulBits Consulting
- **Subtitle:** Review plans, UX, and posts
- **Category:** Business & Operations
- **Availability:** All supported markets
- **Website:** https://thoughtfulbits.ai/board-deck-review
- **Privacy:** https://thoughtfulbits.ai/privacy
- **Terms:** https://thoughtfulbits.ai/terms
- **Support:** https://thoughtfulbits.ai/support
- **Description:** Six rigorous review and editing workflows for B2B SaaS leaders: board-deck audits, board feedback, product-plan and SPARK feature reviews, multi-agent UI/UX testing, and reader-first social post editing.

## Starter prompts

1. Audit the attached board deck before I send it. Identify the few fixes that matter most.
2. Read the attached board deck like a director and give me the concise meeting-room reaction.
3. Edit this social post for a cold audience without changing the facts or my voice.

## Positive tests

### 1. Deep board-deck audit

- **Prompt:** Audit this board deck before it goes to our directors. Recalculate the math, inspect the speaker notes, and give me the few fixes that matter most.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/board-deck-audit/files/lumen_visual_board_excerpt.pptx
- **Expected skill:** `board-deck-audit`
- **Expected result:** A structured verdict that inspects slides and speaker notes, reconciles quantitative claims, grades evidence, anticipates board questions, and prioritizes the necessary changes.

### 2. Concise board feedback

- **Prompt:** Read this like a director the night before the meeting. Does it make sense, and what will the board say in the room? Keep it concise.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/board-deck-audit/files/meridian_q3_board_deck.md
- **Expected skill:** `board-feedback`
- **Expected result:** A one-screen director reaction with the overall read, likely meeting-room reactions, expected questions, and a clear makes-sense verdict without audit tables.

### 3. Full product-plan review

- **Prompt:** Review this FY27 product plan before our offsite. Grade it against the full ThoughtfulBits rubric and tell me where it falls short.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/product-plan-feedback/files/alder_product_plan.md
- **Expected skill:** `product-plan-feedback`
- **Expected result:** A calibrated review that evaluates strategy, customer evidence, constituents, roadmap, metrics, design partners, GTM, positioning, competition, and pricing.

### 4. Partial-roadmap boundary case

- **Prompt:** This is only our H2 engineering roadmap, not the whole company plan. Review it against the product-plan standards that actually apply to its scope.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/product-plan-feedback/files/ridgeline_h2_roadmap.md
- **Expected skill:** `product-plan-feedback`
- **Expected result:** A roadmap-scoped review that does not penalize missing GTM or pricing, while identifying the in-scope automation, measurement, and reliability gaps.

### 5. SPARK feature review

- **Prompt:** SPARK-score this feature spec before we commit the quarter to it. Show the evidence for each dimension and the three simplest improvements.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/product-feature-feedback/files/wren_missed_call_spec.md
- **Expected skill:** `product-feature-feedback`
- **Expected result:** A cited 1-5 score for each SPARK dimension, the correct total and verdict band, a cut list, one delight moment, and three focused improvements.

### 6. Multi-agent UI/UX test

- **Prompt:** Test the account-creation flow in this spec with five independent UI/UX methods. Return the numeric average, critical gate, and loop-ready JSON.
- **Attachment:** https://raw.githubusercontent.com/thoughtfulbits/thoughtfulbits-skills/main/evals/test-ui-ux/files/harbor_account_creation_spec.md
- **Expected skill:** `test-ui-ux`
- **Expected result:** Exactly five isolated method results — SPARK, Nielsen, cognitive walkthrough, PURE, and WCAG 2.2 AA — mechanically averaged to one decimal, with a provisional verdict because a specification is not a live exercised UI.

### 7. Reader-first social post edit

- **Prompt:** Edit this X draft for a cold audience, but keep every fact and make it sound like me: “We reduced the setup form from 14 fields to 4. Early users are finishing it faster, but we have not analyzed the data yet.”
- **Expected skill:** `post-editor`
- **Expected result:** A ready-to-paste post that uses the concrete 14-to-4 contrast, keeps the faster-completion observation qualified, and improves reader value and shareability without inventing data, customer emotion, or a virality promise.

## Negative tests

### 1. Visual redesign request

- **Prompt:** Redesign this sales presentation with a modern visual theme, new illustrations, and polished slide transitions.
- **Expected result:** ThoughtfulBits Skills should not activate because the request is visual production rather than board or product review.

### 2. Fundraising pitch request

- **Prompt:** Rewrite my seed fundraising pitch so it is more persuasive to venture investors.
- **Expected result:** ThoughtfulBits Skills should not activate because an investor pitch is not a board pre-read or one of the supported product-review documents.

### 3. Unrelated writing request

- **Prompt:** Draft a blog post announcing our new office and summer internship program.
- **Expected result:** ThoughtfulBits Skills should not activate because this is blank-page long-form drafting, not editing an existing short- or medium-form social post or running one of the supported reviews.

## Release notes

Version 1.3.1 broadens `post-editor` to short- and medium-form X, LinkedIn, and social-caption drafts. It strengthens cold-reader value, emotional recognition, concrete craft, and evidence-backed shareability while preserving facts, intent, voice, and cultural nuance. The framework explicitly credits Nobunaga, Jonah Berger, and Katherine Milkman. There is still no MCP server, custom UI, external service, or independent data collection.

## Publication checklist

- Verify the publisher identity as **ThoughtfulBits Consulting**.
- Upload the ZIP using the portal's **Skills only** option.
- Upload `assets/openai/directory-icon-light.png` and `assets/openai/directory-icon-dark.png` as the directory icons.
- Upload `assets/openai/composer-icon-light.png` and `assets/openai/composer-icon-dark.png` as the composer icons.
- Confirm all supported markets and English as the listing language.
- Run the seven positive and three negative tests above.
- Published in the [OpenAI Plugins Directory](https://chatgpt.com/plugins/plugins_6a6f44be6a5881919d952d77e2da8080); the final directory URL is linked from the README and website.
