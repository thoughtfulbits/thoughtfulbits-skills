# OpenAI plugin submission packet

Use this packet to submit the skills-only ZIP produced by:

```bash
./scripts/build-openai-plugin.sh
```

## Listing

- **Name:** ThoughtfulBits Skills
- **Publisher:** ThoughtfulBits Consulting
- **Subtitle:** Review decks and product plans
- **Category:** Business & Operations
- **Availability:** All supported markets
- **Website:** https://thoughtfulbits.ai/board-deck-review
- **Privacy:** https://thoughtfulbits.ai/privacy
- **Terms:** https://thoughtfulbits.ai/terms
- **Support:** https://thoughtfulbits.ai/support
- **Description:** Four rigorous review workflows for B2B SaaS leaders: deep board-deck audits, concise board feedback, product-plan reviews, and SPARK feature reviews.

## Starter prompts

1. Audit the attached board deck before I send it. Identify the few fixes that matter most.
2. Read the attached board deck like a director and give me the concise meeting-room reaction.
3. Review the attached product plan or feature spec and tell me where it falls short.

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

## Negative tests

### 1. Visual redesign request

- **Prompt:** Redesign this sales presentation with a modern visual theme, new illustrations, and polished slide transitions.
- **Expected result:** ThoughtfulBits Skills should not activate because the request is visual production rather than board or product review.

### 2. Fundraising pitch request

- **Prompt:** Rewrite my seed fundraising pitch so it is more persuasive to venture investors.
- **Expected result:** ThoughtfulBits Skills should not activate because an investor pitch is not a board pre-read or one of the supported product-review documents.

### 3. Unrelated writing request

- **Prompt:** Draft a blog post announcing our new office and summer internship program.
- **Expected result:** ThoughtfulBits Skills should not activate because the request is unrelated to board-deck, product-plan, or feature review.

## Release notes

Version 1.1.0 adds native installation in ChatGPT Work and Codex through OpenAI's universal plugin directory while preserving the existing Claude Desktop package. It includes four instruction-only review skills, OpenAI-specific skill metadata, and no MCP server, custom UI, external service, or independent data collection.

## Publication checklist

- Verify the publisher identity as **ThoughtfulBits Consulting**.
- Upload the ZIP using the portal's **Skills only** option.
- Upload `assets/logo.png` as the listing logo if the portal requests it separately.
- Confirm all supported markets and English as the listing language.
- Run the five positive and three negative tests above.
- Publish only after OpenAI approval, then add the final directory URL to the README and website.
