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

## How to invoke

Use the Agent tool to launch the `manim-scene-builder` subagent. Pass the user's full request as the task prompt, preserving all details about:

- The mathematical concept or topic to animate
- Target audience or complexity level (if mentioned)
- Desired quality or length (if mentioned)
- Any specific visual style, color, or layout preferences

## Example delegation prompt

```
Create a Manim animation that visually explains the Pythagorean theorem.
Show a right triangle with labeled sides a, b, and c. Animate squares
growing from each side and demonstrate that the area of the two smaller
squares equals the area of the largest square. Use a clean, beginner-friendly
style with blue for the triangle and yellow highlights for key steps.
Render to a 1080p .mp4 file.
```

## Key conventions for the manim-scene-builder agent

- Scene class names should be descriptive (e.g. `PythagoreanTheoremProof`)
- Output lands in `media/videos/<filename>/<quality>/SceneName.mp4`
- Use `-pqh` flag for 1080p (default), `-pql` for fast test renders
- `MathTex` for LaTeX expressions, `Text` for plain text
- Standard color coding: `BLUE`/`WHITE` for primary, `YELLOW` for highlights, `RED` for warnings, `GREEN` for results
