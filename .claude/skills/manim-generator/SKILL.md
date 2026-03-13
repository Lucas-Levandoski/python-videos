---
name: manim
description: Use this skill whenever the user wants to create, generate, or animate a mathematical or educational video using Python Manim. Trigger on requests like "create a manim animation", "make a manim scene", "visualize this math concept", "animate this with manim", "generate a manim video", or any time the user describes a mathematical concept they want to see as an animated video. Also trigger when the user asks to render or build a .mp4 from a manim script.
---

# Manim Code Generator

This skill handles all requests to create mathematical animations and educational videos using the [Manim Community Edition](https://docs.manim.community/) library.

## What it does

Delegates the full request to the `manim-scene-builder` subagent, which:

1. Writes a clean, well-structured Manim Python scene script
2. Renders it to an `.mp4` file via the Manim CLI
3. Reports the output file path and any notable animation decisions

## Mandatory folder structure

Before delegating to the agent, derive a concept slug from the user's request (lowercase, hyphenated, e.g. `pythagorean-theorem`). All output **must** go inside `../videos/<concept-name>/` (relative to the `claude/` working directory, i.e. the repo root `videos/` folder).

```
videos/
└── <concept-name>/
    ├── blueprint.md    ← pedagogical blueprint
    ├── script.md       ← narrator script (Portuguese)
    ├── main.py         ← Manim scene file
    └── main.mp4        ← rendered video
```

Include this rule explicitly in every prompt sent to the `manim-scene-builder` agent.

## How to invoke

Use the Agent tool to launch the `manim-scene-builder` subagent. Pass the user's full request as the task prompt, preserving all details about:

- The mathematical concept or topic to animate
- Target audience or complexity level (if mentioned)
- Desired quality or length (if mentioned)
- Any specific visual style, color, or layout preferences
- **The concept folder path**: `../videos/<concept-name>/` — the agent must write `main.py` there

## Example delegation prompt

```
Create a Manim animation that visually explains the Pythagorean theorem.
Show a right triangle with labeled sides a, b, and c. Animate squares
growing from each side and demonstrate that the area of the two smaller
squares equals the area of the largest square. Use a clean, beginner-friendly
style with blue for the triangle and yellow highlights for key steps.

IMPORTANT: Save the scene file to ../videos/pythagorean-theorem/main.py.
The scene class must be named Main. Render to 1080p.
```

## Key conventions for the manim-scene-builder agent

- Scene class is always named `Main` (matches VS Code build task and CLAUDE.md convention)
- Python file is always `main.py`, saved to `../videos/<concept-name>/main.py`
- Use `-qh` flag for 1080p (default), `-pql` for fast test renders
- `MathTex` for LaTeX expressions, `Text` for plain text
- Standard color coding: `BLUE`/`WHITE` for primary, `YELLOW` for highlights, `RED` for warnings, `GREEN` for results
