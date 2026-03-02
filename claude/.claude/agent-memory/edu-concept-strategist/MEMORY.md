# Educational Concept Strategist -- Memory

## Project Structure
- Blueprints are stored in `/mnt/c/Users/lucas/source/repos/videos/claude/blueprints/{topic-slug}/teaching-blueprint.md`
- First blueprint created: `llm-tokens`

## Effective Patterns Discovered

### Opening Hooks for Technical Topics
- **Prediction-and-reveal** works well for topics with counter-intuitive mechanics. Ask the viewer to guess, then show the surprising real answer. Creates immediate curiosity gap.
- For developer audiences, live demos beat abstract intros. Show the tool/output first, explain second.

### Audience: Developer / Tech-Curious Profile
- Assume comfort with: strings, arrays, APIs, basic data structures, JSON.
- Do NOT assume: ML/NLP background, statistics, linear algebra.
- Tone calibration: "senior engineer to smart colleague" -- precise, no hedging, conversational but not dumbed down.
- This audience dislikes over-analogizing. Cap analogies at 2 per video; use them for abstract concepts only.

### Pedagogical Notes
- **Concrete-first, theory-second** is the default strategy for technical explainers. Show the phenomenon, create the question, then teach the mechanism.
- For algorithmic/iterative processes (like BPE), use micro-examples (5 items max) with step-by-step animation. Offer an "escape hatch" summary sentence for viewers who get lost.
- **Side-by-side comparison** is the workhorse visual for "how X differs across systems" segments.
- Always flag scope traps (e.g., BPE vs. WordPiece deep-dive) explicitly in production notes.

### Misconception Handling
- Address the #1 misconception in the opening hook, not in a later "misconceptions" segment. This reframes the viewer's mental model from the start.
- For remaining misconceptions, address each at the moment in the video where it naturally arises, not in a batch.

## Topic Files
- See `technical-explainer-patterns.md` for detailed notes on structuring technical concept videos.
