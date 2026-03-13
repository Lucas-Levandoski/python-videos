from manim import *
import sys
import os

# Portrait 9:16
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16.0
config.frame_width = 9.0

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
from manim_common.bg import build_futuristic_bg

# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------
TOKEN_COLORS = [BLUE, GREEN, YELLOW, TEAL, PURPLE, ORANGE, RED, MAROON]
PROB_BAR_COLOR = GREEN
HIGHLIGHT_COLOR = YELLOW


# ---------------------------------------------------------------------------
# Main Scene
# ---------------------------------------------------------------------------
class Main(Scene):
    # ------------------------------------------------------------------
    # Helper: build a single token cell (rounded rect + label)
    # ------------------------------------------------------------------
    def make_token_cell(self, text, color, font_size=30, rect_height=0.70, padding=0.22):
        lbl = Text(text, font_size=font_size, color=WHITE, weight=BOLD)
        w = max(lbl.width + padding * 2, 0.50)
        rect = RoundedRectangle(
            width=w,
            height=rect_height,
            corner_radius=0.12,
            color=color,
            fill_color=color,
            fill_opacity=0.75,
            stroke_width=2.0,
        )
        lbl.move_to(rect.get_center())
        return VGroup(rect, lbl)

    # ------------------------------------------------------------------
    # Helper: build a horizontal bar of token cells
    # ------------------------------------------------------------------
    def make_token_bar(self, tokens, colors=None, font_size=30,
                       rect_height=0.70, padding=0.22, buff=0.08):
        if colors is None:
            colors = TOKEN_COLORS
        bar = VGroup()
        for i, tok in enumerate(tokens):
            cell = self.make_token_cell(tok, colors[i % len(colors)],
                                        font_size=font_size,
                                        rect_height=rect_height,
                                        padding=padding)
            bar.add(cell)
        bar.arrange(RIGHT, buff=buff)
        return bar

    # ------------------------------------------------------------------
    # Helper: build a probability row  (token label | bar | percent)
    # ------------------------------------------------------------------
    def make_prob_row(self, token_text, percent, max_bar_width=3.2,
                      bar_color=GREEN, font_size=26, highlighted=False):
        tok_lbl = Text(token_text, font_size=font_size, color=WHITE, weight=BOLD)
        tok_lbl.set_width(min(tok_lbl.width, 2.2))

        bar_bg = Rectangle(
            width=max_bar_width,
            height=0.38,
            color=GREY_D,
            fill_color=GREY_D,
            fill_opacity=0.6,
            stroke_width=0,
        )
        fill_w = max_bar_width * (percent / 100)
        bar_fill = Rectangle(
            width=fill_w,
            height=0.38,
            color=bar_color,
            fill_color=bar_color,
            fill_opacity=0.85,
            stroke_width=0,
        )
        bar_fill.align_to(bar_bg, LEFT)

        bar_group = VGroup(bar_bg, bar_fill)

        pct_lbl = Text(f"{percent}%", font_size=font_size - 2, color=GREY_A)
        pct_lbl.set_width(min(pct_lbl.width, 0.7))

        row = VGroup(tok_lbl, bar_group, pct_lbl)
        row.arrange(RIGHT, buff=0.20, aligned_edge=ORIGIN)

        if highlighted:
            border = SurroundingRectangle(
                row,
                color=YELLOW,
                stroke_width=2.5,
                buff=0.12,
                corner_radius=0.10,
            )
            return VGroup(row, border)

        return row

    # ------------------------------------------------------------------
    # Main construct
    # ------------------------------------------------------------------
    def construct(self):
        build_futuristic_bg(self)

        # ==============================================================
        # 0:00 – 0:08  HOOK
        # ==============================================================
        self._hook()

        # ==============================================================
        # 0:08 – 0:23  DEFINITION
        # ==============================================================
        self._definition()

        # ==============================================================
        # 0:23 – 0:43  TOKEN ≠ PALAVRA
        # ==============================================================
        self._token_vs_word()

        # ==============================================================
        # 0:43 – 1:18  GENERATIVE MECHANISM
        # ==============================================================
        self._generative_mechanism()

        # ==============================================================
        # 1:18 – 1:30  CLOSING
        # ==============================================================
        self._closing()

    # ------------------------------------------------------------------
    # HOOK (0:00 – 0:08)
    # ------------------------------------------------------------------
    def _hook(self):
        # Full sentence appears first
        sentence = Text(
            "Inteligência artificial\nmuda o mundo",
            font_size=52,
            color=WHITE,
            line_spacing=1.3,
        )
        sentence.move_to(ORIGIN)

        self.play(FadeIn(sentence, shift=UP * 0.3), run_time=0.8)
        self.wait(1.2)

        # Build the token bar — positioned where sentence was
        hook_tokens = [
            "Int", "el", "ig", "ência",
            "▁artificial", "▁muda", "▁o", "▁mundo",
        ]
        hook_bar = self.make_token_bar(
            hook_tokens,
            colors=TOKEN_COLORS,
            font_size=26,
            rect_height=0.65,
        )
        # Portrait frame is 9 wide; scale down if needed
        if hook_bar.width > 8.2:
            hook_bar.scale(8.2 / hook_bar.width)

        # Arrange in two rows for portrait readability
        row1 = self.make_token_bar(
            hook_tokens[:4], colors=TOKEN_COLORS[:4], font_size=26, rect_height=0.65
        )
        row2 = self.make_token_bar(
            hook_tokens[4:], colors=TOKEN_COLORS[4:], font_size=26, rect_height=0.65
        )
        token_rows = VGroup(row1, row2)
        token_rows.arrange(DOWN, buff=0.30)
        token_rows.move_to(ORIGIN)

        if token_rows.width > 8.2:
            token_rows.scale(8.2 / token_rows.width)

        # Shatter: FadeOut sentence, then burst each token in
        self.play(FadeOut(sentence), run_time=0.4)
        anims = []
        for cell in list(row1) + list(row2):
            anims.append(FadeIn(cell, scale=0.6, run_time=0.5))
        self.play(LaggedStart(*anims, lag_ratio=0.12))
        self.wait(0.8)

        # Pulse the whole token display
        self.play(
            token_rows.animate.scale(1.05),
            run_time=0.25,
        )
        self.play(
            token_rows.animate.scale(1 / 1.05),
            run_time=0.25,
        )
        self.wait(0.5)

        self.play(FadeOut(token_rows), run_time=0.5)

    # ------------------------------------------------------------------
    # DEFINITION (0:08 – 0:23)
    # ------------------------------------------------------------------
    def _definition(self):
        label = Text(
            "Token = menor unidade\nque a IA processa",
            font_size=44,
            color=WHITE,
            line_spacing=1.35,
        )
        label.move_to(ORIGIN)

        # Highlight "Token" in yellow
        highlight_box = SurroundingRectangle(
            label,
            color=YELLOW,
            stroke_width=2.5,
            buff=0.20,
            corner_radius=0.14,
        )

        self.play(Write(label), run_time=1.2)
        self.wait(0.5)
        self.play(Create(highlight_box), run_time=0.6)
        self.wait(2.5)
        self.play(FadeOut(VGroup(label, highlight_box)), run_time=0.5)

    # ------------------------------------------------------------------
    # TOKEN ≠ PALAVRA (0:23 – 0:43)
    # ------------------------------------------------------------------
    def _token_vs_word(self):
        title = Text("Token  ≠  palavra", font_size=44, color=YELLOW, weight=BOLD)
        title.move_to(UP * 6.5)
        self.play(FadeIn(title, shift=DOWN * 0.3), run_time=0.5)

        examples = [
            # (word_text,  tokens_list,  label_text,            token_colors)
            (
                "gato",
                ["gato"],
                "1 token",
                [BLUE],
            ),
            (
                "inacreditável",
                ["in", "acredit", "ável"],
                "3 tokens",
                [BLUE, TEAL, GREEN],
            ),
            (
                "Olá, mundo!",
                ["Ol", "á", ",", "▁mundo", "!"],
                "pontuação = token próprio",
                [BLUE, GREEN, YELLOW, TEAL, ORANGE],
            ),
        ]

        for word_text, toks, lbl_text, tok_colors in examples:
            # Word text
            word = Text(word_text, font_size=48, color=WHITE)
            word.move_to(UP * 3.5)

            # Token bar (build before arrow so we can target it)
            bar = self.make_token_bar(
                toks, colors=tok_colors, font_size=30, rect_height=0.70
            )
            bar.move_to(UP * 1.5)
            if bar.width > 7.8:
                bar.scale(7.8 / bar.width)

            # Arrow from bottom of word to top of token bar
            arrow = Arrow(
                start=word.get_bottom() + DOWN * 0.05,
                end=bar.get_top() + UP * 0.05,
                color=GREY_A,
                buff=0.05,
                stroke_width=2.5,
                max_tip_length_to_length_ratio=0.15,
            )

            # Label below bar
            lbl = Text(lbl_text, font_size=32, color=GREEN)
            lbl.next_to(bar, DOWN, buff=0.35)

            self.play(FadeIn(word, shift=DOWN * 0.2), run_time=0.5)
            self.play(Create(arrow), run_time=0.3)
            self.play(
                LaggedStart(
                    *[FadeIn(cell, scale=0.7) for cell in bar],
                    lag_ratio=0.15,
                    run_time=0.6,
                )
            )
            self.play(Write(lbl), run_time=0.5)
            self.wait(1.4)
            self.play(
                FadeOut(VGroup(word, arrow, bar, lbl)),
                run_time=0.4,
            )

        self.play(FadeOut(title), run_time=0.4)

    # ------------------------------------------------------------------
    # GENERATIVE MECHANISM (0:43 – 1:18)
    # ------------------------------------------------------------------
    def _generative_mechanism(self):
        # --- Section title ---
        sec_title = Text("Como a IA gera texto", font_size=38, color=YELLOW, weight=BOLD)
        sec_title.move_to(UP * 6.8)
        self.play(FadeIn(sec_title, shift=DOWN * 0.3), run_time=0.5)

        # ---- STEP 1: input tokens enter the network ----
        self._gen_step1(sec_title)

        # ---- STEP 2: probability list ----
        self._gen_step2()

        # ---- STEP 3: token selected, cycle repeats ----
        self._gen_step3()

        self.play(FadeOut(sec_title), run_time=0.4)

    def _gen_step1(self, sec_title):
        step_lbl = Text("Passo 1: tokens entram na rede", font_size=30, color=GREY_A)
        step_lbl.next_to(sec_title, DOWN, buff=0.25)
        self.play(FadeIn(step_lbl), run_time=0.4)

        # Input token bar
        input_tokens = ["Int", "el", "ig", "ência"]
        in_bar = self.make_token_bar(
            input_tokens,
            colors=TOKEN_COLORS[:4],
            font_size=26,
            rect_height=0.62,
        )
        in_bar.move_to(UP * 4.2)
        if in_bar.width > 3.8:
            in_bar.scale(3.8 / in_bar.width)

        # Neural network box (stylized)
        nn_box = self._make_nn_box()
        nn_box.move_to(UP * 1.0)

        # Arrow from tokens to box
        arrow_in = Arrow(
            start=in_bar.get_bottom() + DOWN * 0.05,
            end=nn_box.get_top() + UP * 0.05,
            color=BLUE_B,
            stroke_width=2.5,
            buff=0.05,
        )

        self.play(
            LaggedStart(
                *[FadeIn(cell, scale=0.7) for cell in in_bar],
                lag_ratio=0.15,
                run_time=0.7,
            )
        )
        self.play(Create(arrow_in), run_time=0.5)
        self.play(FadeIn(nn_box), run_time=0.6)

        # Pulse the nn box to simulate processing
        for _ in range(2):
            self.play(
                nn_box.animate.set_fill(BLUE_D, opacity=0.55),
                run_time=0.3,
            )
            self.play(
                nn_box.animate.set_fill(BLUE_E, opacity=0.35),
                run_time=0.3,
            )

        self.wait(0.5)

        # Store refs for next step
        self._in_bar = in_bar
        self._nn_box = nn_box
        self._arrow_in = arrow_in
        self._step_lbl = step_lbl

    def _make_nn_box(self):
        """Stylized neural-network rectangle with 3 columns of nodes."""
        box = RoundedRectangle(
            width=5.5,
            height=3.2,
            corner_radius=0.25,
            color=BLUE_C,
            fill_color=BLUE_E,
            fill_opacity=0.35,
            stroke_width=2.0,
        )

        # Node columns: 3 cols x 3 rows
        nodes = VGroup()
        cols = [-1.6, 0.0, 1.6]
        rows = [0.85, 0.0, -0.85]
        for x in cols:
            for y in rows:
                node = Circle(
                    radius=0.18,
                    color=BLUE_B,
                    fill_color=BLUE_B,
                    fill_opacity=0.5,
                    stroke_width=1.5,
                )
                node.move_to([x, y, 0])
                nodes.add(node)

        # Connections (only adjacent columns)
        edges = VGroup()
        col_nodes = [nodes[i * 3 : (i + 1) * 3] for i in range(3)]
        for ci in range(2):
            for n1 in col_nodes[ci]:
                for n2 in col_nodes[ci + 1]:
                    edge = Line(
                        n1.get_center(),
                        n2.get_center(),
                        color=BLUE_B,
                        stroke_width=0.8,
                        stroke_opacity=0.4,
                    )
                    edges.add(edge)

        label = Text("rede neural", font_size=22, color=GREY_B)
        label.move_to(box.get_bottom() + UP * 0.32)

        return VGroup(box, edges, nodes, label)

    def _gen_step2(self):
        step_lbl2 = Text("Passo 2: probabilidades", font_size=30, color=GREY_A)
        step_lbl2.move_to(self._step_lbl.get_center())

        self.play(
            FadeOut(self._step_lbl),
            FadeIn(step_lbl2),
            run_time=0.4,
        )

        # Probability list appears to the right/below the nn box
        prob_data = [
            ("▁artificial", 42, True),
            ("▁incrível",   18, False),
            ("▁muda",       11, False),
            ("▁é",           7, False),
            ("...",          4, False),
        ]

        rows = VGroup()
        for tok_text, pct, highlighted in prob_data:
            bar_color = YELLOW if highlighted else GREEN
            row = self.make_prob_row(
                tok_text, pct,
                max_bar_width=2.8,
                bar_color=bar_color,
                font_size=24,
                highlighted=highlighted,
            )
            rows.add(row)

        rows.arrange(DOWN, buff=0.22, aligned_edge=LEFT)
        rows.next_to(self._nn_box, DOWN, buff=0.55)
        rows.shift(RIGHT * 0.2)

        if rows.width > 8.2:
            rows.scale(8.2 / rows.width)

        # Arrow from nn box to prob list
        arrow_out = Arrow(
            start=self._nn_box.get_bottom() + DOWN * 0.05,
            end=rows.get_top() + UP * 0.05,
            color=GREEN,
            stroke_width=2.5,
            buff=0.05,
        )

        self.play(Create(arrow_out), run_time=0.5)
        self.play(
            LaggedStart(
                *[FadeIn(row, shift=RIGHT * 0.2) for row in rows],
                lag_ratio=0.18,
                run_time=1.0,
            )
        )
        self.wait(1.0)

        # Highlight the top entry
        top_row = rows[0]
        self.play(
            top_row.animate.scale(1.08),
            run_time=0.35,
        )
        self.play(
            top_row.animate.scale(1 / 1.08),
            run_time=0.35,
        )
        self.wait(0.8)

        self._rows = rows
        self._arrow_out = arrow_out
        self._step_lbl2 = step_lbl2

    def _gen_step3(self):
        step_lbl3 = Text("Passo 3: escolha e repetição", font_size=30, color=GREY_A)
        step_lbl3.move_to(self._step_lbl2.get_center())

        self.play(
            FadeOut(self._step_lbl2),
            FadeIn(step_lbl3),
            run_time=0.4,
        )

        # The winning token flies left and joins the input sequence
        # Make a copy of the top probability row token label
        winning_token = "▁artificial"
        winner_cell = self.make_token_cell(
            winning_token, YELLOW, font_size=26, rect_height=0.62
        )
        # Start at the top prob row position
        winner_cell.move_to(self._rows[0].get_center())
        self.add(winner_cell)

        # Hide the probability rows
        self.play(
            FadeOut(self._rows),
            FadeOut(self._arrow_out),
            run_time=0.4,
        )

        # Animate winner flying to join the input bar (above nn box)
        # New extended input bar: original 4 + winner
        new_tokens = ["Int", "el", "ig", "ência", "▁artificial"]
        new_colors = TOKEN_COLORS[:4] + [YELLOW]
        new_bar = self.make_token_bar(
            new_tokens, colors=new_colors, font_size=24, rect_height=0.58
        )
        new_bar.move_to(self._in_bar.get_center())
        if new_bar.width > 5.5:
            new_bar.scale(5.5 / new_bar.width)

        # Fly winner to slot 4 position in new_bar
        target_pos = new_bar[4].get_center()

        self.play(
            winner_cell.animate.move_to(target_pos).scale(0.7),
            run_time=0.8,
        )
        self.remove(winner_cell)
        self.play(
            FadeOut(self._in_bar),
            FadeIn(new_bar),
            run_time=0.3,
        )
        self.wait(0.3)

        # --- Fast-forward: 2 more cycles shown quickly ---
        cycle_data = [
            (["Int", "el", "ig", "ência", "▁artificial", "▁muda"],
             TOKEN_COLORS[:4] + [YELLOW, ORANGE],
             "▁muda", ORANGE),
            (["Int", "el", "ig", "ência", "▁artificial", "▁muda", "▁o"],
             TOKEN_COLORS[:4] + [YELLOW, ORANGE, RED],
             "▁o", RED),
        ]

        current_bar = new_bar
        for extended_tokens, ext_colors, next_tok_text, next_tok_color in cycle_data:
            # Show a quick flash of the nn box processing
            self.play(
                self._nn_box.animate.set_fill(BLUE_D, opacity=0.7),
                run_time=0.2,
            )
            self.play(
                self._nn_box.animate.set_fill(BLUE_E, opacity=0.35),
                run_time=0.2,
            )

            # Animate new token appearing
            new_cell = self.make_token_cell(
                next_tok_text, next_tok_color, font_size=24, rect_height=0.58
            )
            new_cell.move_to(self._nn_box.get_center() + DOWN * 1.2)
            new_cell.set_opacity(0)

            ext_bar = self.make_token_bar(
                extended_tokens, colors=ext_colors, font_size=24, rect_height=0.58
            )
            ext_bar.move_to(current_bar.get_center())
            if ext_bar.width > 4.6:
                ext_bar.scale(4.6 / ext_bar.width)

            self.play(
                FadeOut(current_bar),
                FadeIn(ext_bar),
                run_time=0.45,
            )
            current_bar = ext_bar
            self.wait(0.25)

        # Final assembled phrase
        final_tokens = ["Int", "el", "ig", "ência", "▁artificial", "▁muda", "▁o", "▁mundo"]
        final_colors = TOKEN_COLORS
        final_bar = self.make_token_bar(
            final_tokens, colors=final_colors, font_size=24, rect_height=0.58
        )
        final_bar.move_to(current_bar.get_center())
        if final_bar.width > 5.0:
            final_bar.scale(5.0 / final_bar.width)

        self.play(
            self._nn_box.animate.set_fill(BLUE_D, opacity=0.7),
            run_time=0.2,
        )
        self.play(
            self._nn_box.animate.set_fill(BLUE_E, opacity=0.35),
            run_time=0.2,
        )
        self.play(
            FadeOut(current_bar),
            FadeIn(final_bar),
            run_time=0.5,
        )
        self.wait(0.8)

        # Fade out the whole mechanism
        to_remove = VGroup(self._nn_box, self._arrow_in, final_bar, step_lbl3)
        self.play(FadeOut(to_remove), run_time=0.6)

    # ------------------------------------------------------------------
    # CLOSING (1:18 – 1:30)
    # ------------------------------------------------------------------
    def _closing(self):
        line1 = Text(
            "A IA não escreve frases.",
            font_size=46,
            color=WHITE,
            weight=BOLD,
        )
        line2 = Text(
            "Ela prevê um pedacinho",
            font_size=46,
            color=WHITE,
            weight=BOLD,
        )
        line3 = Text(
            "de cada vez.",
            font_size=46,
            color=YELLOW,
            weight=BOLD,
        )

        closing = VGroup(line1, line2, line3)
        closing.arrange(DOWN, buff=0.45)
        closing.move_to(ORIGIN)

        self.play(
            LaggedStart(
                FadeIn(line1, shift=UP * 0.2),
                FadeIn(line2, shift=UP * 0.2),
                FadeIn(line3, shift=UP * 0.2),
                lag_ratio=0.4,
                run_time=1.5,
            )
        )
        self.wait(3.0)
        self.play(FadeOut(closing), run_time=0.8)
