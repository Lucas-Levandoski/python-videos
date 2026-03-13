import random
from manim import *

def build_futuristic_bg(scene):
    """Shared background: corner gradients + horizon glow + diagonal streaks + bokeh dots."""
    STREAK_COLORS = ["#00d4ff", "#4fc3f7", "#80deea", "#b3e5fc", BLUE_C, TEAL_C, WHITE]
    DOT_COLORS    = ["#00d4ff", "#4fc3f7", BLUE_C, TEAL_C, "#b3e5fc"]

    # Diagonal direction: up-right at ~30° from vertical
    DIAG = UP * 0.87 + RIGHT * 0.50

    bg = VGroup()

    # --- Corner gradient blobs (stacked circles for soft falloff) ---
    for cx, cy, col in [(-6.5, 3.8, "#4a00a0"), (6.5, -3.8, "#004d6e")]:
        for radius, op in [(5.5, 0.07), (3.8, 0.06), (2.2, 0.05)]:
            blob = Circle(radius=radius, color=col,
                          fill_color=col, fill_opacity=op, stroke_width=0)
            blob.move_to([cx, cy, 0])
            bg.add(blob)

    # --- Diagonal streaks ---
    for _ in range(45):
        h     = random.uniform(0.2, 2.2)
        x     = random.uniform(-9.0, 5.0)   # bias left so they drift into frame
        y_ctr = random.uniform(-5.0, 4.5)
        color = random.choice(STREAK_COLORS)
        max_op = random.uniform(0.18, 0.42)
        speed  = random.uniform(0.35, 1.5)
        sw     = random.uniform(0.5, 2.0)

        # Slant the line itself to match the diagonal direction
        dx = h * 0.29   # ~16° slant from vertical
        streak = Line([x - dx, y_ctr - h / 2, 0], [x + dx, y_ctr + h / 2, 0],
                      color=color, stroke_width=sw)
        streak.set_opacity(0.0)

        def make_streak_upd(spd, mop, ph, ph_spd):
            phase = [ph]
            def upd(m, dt):
                phase[0] += ph_spd * dt
                m.set_opacity(mop * max(0, np.sin(phase[0])))
                m.shift(DIAG * spd * dt)
                cx, cy = m.get_center()[:2]
                if cy > 5.5 or cx > 9.0:
                    m.move_to([random.uniform(-10.0, -1.0),
                               random.uniform(-6.0, -3.0), 0])
                    phase[0] = random.uniform(0, TAU)
            return upd

        streak.add_updater(make_streak_upd(
            speed, max_op,
            random.uniform(0, TAU),
            random.uniform(0.4, 1.8),
        ))
        bg.add(streak)

    # --- Bokeh dots (also drift diagonally, more slowly) ---
    for _ in range(55):
        color  = random.choice(DOT_COLORS)
        max_op = random.uniform(0.07, 0.25)
        dot    = Dot(radius=random.uniform(0.02, 0.14), color=color)
        dot.set_fill(color, opacity=0.0)
        dot.move_to([random.uniform(-7.5, 7.5), random.uniform(-4.5, 4.5), 0])

        speed = random.uniform(0.02, 0.08)

        def make_dot_upd(spd, mop, ph, ph_spd):
            phase = [ph]
            def upd(m, dt):
                phase[0] += ph_spd * dt
                m.set_fill(opacity=mop * max(0, np.sin(phase[0])))
                m.shift(DIAG * spd * dt)
                cx, cy = m.get_center()[:2]
                if cy > 5.0 or cx > 8.5:
                    m.move_to([random.uniform(-8.5, 0.0),
                               random.uniform(-5.0, 0.0), 0])
                    phase[0] = random.uniform(0, TAU)
            return upd

        dot.add_updater(make_dot_upd(
            speed, max_op,
            random.uniform(0, TAU),
            random.uniform(0.3, 1.3),
        ))
        bg.add(dot)

    scene.add(bg)