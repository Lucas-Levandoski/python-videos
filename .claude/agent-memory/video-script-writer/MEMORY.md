# Video Script Writer -- Agent Memory

## User Preferences
- User provides blueprints as input; scripts must follow blueprint structure exactly
- Uses [VISUAL] annotations (not [B-ROLL]) for Manim-based videos
- Prefers complete script delivery when blueprint is detailed and structure is explicit
- Scripts saved to `<concept-folder>/script.md` per CLAUDE.md conventions

## Project Conventions
- All scripts in Portuguese (Brazil)
- Target pacing: ~2.5 words/second in Portuguese (~150 words/minute)
- Blueprint word budgets are strict -- respect them
- [PAUSE] markers for narrator breathing room, especially in dense segments
- Emphasis with *italics* for words narrator should stress
- No technical jargon beyond what blueprint explicitly allows

## User Production Style (learned from llm-optimization)
- [FACE CAM] markers between every major concept transition -- narrator on camera for breathers/bridges
- Sound design cues: [SFX: impacto grave], [SFX: whoosh transicao], [SFX: impacto unico]
- Music direction throughout: [MUSICA: trocar para X mood], [MUSICA: build tension], [MUSICA: drop]
- Visual transition markers: [TRANSICAO VISUAL: description]
- Pacing: alternate high-energy reveals with calm explanatory sections
- Face cam text should feel natural, conversational, bridging concepts
- Technical terms (quantization, MoE, Flash Attention) stay in English in Portuguese scripts

## Completed Scripts
- `llm-tokens/script.md` -- "Tokens: A Unidade Secreta dos LLMs" (~520 words, 3:30 target)
- `llm-optimization/script.md` -- "Como LLMs Ficaram 1000x Mais Baratos" (~1950 words, ~13 min, 13 segments)
