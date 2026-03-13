# Manim Scene Builder — Persistent Memory

See detailed notes in topic files linked below.

## Key Patterns

- **Class name**: always `Main(Scene)` — matches VS Code build task and CLAUDE.md convention.
- **Output path**: `videos/<concept>/media/videos/main/<quality>/Main.mp4`. Copy to `videos/<concept>/main.py` and `main.mp4`.
- **Render command**: `manim -qh main.py Main` from inside the concept folder.

## Geometry Helpers (confirmed working)

Use free-standing helper methods inside the `Main` class:

```python
def build_right_triangle(self, a, b, origin=ORIGIN, color=WHITE):
    v0 = np.array(origin)
    v1 = v0 + UP * a
    v2 = v0 + RIGHT * b
    tri = Polygon(v0, v1, v2, color=color, stroke_width=3)
    return tri, v0, v1, v2

def right_angle_mark(self, corner, size=0.18, color=WHITE):
    sq = Square(side_length=size, color=color, stroke_width=2)
    sq.move_to(corner + np.array([size / 2, size / 2, 0]))
    return sq

def square_on_segment(self, p1, p2, outward_dir, color=BLUE, opacity=0.35):
    side_vec = p2 - p1
    perp = outward_dir * np.linalg.norm(side_vec)
    sq = Polygon(p1, p2, p2 + perp, p1 + perp,
                 color=color, fill_color=color,
                 fill_opacity=opacity, stroke_width=2.5)
    return sq
```

`outward_dir` for square on hypotenuse: `normalize(rotate_vector(hip_vec, -PI / 2))`.

## Color Palette (this project)

- `BLUE` — catetos e quadrados menores
- `YELLOW` — hipotenusa e quadrado maior
- `GREEN` — resultados / confirmacao (`\checkmark`, contas certas)
- `WHITE` — texto geral, angulo reto
- `RED` — nao usado (sem elementos negativos no video de Pitagoras)

## MathTex Color Coding

Split the expression into tokens to color individual parts:

```python
formula = MathTex(r"a^2", r"+", r"b^2", r"=", r"c^2", font_size=48)
formula[0].set_color(BLUE)
formula[2].set_color(BLUE)
formula[4].set_color(YELLOW)
```

## Animation Sequence Template (Pythagorean video)

1. Hook: `Create(tri)` -> `GrowFromEdge(sq, direction)` x3 -> copies fly to hyp square
2. Naming: `Write(label)` one by one; flash angle mark with `.animate.set_color(YELLOW).scale(1.3)`
3. Squares: `GrowFromEdge` per side (RIGHT for left square, UP for bottom, LEFT for hyp)
4. Reveal: copies `.animate.move_to(center).scale(0.48)` then `FadeOut` + `Write(formula)`
5. Example: same GrowFromEdge pattern, then `Write(conta)` + `Write(checkmark)`
6. Closing: `Write(formula_final)` + small recap triangle + challenge text

## Token Bar Helper (LLM-Tokens video, confirmed working pattern)

```python
def make_token_bar(self, tokens, token_colors=None, font_size=28,
                   rect_height=0.65, padding=0.18, show_ids=False, ids=None):
    bar = VGroup()
    for i, tok in enumerate(tokens):
        color = token_colors[i % len(token_colors)]
        lbl = Text(tok, font_size=font_size, color=WHITE, weight=BOLD)
        w = lbl.width + padding * 2
        rect = Rectangle(width=w, height=rect_height, color=color,
                         fill_color=color, fill_opacity=0.75, stroke_width=1.5)
        lbl.move_to(rect.get_center())
        cell = VGroup(rect, lbl)
        if show_ids and ids is not None:
            id_lbl = Text(str(ids[i]), font_size=16, color=GREY_B)
            id_lbl.next_to(rect, DOWN, buff=0.08)
            cell.add(id_lbl)
        bar.add(cell)
    bar.arrange(RIGHT, buff=0.06)
    return bar
```

Key insight: child VGroups of `make_token_bar` can be referenced by index (`bar[i]`) for
individual cell animations. You can `FadeIn(bar[0])` independently even if the full bar is
not in the scene. `.get_center()` works on any VGroup child regardless of scene membership.

## Progress Bar (color-changing fill)

Use two stacked Rectangles — background + fill. Animate fill width + color in sequence:
```python
cost_bg   = Rectangle(width=6.0, height=0.45, ...)
cost_fill = Rectangle(width=0.01, height=0.45, color=GREEN, ...)
cost_fill.align_to(cost_bg, LEFT)
# Animate:
self.play(cost_fill.animate.set_width(2.0).align_to(cost_bg, LEFT))
self.play(cost_fill.animate.set_color(YELLOW).set_fill(YELLOW).set_width(4.0).align_to(cost_bg, LEFT))
```
Always call `.align_to(cost_bg, LEFT)` after `.set_width()` or bar drifts to center.

## Shared Futuristic Background (mandatory)

Every new scene **must** import and apply the shared background from `videos/manim_common/bg.py`.
Add this block at the top of every `main.py`, right after `from manim import *`:

```python
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from manim_common.bg import build_futuristic_bg
```

Then call it as the **first line** inside `construct()`:

```python
def construct(self):
    build_futuristic_bg(self)   # animated bg: corner blobs + streaks + bokeh dots
    ...
```

Source: `videos/manim_common/bg.py` — do NOT copy the function inline; always import it.

## Details

- See `patterns.md` for reusable snippets.
