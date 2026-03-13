# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a video production repository for creating educational content. It combines three stages: pedagogical blueprint design, script writing, and Manim animation. All scripts are written in **Portuguese (Brazil)**.

The `claude/` directory (this working directory) holds the Claude Code agent configuration. Manim scene files and rendered output live in the parent repo root (`../`).

## Folder Structure Rule (mandatory)

Every concept gets its own folder at the **repo root** under `projects/`:

```
projects/
└── <concept-name>/          ← slug derived from the concept (e.g. "pythagorean-theorem")
    ├── blueprint.md         ← pedagogical blueprint (edu-concept-strategist output)
    ├── script.md            ← narrator script in Portuguese (video-script-writer output)
    ├── main.py              ← Manim scene file (manim-scene-builder output)
    └── main.mp4             ← rendered video (copied from Manim media output)
```

All agents **must** write their output into this folder. Never save files to the repo root or to arbitrary paths.

## Manim Commands

```bash
# Install dependency
pip install manim

# Render at 1080p (production) — run from inside the concept folder
manim -qh main.py Main

# Render at 480p (fast test)
manim -pql main.py Main

# Render at 4K
manim -qk main.py Main
```

The VS Code default build task (`Ctrl+Shift+B`) runs `manim -qh ${file} Main`.

Rendered `.mp4` files land in `projects/<concept-name>/media/videos/main/<quality>/Main.mp4`. After rendering, copy the final `.mp4` to `videos/<concept-name>/main.mp4` for easy access.

## Three-Agent Pipeline

The video creation workflow uses three specialized agents in sequence:

1. **`edu-concept-strategist`** — Invoked first for any new video. Produces a structured teaching blueprint using Bloom's Taxonomy and instructional design principles. Uses `claude-opus-4-6`. Asks for video length if not specified.

2. **`video-script-writer`** — Takes the blueprint and writes a narrator-ready script **in Portuguese**. Works interactively section-by-section, waiting for user approval before proceeding. Uses `claude-opus-4-6`.

3. **`manim-scene-builder`** — Writes and renders Manim Python scenes to `.mp4`. Has restricted tools (Read, Edit, Write, Glob, Grep, NotebookEdit — no Bash). Uses `claude-sonnet-4-6`.

Agent teams are enabled via `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (set in `.claude/settings.json`). Teammate mode is `tmux`.

## Manim Conventions

- Scene classes are named `Main` (the VS Code task and existing scenes all use this)
- Color coding: `BLUE`/`WHITE` for primary concepts, `YELLOW` for highlights, `RED` for warnings/negatives, `GREEN` for results
- Use `MathTex` for LaTeX expressions, `Text` for plain text
- Use `VGroup` to group related objects for coordinated transforms
- Portuguese text in `Text()` objects is standard (e.g., `"Sociável"`, `"Diúrno"`)

## Agent Memory

Each agent has persistent memory in `.claude/agent-memory/<agent-name>/`. The `MEMORY.md` in each directory is auto-loaded into that agent's system prompt (truncated after 200 lines). Detailed notes go in separate topic files linked from `MEMORY.md`.

## Slash Command

`/manim <description>` delegates directly to the `manim-scene-builder` agent via the skill defined in `.claude/skills/manim-generator/SKILL.md`.
