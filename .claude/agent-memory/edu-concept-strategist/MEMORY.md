# Educational Concept Strategist -- Memory

## Project Structure
- Blueprints stored at `projects/<concept-slug>/blueprint.md` (per CLAUDE.md folder structure rule)
- Videos created: `llm-tokens`, `pythagorean-theorem`, `llm-optimization`

## Effective Patterns Discovered

### Opening Hooks for Technical Topics
- **Prediction-and-reveal** works well for topics with counter-intuitive mechanics. Ask the viewer to guess, then show the surprising real answer. Creates immediate curiosity gap.
- For developer audiences, live demos beat abstract intros. Show the tool/output first, explain second.

### Audience: Developer / Tech-Curious Profile
- Assume comfort with: strings, arrays, APIs, basic data structures, JSON.
- Do NOT assume: ML/NLP background, statistics, linear algebra.
- Tone calibration: "senior engineer to smart colleague" -- precise, no hedging, conversational but not dumbed down.
- This audience dislikes over-analogizing. Cap analogies at 2 per short video, up to 3-4 for long-form (10+ min) if each is brief and grounded.
- For long-form: "tech journalist telling a story" tone works well. Narrative momentum matters more than lecture structure.

### Pedagogical Notes
- **Concrete-first, theory-second** is the default strategy for technical explainers. Show the phenomenon, create the question, then teach the mechanism.
- For algorithmic/iterative processes (like BPE), use micro-examples (5 items max) with step-by-step animation. Offer an "escape hatch" summary sentence for viewers who get lost.
- **Side-by-side comparison** is the workhorse visual for "how X differs across systems" segments.
- Always flag scope traps (e.g., BPE vs. WordPiece deep-dive) explicitly in production notes.

### Misconception Handling
- Address the #1 misconception in the opening hook, not in a later "misconceptions" segment. This reframes the viewer's mental model from the start.
- For remaining misconceptions, address each at the moment in the video where it naturally arises, not in a batch.

### Short-Form Videos (60-120s)
- Word budget: ~2.3 words/second for Portuguese narration. 90s = ~210 words max.
- Max 3 learning objectives. Max 5 concept segments.
- Silence is a tool: let key animations breathe for 2-3s without narration.
- Scope discipline is critical. Explicitly list what NOT to include in production notes.
- For math/geometry topics: visual proof ("proof without words") beats algebraic proof for beginner audiences.

### Mid-Form Videos (3-4 min)
- Word budget: ~2.5 words/second for Portuguese narration. 210s = ~540 words max.
- Max 4 learning objectives. Max 6 concept segments.
- One segment can be 2x longer than others IF subdivided into visual steps (e.g., BPE in 3 steps).
- Place the densest segment at position 3 (flanked by concrete segments on both sides).
- Include a "re-energizer" segment after the dense one (surprising examples, flash-card format).
- For scope: cut practical implications before cutting core mechanism -- mechanism is the conceptual heart.

### Audience: Brazilian Secondary Students (12-16)
- Use "voce" (informal). Short sentences (max 15 words).
- Tone: "professor jovem" -- direct, enthusiastic, not childish.
- Define technical terms on first use but DO use proper terminology (cateto, hipotenusa, not dumbed-down substitutes).
- Color-coding is essential for this audience: map concepts to colors and keep them consistent throughout.

### Long-Form Videos (10-15 min)
- Word budget: ~2.5 words/second for Portuguese narration. 780s = ~1,750 words max (reserve ~80s for visual-only moments).
- Max 5 learning objectives. Max 11-12 concept segments.
- Use a 3-act narrative structure (Setup / Transformation / Resolution) for topics with a temporal arc.
- **Clustering technique**: when covering many related concepts (e.g., 9 optimization techniques), group them into 3 clusters of 2-3 items. Go deep on flagship items, montage-pace the rest. Reduces cognitive load from N items to 3 categories.
- Place the deepest/most novel concept slightly past the midpoint (position 6-7 of 11). The audience is warmed up but not fatigued.
- **Dual-track timelines** work well for showing how two forces (e.g., proprietary vs open-source) interact over time.
- For "compounding innovations" stories, use a stacking/layering visual at the end to show how individual improvements multiply.

### Opening Hooks by Type
- **Dramatic quantification** works for economic/trend topics. Show the shocking number first, then promise to explain it. (Used in llm-optimization: $60 -> $0.15 counter.)
- **Prediction-and-reveal** works for counter-intuitive mechanics. (Used in llm-tokens.)

### Scope Management for Dense Topics
- When user requests 9+ subtopics, flag scope concerns proactively. Recommend clustering + depth hierarchy (deep/medium/brief) rather than uniform shallow coverage.
- Always include a "What NOT to include" section in production notes. For dense topics, this section is as important as the content itself.
- Suggest follow-up videos explicitly for topics cut from scope. This reassures the user that cut content is not forgotten.

## Topic Files
- See `technical-explainer-patterns.md` for detailed notes on structuring technical concept videos.
