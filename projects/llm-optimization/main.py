from manim import *
import sys
import os

# Landscape 16:9 — default Manim resolution (1920x1080), no config override needed

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../.."))
from manim_common.bg import build_futuristic_bg

# ---------------------------------------------------------------------------
# Color palette
# ---------------------------------------------------------------------------
C_PRICE   = RED           # costs / prices / negatives
C_TOKENS  = YELLOW        # token counts / highlights
C_GOOD    = GREEN         # savings / results / gains
C_TECH    = BLUE          # technical concepts
C_WHITE   = WHITE         # general text
C_DIM     = GREY_B        # secondary labels
C_TEAL    = TEAL          # accent / alternative tech


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def make_bar(width, height, color, fill_op=0.7, stroke_w=1.5):
    return Rectangle(
        width=width, height=height,
        color=color, fill_color=color,
        fill_opacity=fill_op, stroke_width=stroke_w,
    )


def make_box(text_obj, color, fill_op=0.18, padding=0.2, corner_r=0.12):
    box = RoundedRectangle(
        width=text_obj.width + padding * 2,
        height=text_obj.height + padding,
        corner_radius=corner_r,
        color=color,
        fill_color=color,
        fill_opacity=fill_op,
        stroke_width=2.0,
    )
    box.move_to(text_obj.get_center())
    return box


# ---------------------------------------------------------------------------
# Main Scene
# ---------------------------------------------------------------------------
class Main(Scene):

    # ======================================================================
    # Entry point
    # ======================================================================
    def construct(self):
        build_futuristic_bg(self)

        self._seg0_hook()
        self._seg1_parameters()
        self._seg2_training_vs_inference()
        self._seg3_price_problem()
        self._seg4_quantization()
        self._seg5_distillation()
        self._seg6_moe()
        self._seg7_flash_attention()
        self._seg8_chinchilla()
        self._seg9_hardware()
        self._seg10_speculative()
        self._seg11_price_timeline()
        self._seg12_closing()

    # ======================================================================
    # SEG 0 — HOOK: preço caindo de $60 → $0.07
    # ======================================================================
    def _seg0_hook(self):
        # Title card
        title = Text(
            "Como LLMs Ficaram\n1000x Mais Baratos",
            font_size=62,
            color=WHITE,
            weight=BOLD,
            line_spacing=1.2,
        ).move_to(ORIGIN)

        self.play(FadeIn(title, scale=0.85), run_time=1.0)
        self.wait(2.5)
        self.play(FadeOut(title), run_time=0.6)

        # ---- Dual counter: price drops (green→red label) / tokens consumed rises ----
        price_lbl  = Text("Custo por milhão de tokens", font_size=32, color=C_DIM)
        price_lbl.move_to(UP * 2.8 + LEFT * 3.0)

        tokens_lbl = Text("Tokens consumidos / dia", font_size=32, color=C_DIM)
        tokens_lbl.move_to(UP * 2.8 + RIGHT * 3.0)

        divider = Line(UP * 3.5, DOWN * 3.5, color=GREY_D, stroke_width=1.5)

        self.play(
            FadeIn(price_lbl),
            FadeIn(tokens_lbl),
            Create(divider),
            run_time=0.6,
        )

        # Price counter — starts at $60.00, drops to $0.07
        price_values  = [60.00, 30.00, 15.00, 5.00, 2.00, 0.60, 0.15, 0.07]
        tokens_values = [
            "~500", "~2.000", "~5.000", "~20.000",
            "~50.000", "~150.000", "~300.000", "~500.000+",
        ]
        price_colors = [RED, RED, RED, ORANGE, YELLOW, YELLOW, GREEN, GREEN]

        price_num  = Text(f"${price_values[0]:.2f}", font_size=96, color=RED, weight=BOLD)
        price_num.move_to(LEFT * 3.0)

        tok_num = Text(tokens_values[0], font_size=72, color=YELLOW, weight=BOLD)
        tok_num.move_to(RIGHT * 3.0)

        year_lbl = Text("2020", font_size=36, color=C_DIM)
        year_lbl.move_to(DOWN * 2.8)

        self.play(
            FadeIn(price_num, shift=DOWN * 0.3),
            FadeIn(tok_num, shift=UP * 0.3),
            FadeIn(year_lbl),
            run_time=0.7,
        )
        self.wait(0.8)

        years = ["2020", "2021", "2021", "2022", "2023", "2023", "2024", "2025"]
        for i in range(1, len(price_values)):
            new_price = Text(
                f"${price_values[i]:.2f}",
                font_size=96,
                color=price_colors[i],
                weight=BOLD,
            ).move_to(LEFT * 3.0)

            new_tok = Text(
                tokens_values[i],
                font_size=72,
                color=YELLOW,
                weight=BOLD,
            ).move_to(RIGHT * 3.0)

            new_year = Text(years[i], font_size=36, color=C_DIM).move_to(DOWN * 2.8)

            speed = 0.35 if i < 4 else 0.25
            self.play(
                FadeOut(price_num, shift=DOWN * 0.2),
                FadeIn(new_price, shift=DOWN * 0.2),
                FadeOut(tok_num, shift=UP * 0.2),
                FadeIn(new_tok, shift=UP * 0.2),
                FadeOut(year_lbl),
                FadeIn(new_year),
                run_time=speed,
            )
            price_num  = new_price
            tok_num    = new_tok
            year_lbl   = new_year
            self.wait(0.2)

        self.wait(1.5)

        # Final annotation: 857x reduction
        reduction = Text("857x mais barato em 5 anos", font_size=38, color=C_GOOD, weight=BOLD)
        reduction.move_to(DOWN * 1.8)
        self.play(Write(reduction), run_time=0.8)
        self.wait(2.0)

        # Comparison persons
        self.play(
            FadeOut(VGroup(
                price_lbl, tokens_lbl, divider,
                price_num, tok_num, year_lbl, reduction,
            )),
            run_time=0.5,
        )

        person_2020 = VGroup(
            Text("Pessoa em 2020", font_size=34, color=C_DIM),
            Text("~500 tokens/dia", font_size=48, color=YELLOW, weight=BOLD),
        ).arrange(DOWN, buff=0.3).move_to(LEFT * 3.5)

        person_2025 = VGroup(
            Text("Pessoa em 2025", font_size=34, color=C_DIM),
            Text("~500.000+ tokens/dia", font_size=40, color=GREEN, weight=BOLD),
        ).arrange(DOWN, buff=0.3).move_to(RIGHT * 3.0)

        vs_label = Text("VS", font_size=52, color=WHITE, weight=BOLD).move_to(ORIGIN)

        self.play(
            FadeIn(person_2020, shift=LEFT * 0.3),
            FadeIn(vs_label),
            FadeIn(person_2025, shift=RIGHT * 0.3),
            run_time=0.8,
        )
        self.wait(2.5)
        self.play(FadeOut(VGroup(person_2020, vs_label, person_2025)), run_time=0.6)

    # ======================================================================
    # SEG 1 — PARÂMETROS
    # ======================================================================
    def _seg1_parameters(self):
        # Section title
        seg_title = self._section_title("Parâmetros: o que são os LLMs?")
        self.wait(0.5)

        # Neural network visualization
        nn = self._make_nn_diagram(cols=4, rows=4, spacing_x=2.2, spacing_y=1.0)
        nn.move_to(ORIGIN + DOWN * 0.3)
        nn.scale(0.85)

        self.play(Create(nn), run_time=1.2)
        self.wait(0.8)

        # Zoom into one weight connection — highlight it
        # Find a connection in the nn (edges are in nn[1])
        highlight_edge = nn[1][5].copy().set_color(YELLOW).set_stroke(width=5)
        self.play(Create(highlight_edge), run_time=0.5)

        # Show floating point number
        weight_val = Text("0.00342", font_size=44, color=YELLOW, weight=BOLD)
        weight_val.next_to(highlight_edge.get_center(), UP, buff=0.3)
        weight_box = make_box(weight_val, YELLOW, fill_op=0.15)
        self.play(FadeIn(VGroup(weight_box, weight_val)), run_time=0.5)
        self.wait(1.2)
        self.play(FadeOut(VGroup(highlight_edge, weight_box, weight_val)), run_time=0.4)

        # Number "175 billion" appears digit by digit
        self.play(FadeOut(nn), run_time=0.5)

        big_num = Text("175.000.000.000", font_size=72, color=YELLOW, weight=BOLD)
        big_num.move_to(UP * 0.5)
        param_label = Text("parâmetros no GPT-3", font_size=36, color=C_DIM)
        param_label.next_to(big_num, DOWN, buff=0.4)

        # Reveal digit by digit
        self.play(
            LaggedStart(
                *[FadeIn(char, shift=DOWN * 0.2) for char in big_num],
                lag_ratio=0.04,
                run_time=1.5,
            )
        )
        self.play(FadeIn(param_label), run_time=0.5)
        self.wait(2.0)

        # Slider analogy: changing parameter changes output
        slider_label = Text("Mudar um parâmetro → muda a saída", font_size=34, color=WHITE)
        slider_label.move_to(DOWN * 2.0)

        slider_bg = Rectangle(width=5.0, height=0.35, color=GREY_D,
                               fill_color=GREY_D, fill_opacity=0.6, stroke_width=0)
        slider_bg.move_to(DOWN * 2.8)
        slider_fill = Rectangle(width=2.5, height=0.35, color=C_TECH,
                                 fill_color=C_TECH, fill_opacity=0.85, stroke_width=0)
        slider_fill.align_to(slider_bg, LEFT)

        knob = Circle(radius=0.22, color=WHITE, fill_color=WHITE, fill_opacity=1.0)
        knob.move_to(slider_fill.get_right())

        self.play(FadeIn(slider_label), FadeIn(slider_bg), run_time=0.4)
        self.play(FadeIn(slider_fill), FadeIn(knob), run_time=0.4)
        self.play(
            slider_fill.animate.set_width(4.2).align_to(slider_bg, LEFT),
            knob.animate.move_to(slider_bg.get_left() + RIGHT * 4.2),
            run_time=0.8,
        )
        self.play(
            slider_fill.animate.set_width(1.0).align_to(slider_bg, LEFT),
            knob.animate.move_to(slider_bg.get_left() + RIGHT * 1.0),
            run_time=0.6,
        )
        self.wait(1.5)

        all_objs = VGroup(seg_title, big_num, param_label, slider_label,
                          slider_bg, slider_fill, knob)
        self.play(FadeOut(all_objs), run_time=0.6)

    def _make_nn_diagram(self, cols=4, rows=4, spacing_x=2.2, spacing_y=1.0):
        nodes = VGroup()
        edges = VGroup()
        node_grid = []
        total_w = (cols - 1) * spacing_x
        total_h = (rows - 1) * spacing_y

        for c in range(cols):
            col_nodes = []
            for r in range(rows):
                x = c * spacing_x - total_w / 2
                y = r * spacing_y - total_h / 2
                node = Circle(
                    radius=0.22,
                    color=BLUE_C,
                    fill_color=BLUE_E,
                    fill_opacity=0.6,
                    stroke_width=2.0,
                )
                node.move_to([x, y, 0])
                nodes.add(node)
                col_nodes.append(node)
            node_grid.append(col_nodes)

        for c in range(cols - 1):
            for n1 in node_grid[c]:
                for n2 in node_grid[c + 1]:
                    edge = Line(
                        n1.get_center(), n2.get_center(),
                        color=BLUE_B, stroke_width=0.9, stroke_opacity=0.4,
                    )
                    edges.add(edge)

        return VGroup(nodes, edges)

    # ======================================================================
    # SEG 2 — TREINAMENTO vs INFERÊNCIA
    # ======================================================================
    def _seg2_training_vs_inference(self):
        seg_title = self._section_title("Treinamento vs. Inferência")
        self.wait(0.5)

        # Split screen
        left_bg  = Rectangle(width=6.5, height=7.0, color=RED,
                              fill_color=RED, fill_opacity=0.08, stroke_width=1.5)
        right_bg = Rectangle(width=6.5, height=7.0, color=GREEN,
                              fill_color=GREEN, fill_opacity=0.08, stroke_width=1.5)
        left_bg.move_to(LEFT * 3.5 + DOWN * 0.3)
        right_bg.move_to(RIGHT * 3.5 + DOWN * 0.3)

        # Labels
        lbl_train = Text("TREINAMENTO", font_size=36, color=RED, weight=BOLD)
        lbl_train.move_to(LEFT * 3.5 + UP * 2.8)

        lbl_infer = Text("INFERÊNCIA", font_size=36, color=GREEN, weight=BOLD)
        lbl_infer.move_to(RIGHT * 3.5 + UP * 2.8)

        self.play(
            FadeIn(left_bg), FadeIn(right_bg),
            FadeIn(lbl_train), FadeIn(lbl_infer),
            run_time=0.7,
        )

        # Training details
        train_details = VGroup(
            Text("Cluster de GPUs", font_size=30, color=WHITE),
            Text("Meses de computação", font_size=28, color=C_DIM),
            Text("Bilhões de exemplos", font_size=28, color=C_DIM),
        ).arrange(DOWN, buff=0.35).move_to(LEFT * 3.5 + UP * 0.8)

        train_cost_gpt3 = Text("GPT-3: $4,6 milhões", font_size=34, color=RED, weight=BOLD)
        train_cost_gpt3.move_to(LEFT * 3.5 + DOWN * 0.8)

        train_cost_gpt4 = Text("GPT-4: $100 milhões+", font_size=34, color=RED, weight=BOLD)
        train_cost_gpt4.move_to(LEFT * 3.5 + DOWN * 1.7)

        # Inference details
        infer_details = VGroup(
            Text("Uma chamada de API", font_size=30, color=WHITE),
            Text("Milissegundos", font_size=28, color=C_DIM),
            Text("Uma resposta por vez", font_size=28, color=C_DIM),
        ).arrange(DOWN, buff=0.35).move_to(RIGHT * 3.5 + UP * 0.8)

        infer_cost = Text("Frações de centavo", font_size=34, color=GREEN, weight=BOLD)
        infer_cost.move_to(RIGHT * 3.5 + DOWN * 0.8)

        infer_speed = Text("< 1 segundo", font_size=34, color=GREEN, weight=BOLD)
        infer_speed.move_to(RIGHT * 3.5 + DOWN * 1.7)

        self.play(
            LaggedStart(
                *[FadeIn(t, shift=RIGHT * 0.2) for t in train_details],
                lag_ratio=0.2, run_time=0.8,
            )
        )
        self.play(FadeIn(train_cost_gpt3), run_time=0.4)
        self.play(FadeIn(train_cost_gpt4), run_time=0.4)
        self.wait(0.5)

        self.play(
            LaggedStart(
                *[FadeIn(t, shift=LEFT * 0.2) for t in infer_details],
                lag_ratio=0.2, run_time=0.8,
            )
        )
        self.play(FadeIn(infer_cost), run_time=0.4)
        self.play(FadeIn(infer_speed), run_time=0.4)
        self.wait(1.5)

        # Scale / balance animation
        balance_label = Text(
            "Treinamento é caro UMA VEZ.\nInferência precisa ser barata SEMPRE.",
            font_size=30, color=YELLOW, line_spacing=1.3,
        )
        balance_label.move_to(DOWN * 2.8)
        self.play(Write(balance_label), run_time=1.0)
        self.wait(2.5)

        all_objs = VGroup(
            seg_title, left_bg, right_bg,
            lbl_train, lbl_infer,
            train_details, train_cost_gpt3, train_cost_gpt4,
            infer_details, infer_cost, infer_speed,
            balance_label,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 3 — O PROBLEMA DO PREÇO
    # ======================================================================
    def _seg3_price_problem(self):
        seg_title = self._section_title("O Problema: custos proibitivos")
        self.wait(0.5)

        # Calculator summing costs
        costs = [
            ("Ler um livro",         "$5,00",      5),
            ("Chatbot pessoal/mês",  "$2.400,00",  2400),
            ("Assistente de código", "$15.000,00", 15000),
        ]

        running_total = 0
        cost_objs = []
        total_text = None

        for label, price_str, price_val in costs:
            lbl_obj = Text(f"• {label}", font_size=34, color=WHITE)
            price_obj = Text(price_str, font_size=34, color=RED, weight=BOLD)
            row = VGroup(lbl_obj, price_obj)
            row.arrange(RIGHT, buff=0.5)

            if cost_objs:
                row.next_to(cost_objs[-1], DOWN, buff=0.45)
            else:
                row.move_to(UP * 1.5)

            self.play(FadeIn(row, shift=LEFT * 0.3), run_time=0.5)

            # Pulse the price in red
            self.play(price_obj.animate.scale(1.15), run_time=0.2)
            self.play(price_obj.animate.scale(1 / 1.15), run_time=0.2)
            cost_objs.append(row)

            running_total += price_val

        # Running total
        total_val = Text(
            f"Total: ${running_total:,.2f}/mês",
            font_size=42, color=RED, weight=BOLD,
        )
        total_val.next_to(cost_objs[-1], DOWN, buff=0.7)
        total_text = total_val

        self.play(Write(total_val), run_time=0.6)
        self.wait(1.0)

        # Pulse all red numbers
        red_nums = VGroup(*[row[1] for row in cost_objs], total_val)
        for _ in range(2):
            self.play(red_nums.animate.set_color(ORANGE), run_time=0.25)
            self.play(red_nums.animate.set_color(RED),    run_time=0.25)

        self.wait(0.5)

        # Explode into particles → clean screen → "AS OTIMIZAÇÕES"
        all_cost_group = VGroup(*cost_objs, total_val)
        # Scatter effect
        self.play(
            LaggedStart(
                *[
                    FadeOut(obj, shift=np.array([
                        np.random.uniform(-4, 4),
                        np.random.uniform(-3, 3),
                        0,
                    ]))
                    for obj in list(all_cost_group)
                ],
                lag_ratio=0.12,
                run_time=0.8,
            )
        )

        # Big reveal
        reveal = Text("AS OTIMIZAÇÕES", font_size=80, color=C_GOOD, weight=BOLD)
        reveal.move_to(ORIGIN)

        self.play(FadeOut(seg_title), run_time=0.3)
        self.play(FadeIn(reveal, scale=0.7), run_time=0.8)
        self.wait(1.5)

        sub = Text(
            "7 técnicas que reduziram o custo em 1000x",
            font_size=34, color=WHITE,
        )
        sub.next_to(reveal, DOWN, buff=0.5)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.6)
        self.wait(2.0)
        self.play(FadeOut(VGroup(reveal, sub)), run_time=0.6)

    # ======================================================================
    # SEG 4 — QUANTIZAÇÃO
    # ======================================================================
    def _seg4_quantization(self):
        seg_title = self._section_title("Técnica 1: Quantização")
        self.wait(0.5)

        # Show bit blocks for each precision
        precisions = [
            ("FP32", 32, RED,    "Padrão — 4 bytes"),
            ("FP16", 16, ORANGE, "Metade — 2 bytes"),
            ("INT8",  8, YELLOW, "Um quarto — 1 byte"),
            ("INT4",  4, GREEN,  "Um oitavo — 0,5 byte"),
        ]

        bit_groups = VGroup()
        labels_grp = VGroup()
        desc_grp   = VGroup()

        row_y = [1.8, 0.5, -0.8, -2.1]

        for i, (name, bits, color, desc) in enumerate(precisions):
            y = row_y[i]

            name_lbl = Text(name, font_size=34, color=color, weight=BOLD)
            name_lbl.move_to(LEFT * 5.8 + UP * y)

            # Bit blocks
            block_grp = VGroup()
            for b in range(bits):
                block = Rectangle(
                    width=0.28, height=0.42,
                    color=color,
                    fill_color=color,
                    fill_opacity=0.7,
                    stroke_width=1.0,
                )
                block_grp.add(block)
            block_grp.arrange(RIGHT, buff=0.04)

            # Clamp to max width
            max_w = 7.0
            if block_grp.width > max_w:
                block_grp.scale(max_w / block_grp.width)

            block_grp.move_to(LEFT * 0.8 + UP * y)

            desc_lbl = Text(desc, font_size=24, color=C_DIM)
            desc_lbl.move_to(RIGHT * 5.0 + UP * y)

            bit_groups.add(block_grp)
            labels_grp.add(name_lbl)
            desc_grp.add(desc_lbl)

        # Animate each row
        for i in range(4):
            self.play(
                FadeIn(labels_grp[i]),
                LaggedStart(
                    *[FadeIn(b, scale=0.5) for b in bit_groups[i]],
                    lag_ratio=0.03,
                    run_time=0.5,
                ),
                FadeIn(desc_grp[i]),
                run_time=0.6,
            )
            self.wait(0.4)

        self.wait(1.0)

        # Dramatic comparison: 70B model sizes
        self.play(
            FadeOut(VGroup(bit_groups, labels_grp, desc_grp)),
            run_time=0.5,
        )

        compare_title = Text("Modelo 70B — comparação de tamanho", font_size=34, color=WHITE)
        compare_title.move_to(UP * 3.0)
        self.play(FadeIn(compare_title), run_time=0.4)

        fp32_label = Text("70B FP32", font_size=40, color=RED, weight=BOLD)
        fp32_label.move_to(LEFT * 4.5 + UP * 1.0)

        fp32_size = Text("= 280 GB", font_size=48, color=RED, weight=BOLD)
        fp32_size.next_to(fp32_label, DOWN, buff=0.3)

        fp32_note = Text("Precisa de 4 GPUs A100", font_size=26, color=C_DIM)
        fp32_note.next_to(fp32_size, DOWN, buff=0.25)

        arrow_right = Arrow(LEFT * 1.0, RIGHT * 1.0, color=YELLOW, stroke_width=3)
        arrow_right.move_to(ORIGIN + UP * 1.0)

        int4_label = Text("70B INT4", font_size=40, color=GREEN, weight=BOLD)
        int4_label.move_to(RIGHT * 4.5 + UP * 1.0)

        int4_size = Text("= 35 GB", font_size=48, color=GREEN, weight=BOLD)
        int4_size.next_to(int4_label, DOWN, buff=0.3)

        int4_note = Text("Cabe em 1 GPU consumer!", font_size=26, color=GREEN)
        int4_note.next_to(int4_size, DOWN, buff=0.25)

        self.play(FadeIn(fp32_label), FadeIn(fp32_size), run_time=0.5)
        self.play(FadeIn(fp32_note), run_time=0.4)
        self.play(GrowArrow(arrow_right), run_time=0.5)
        self.play(FadeIn(int4_label), FadeIn(int4_size), run_time=0.5)
        self.play(FadeIn(int4_note), run_time=0.4)
        self.wait(1.0)

        # Quality bar comparison
        qual_title = Text("Qualidade preservada:", font_size=30, color=WHITE)
        qual_title.move_to(DOWN * 1.2 + LEFT * 3.5)

        # FP32 quality bar
        q32_bg = make_bar(5.0, 0.4, GREY_D, fill_op=0.4)
        q32_fill = make_bar(5.0, 0.4, RED, fill_op=0.8)
        q32_fill.align_to(q32_bg, LEFT)
        q32 = VGroup(q32_bg, q32_fill).move_to(DOWN * 1.9 + LEFT * 0.5)
        q32_lbl = Text("FP32: 100%", font_size=26, color=RED)
        q32_lbl.next_to(q32, RIGHT, buff=0.2)

        q4_bg = make_bar(5.0, 0.4, GREY_D, fill_op=0.4)
        q4_fill = make_bar(4.85, 0.4, GREEN, fill_op=0.8)
        q4_fill.align_to(q4_bg, LEFT)
        q4 = VGroup(q4_bg, q4_fill).move_to(DOWN * 2.7 + LEFT * 0.5)
        q4_lbl = Text("INT4: ~97%", font_size=26, color=GREEN)
        q4_lbl.next_to(q4, RIGHT, buff=0.2)

        self.play(FadeIn(qual_title), run_time=0.3)
        self.play(FadeIn(q32), FadeIn(q32_lbl), run_time=0.4)
        self.play(FadeIn(q4),  FadeIn(q4_lbl),  run_time=0.4)
        self.wait(2.0)

        all_objs = VGroup(
            seg_title, compare_title,
            fp32_label, fp32_size, fp32_note,
            arrow_right,
            int4_label, int4_size, int4_note,
            qual_title, q32, q32_lbl, q4, q4_lbl,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 5 — DESTILAÇÃO
    # ======================================================================
    def _seg5_distillation(self):
        seg_title = self._section_title("Técnica 2: Destilação")
        self.wait(0.5)

        # Teacher model (large circle)
        teacher_circle = Circle(
            radius=1.5, color=YELLOW,
            fill_color=YELLOW, fill_opacity=0.15, stroke_width=3,
        )
        teacher_circle.move_to(LEFT * 4.0 + UP * 0.5)

        teacher_label = Text("Modelo Professor", font_size=28, color=YELLOW, weight=BOLD)
        teacher_label.move_to(teacher_circle.get_center() + UP * 0.2)

        teacher_size = Text("GPT-4\n(enorme)", font_size=24, color=YELLOW)
        teacher_size.move_to(teacher_circle.get_center() + DOWN * 0.4)

        # Student model (smaller circle)
        student_circle = Circle(
            radius=0.8, color=C_TECH,
            fill_color=C_TECH, fill_opacity=0.15, stroke_width=3,
        )
        student_circle.move_to(RIGHT * 4.0 + UP * 0.5)

        student_label = Text("Modelo Aluno", font_size=28, color=C_TECH, weight=BOLD)
        student_label.move_to(student_circle.get_center() + UP * 0.2)

        student_size = Text("GPT-4o-mini\n(pequeno)", font_size=22, color=C_TECH)
        student_size.move_to(student_circle.get_center() + DOWN * 0.3)

        # Arrow: teacher → student
        arrow_teach = Arrow(
            start=teacher_circle.get_right() + RIGHT * 0.1,
            end=student_circle.get_left() + LEFT * 0.1,
            color=C_GOOD, stroke_width=3,
        )
        arrow_label = Text("aprende a imitar", font_size=26, color=C_GOOD)
        arrow_label.next_to(arrow_teach, UP, buff=0.15)

        self.play(
            Create(teacher_circle),
            FadeIn(teacher_label), FadeIn(teacher_size),
            run_time=0.7,
        )
        self.play(
            Create(student_circle),
            FadeIn(student_label), FadeIn(student_size),
            run_time=0.6,
        )
        self.play(GrowArrow(arrow_teach), FadeIn(arrow_label), run_time=0.6)
        self.wait(0.8)

        # Student progress bar
        progress_bg = make_bar(5.0, 0.45, GREY_D, fill_op=0.5)
        progress_bg.move_to(DOWN * 1.5)

        progress_fill = make_bar(0.1, 0.45, C_TECH, fill_op=0.85)
        progress_fill.align_to(progress_bg, LEFT)

        prog_label = Text("Aprendizado do aluno", font_size=26, color=C_DIM)
        prog_label.next_to(progress_bg, UP, buff=0.15)

        self.play(FadeIn(progress_bg), FadeIn(prog_label), run_time=0.4)
        self.play(FadeIn(progress_fill), run_time=0.3)

        # Grow progress bar
        for target_w in [1.5, 2.8, 4.0, 5.0]:
            self.play(
                progress_fill.animate.set_width(target_w).align_to(progress_bg, LEFT),
                run_time=0.35,
            )

        # Student grows (scales up a bit)
        self.play(
            student_circle.animate.scale(1.25),
            run_time=0.5,
        )
        self.wait(0.8)

        # Show model logos with parent arrows
        self.play(
            FadeOut(VGroup(
                teacher_circle, teacher_label, teacher_size,
                student_circle, student_label, student_size,
                arrow_teach, arrow_label,
                progress_bg, progress_fill, prog_label,
            )),
            run_time=0.5,
        )

        examples_title = Text("Exemplos reais de destilação:", font_size=34, color=WHITE)
        examples_title.move_to(UP * 2.5)
        self.play(FadeIn(examples_title), run_time=0.4)

        distill_examples = [
            ("GPT-4o",          "→",  "GPT-4o-mini",     YELLOW,  C_TECH),
            ("Claude 3 Opus",   "→",  "Claude Haiku",    ORANGE,  C_TEAL),
            ("Gemini 1.5 Pro",  "→",  "Gemini Flash",    BLUE,    GREEN),
        ]

        rows = VGroup()
        for parent, arrow_str, child, p_color, c_color in distill_examples:
            p_txt = Text(parent, font_size=30, color=p_color, weight=BOLD)
            a_txt = Text(arrow_str, font_size=30, color=C_DIM)
            c_txt = Text(child, font_size=30, color=c_color, weight=BOLD)
            row = VGroup(p_txt, a_txt, c_txt)
            row.arrange(RIGHT, buff=0.4)
            rows.add(row)

        rows.arrange(DOWN, buff=0.5)
        rows.move_to(ORIGIN + DOWN * 0.2)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.4)

        self.wait(1.8)

        all_objs = VGroup(seg_title, examples_title, rows)
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 6 — MIXTURE OF EXPERTS (MoE)
    # ======================================================================
    def _seg6_moe(self):
        seg_title = self._section_title("Técnica 3: Mixture of Experts (MoE)")
        self.wait(0.5)

        # Traditional model: one big block, all params active
        trad_title = Text("Modelo Tradicional", font_size=30, color=RED, weight=BOLD)
        trad_title.move_to(LEFT * 4.5 + UP * 2.8)

        trad_block = Rectangle(
            width=3.5, height=4.5,
            color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=2.5,
        )
        trad_block.move_to(LEFT * 4.5 + UP * 0.0)

        trad_lbl = Text("TODOS os\nparâmetros\nativados", font_size=26, color=RED,
                        line_spacing=1.2)
        trad_lbl.move_to(trad_block.get_center())

        trad_cost = Text("Lento e caro", font_size=24, color=RED)
        trad_cost.next_to(trad_block, DOWN, buff=0.2)

        # MoE model: 8 expert boxes, 2 highlighted
        moe_title = Text("Modelo MoE (Mixtral)", font_size=30, color=GREEN, weight=BOLD)
        moe_title.move_to(RIGHT * 3.0 + UP * 2.8)

        experts = VGroup()
        expert_colors_list = [GREY_D] * 8
        active_experts = [2, 5]
        for i in range(8):
            col = GREEN if i in active_experts else GREY_D
            fill_op = 0.6 if i in active_experts else 0.25
            exp = Rectangle(
                width=1.1, height=1.1,
                color=col, fill_color=col, fill_opacity=fill_op,
                stroke_width=1.5,
            )
            lbl_e = Text(f"E{i+1}", font_size=22, color=WHITE)
            lbl_e.move_to(exp.get_center())
            experts.add(VGroup(exp, lbl_e))

        experts.arrange_in_grid(2, 4, buff=0.18)
        experts.move_to(RIGHT * 3.0 + UP * 0.3)

        router_box = Rectangle(
            width=2.0, height=0.6,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.2, stroke_width=2,
        )
        router_box.move_to(RIGHT * 3.0 + DOWN * 2.0)
        router_lbl = Text("Router", font_size=26, color=YELLOW, weight=BOLD)
        router_lbl.move_to(router_box.get_center())

        moe_cost = Text("Apenas 2 de 8 ativados", font_size=24, color=GREEN)
        moe_cost.next_to(router_box, DOWN, buff=0.25)

        # Token input
        token_box = RoundedRectangle(
            width=1.5, height=0.55,
            corner_radius=0.1,
            color=C_TECH, fill_color=C_TECH,
            fill_opacity=0.7, stroke_width=1.5,
        )
        tok_lbl_text = Text("token", font_size=22, color=WHITE)
        tok_lbl_text.move_to(token_box.get_center())
        token_input = VGroup(token_box, tok_lbl_text)
        token_input.move_to(RIGHT * 3.0 + DOWN * 3.2)

        self.play(
            FadeIn(trad_title), Create(trad_block),
            FadeIn(trad_lbl), FadeIn(trad_cost),
            run_time=0.7,
        )
        self.wait(0.5)

        self.play(
            FadeIn(moe_title),
            LaggedStart(*[FadeIn(e, scale=0.8) for e in experts], lag_ratio=0.07, run_time=0.7),
            run_time=0.8,
        )

        self.play(
            Create(router_box), FadeIn(router_lbl), FadeIn(moe_cost),
            run_time=0.5,
        )
        self.play(FadeIn(token_input), run_time=0.4)

        # Arrow: token → router → active experts
        arr_tok_router = Arrow(
            start=token_input.get_top() + UP * 0.05,
            end=router_box.get_bottom() + DOWN * 0.05,
            color=YELLOW, stroke_width=2.5, buff=0.05,
        )
        self.play(GrowArrow(arr_tok_router), run_time=0.5)
        self.wait(0.5)

        # Highlight active experts with arrows from router
        expert_arrows = VGroup()
        for idx in active_experts:
            arr = Arrow(
                start=router_box.get_top(),
                end=experts[idx].get_bottom(),
                color=GREEN, stroke_width=2.0, buff=0.05,
            )
            expert_arrows.add(arr)
            self.play(Create(arr), run_time=0.3)
            self.play(experts[idx].animate.set_stroke(GREEN, width=4), run_time=0.2)

        self.wait(1.0)

        # Mixtral stats
        stats = Text(
            "Mixtral 8x7B: 47B total, 13B ativos por token",
            font_size=28, color=YELLOW,
        )
        stats.move_to(DOWN * 3.5)
        self.play(Write(stats), run_time=0.8)
        self.wait(2.0)

        all_objs = VGroup(
            seg_title,
            trad_title, trad_block, trad_lbl, trad_cost,
            moe_title, experts, router_box, router_lbl, moe_cost,
            token_input, arr_tok_router, expert_arrows,
            stats,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 7 — FLASH ATTENTION & KV CACHE
    # ======================================================================
    def _seg7_flash_attention(self):
        seg_title = self._section_title("Técnicas 4 & 5: Flash Attention e KV Cache")
        self.wait(0.5)

        # --- Flash Attention: conveyor belt analogy ---
        fa_title = Text("Flash Attention", font_size=36, color=YELLOW, weight=BOLD)
        fa_title.move_to(UP * 2.8)
        self.play(FadeIn(fa_title), run_time=0.4)

        # Old method: giant pile → overflow
        old_lbl = Text("Método antigo: tudo na memória", font_size=28, color=RED)
        old_lbl.move_to(LEFT * 3.5 + UP * 1.4)

        old_pile = VGroup()
        for i in range(6):
            block = Rectangle(
                width=1.8, height=0.4,
                color=RED, fill_color=RED, fill_opacity=0.4 + i * 0.05,
                stroke_width=1.2,
            )
            old_pile.add(block)
        old_pile.arrange(UP, buff=0.04)
        old_pile.move_to(LEFT * 3.5 + DOWN * 0.1)

        overflow = Text("OVERFLOW!", font_size=28, color=RED, weight=BOLD)
        overflow.next_to(old_pile, UP, buff=0.1)

        self.play(FadeIn(old_lbl), run_time=0.3)
        self.play(
            LaggedStart(*[FadeIn(b) for b in old_pile], lag_ratio=0.1, run_time=0.6)
        )
        self.play(Write(overflow), run_time=0.3)
        self.wait(0.6)

        # New method: process in small blocks
        new_lbl = Text("Flash Attention: blocos pequenos", font_size=28, color=GREEN)
        new_lbl.move_to(RIGHT * 3.5 + UP * 1.4)

        new_blocks = VGroup()
        for i in range(3):
            block = Rectangle(
                width=1.8, height=0.4,
                color=GREEN, fill_color=GREEN, fill_opacity=0.6,
                stroke_width=1.2,
            )
            new_blocks.add(block)
        new_blocks.arrange(UP, buff=0.04)
        new_blocks.move_to(RIGHT * 3.5 + DOWN * 0.9)

        ok_label = Text("Cabe na SRAM\n(ultra-rápida)", font_size=24, color=GREEN,
                        line_spacing=1.2)
        ok_label.next_to(new_blocks, UP, buff=0.1)

        self.play(FadeIn(new_lbl), run_time=0.3)
        for blk in new_blocks:
            self.play(FadeIn(blk, shift=LEFT * 0.2), run_time=0.2)
        self.play(FadeIn(ok_label), run_time=0.3)
        self.wait(0.8)

        speedup_lbl = Text("Flash Attention: 2-4x mais rápido, mesmos resultados",
                           font_size=28, color=YELLOW)
        speedup_lbl.move_to(DOWN * 2.5)
        self.play(Write(speedup_lbl), run_time=0.7)
        self.wait(1.5)

        self.play(
            FadeOut(VGroup(
                fa_title, old_lbl, old_pile, overflow,
                new_lbl, new_blocks, ok_label, speedup_lbl,
            )),
            run_time=0.5,
        )

        # --- KV Cache ---
        kv_title = Text("KV Cache", font_size=36, color=YELLOW, weight=BOLD)
        kv_title.move_to(UP * 2.8)
        self.play(FadeIn(kv_title), run_time=0.4)

        # Without cache: redundant arrows
        no_cache_lbl = Text("Sem cache: recalcula tudo a cada token", font_size=26, color=RED)
        no_cache_lbl.move_to(LEFT * 3.5 + UP * 1.6)

        token_seq_no = self._make_token_seq(["Eu", "gosto", "de"], colors=[BLUE, BLUE, BLUE])
        token_seq_no.move_to(LEFT * 3.5 + UP * 0.5)

        arrows_no = VGroup()
        for tok in token_seq_no:
            arr = Arrow(
                start=tok.get_bottom() + DOWN * 0.05,
                end=tok.get_bottom() + DOWN * 0.7,
                color=RED, stroke_width=2, buff=0.05,
            )
            arrows_no.add(arr)

        self.play(FadeIn(no_cache_lbl), FadeIn(token_seq_no), run_time=0.4)
        self.play(LaggedStart(*[GrowArrow(a) for a in arrows_no], lag_ratio=0.2, run_time=0.6))
        self.wait(0.6)

        # With cache: only new token has arrow
        cache_lbl = Text("Com cache: calcula só o novo token", font_size=26, color=GREEN)
        cache_lbl.move_to(RIGHT * 3.5 + UP * 1.6)

        token_seq_yes = self._make_token_seq(
            ["Eu", "gosto", "de", "IA"],
            colors=[GREY_D, GREY_D, GREY_D, GREEN],
        )
        token_seq_yes.move_to(RIGHT * 3.0 + UP * 0.5)

        cache_box = Rectangle(
            width=2.0, height=0.8,
            color=GREY_D, fill_color=GREY_D, fill_opacity=0.3, stroke_width=1.5,
        )
        cache_box.move_to(RIGHT * 3.0 + DOWN * 0.15)
        cache_box_lbl = Text("cache", font_size=20, color=GREY_B)
        cache_box_lbl.move_to(cache_box.get_center())

        new_arrow = Arrow(
            start=token_seq_yes[3].get_bottom() + DOWN * 0.05,
            end=token_seq_yes[3].get_bottom() + DOWN * 0.7,
            color=GREEN, stroke_width=3, buff=0.05,
        )

        self.play(FadeIn(cache_lbl), FadeIn(token_seq_yes), run_time=0.4)
        self.play(FadeIn(cache_box), FadeIn(cache_box_lbl), run_time=0.3)
        self.play(GrowArrow(new_arrow), run_time=0.4)
        self.wait(1.5)

        cache_benefit = Text("KV Cache: evita recomputação →  latência 10x menor",
                             font_size=26, color=YELLOW)
        cache_benefit.move_to(DOWN * 2.5)
        self.play(Write(cache_benefit), run_time=0.7)
        self.wait(2.0)

        all_objs = VGroup(
            seg_title, kv_title,
            no_cache_lbl, token_seq_no, arrows_no,
            cache_lbl, token_seq_yes, cache_box, cache_box_lbl, new_arrow,
            cache_benefit,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    def _make_token_seq(self, tokens, colors):
        bar = VGroup()
        for i, (tok, col) in enumerate(zip(tokens, colors)):
            lbl = Text(tok, font_size=24, color=WHITE)
            rect = RoundedRectangle(
                width=max(lbl.width + 0.3, 0.7),
                height=0.55,
                corner_radius=0.1,
                color=col, fill_color=col,
                fill_opacity=0.7, stroke_width=1.5,
            )
            lbl.move_to(rect.get_center())
            bar.add(VGroup(rect, lbl))
        bar.arrange(RIGHT, buff=0.08)
        return bar

    # ======================================================================
    # SEG 8 — CHINCHILLA
    # ======================================================================
    def _seg8_chinchilla(self):
        seg_title = self._section_title("Técnica 6: Leis de Escalonamento (Chinchilla)")
        self.wait(0.5)

        # Axes
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 10, 2],
            x_length=7,
            y_length=5,
            axis_config={"color": GREY_B, "stroke_width": 1.5},
            tips=False,
        )
        axes.move_to(ORIGIN + LEFT * 1.0 + DOWN * 0.3)

        x_label = Text("Parâmetros do modelo →", font_size=24, color=C_DIM)
        x_label.next_to(axes, DOWN, buff=0.2)

        y_label = Text("Tokens de treino →", font_size=24, color=C_DIM)
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.8)

        # Chinchilla optimal frontier curve
        chinchilla_curve = axes.plot(
            lambda x: x,
            x_range=[0.5, 9],
            color=GREEN,
            stroke_width=3,
        )
        curve_label = Text("Frontier Chinchilla\n(ótimo)", font_size=22, color=GREEN)
        curve_label.move_to(axes.c2p(9, 8.5))

        self.play(Create(chinchilla_curve), FadeIn(curve_label), run_time=0.8)
        self.wait(0.5)

        # GPT-3 point: high params, few tokens (above line = suboptimal)
        gpt3_point = Dot(axes.c2p(7, 3), color=RED, radius=0.15)
        gpt3_label = Text("GPT-3\n(175B params,\n300B tokens)", font_size=20, color=RED,
                          line_spacing=1.2)
        gpt3_label.next_to(gpt3_point, RIGHT, buff=0.15)

        self.play(FadeIn(gpt3_point, scale=0.5), FadeIn(gpt3_label), run_time=0.5)

        # Annotation: suboptimal
        subopt = Text("Subótimo!\nMuitos params,\npoucos tokens", font_size=20, color=RED,
                      line_spacing=1.2)
        subopt.next_to(gpt3_point, LEFT + UP, buff=0.25)
        subopt_arrow = Arrow(subopt.get_right(), gpt3_point.get_center(),
                             color=RED, stroke_width=2, buff=0.05)
        self.play(FadeIn(subopt), Create(subopt_arrow), run_time=0.5)
        self.wait(0.8)

        # LLaMA point: on the line (optimal)
        llama_point = Dot(axes.c2p(5, 5.2), color=GREEN, radius=0.15)
        llama_label = Text("LLaMA\n(65B params,\n1.4T tokens)", font_size=20, color=GREEN,
                           line_spacing=1.2)
        llama_label.next_to(llama_point, LEFT + DOWN, buff=0.15)

        optimal_lbl = Text("(ótimo!)", font_size=20, color=GREEN)
        optimal_lbl.next_to(llama_label, RIGHT, buff=0.1)

        self.play(FadeIn(llama_point, scale=0.5), FadeIn(llama_label), FadeIn(optimal_lbl), run_time=0.5)
        self.wait(0.5)

        # Comparison table
        compare = VGroup(
            Text("GPT-3:  175B params, 300B tokens  →  $4,6M", font_size=22, color=RED),
            Text("LLaMA: 65B params,  1,4T tokens   →  muito mais barato", font_size=22, color=GREEN),
        ).arrange(DOWN, buff=0.35).move_to(RIGHT * 4.5 + DOWN * 0.3)

        self.play(
            LaggedStart(*[FadeIn(t, shift=LEFT * 0.2) for t in compare],
                        lag_ratio=0.3, run_time=0.8)
        )
        self.wait(2.0)

        all_objs = VGroup(
            seg_title, axes, x_label, y_label,
            chinchilla_curve, curve_label,
            gpt3_point, gpt3_label, subopt, subopt_arrow,
            llama_point, llama_label, optimal_lbl,
            compare,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 9 — HARDWARE
    # ======================================================================
    def _seg9_hardware(self):
        seg_title = self._section_title("Fator Extra: Hardware")
        self.wait(0.5)

        # Timeline
        timeline = Line(LEFT * 5.5, RIGHT * 5.5, color=GREY_B, stroke_width=2)
        timeline.move_to(UP * 0.5)
        self.play(Create(timeline), run_time=0.5)

        milestones = [
            ("A100",  "2020",  "Baseline",         RED,    LEFT * 4.0 + UP * 0.5),
            ("H100",  "2022",  "3x mais rápido",   YELLOW, ORIGIN + UP * 0.5),
            ("B200",  "2024",  "2.5x mais rápido", GREEN,  RIGHT * 4.0 + UP * 0.5),
        ]

        all_hw = VGroup()
        for chip, year, desc, color, pos in milestones:
            dot = Dot(pos, color=color, radius=0.15)
            chip_lbl = Text(chip, font_size=30, color=color, weight=BOLD)
            chip_lbl.next_to(dot, UP, buff=0.25)
            year_lbl = Text(year, font_size=22, color=C_DIM)
            year_lbl.next_to(chip_lbl, UP, buff=0.12)
            desc_lbl = Text(desc, font_size=22, color=color)
            desc_lbl.next_to(dot, DOWN, buff=0.3)

            self.play(
                FadeIn(dot, scale=0.5),
                FadeIn(chip_lbl), FadeIn(year_lbl), FadeIn(desc_lbl),
                run_time=0.5,
            )
            all_hw.add(dot, chip_lbl, year_lbl, desc_lbl)
            self.wait(0.4)

        self.wait(0.8)

        # Progress bar: hardware contribution
        hw_label = Text("Contribuição do hardware:", font_size=28, color=WHITE)
        hw_label.move_to(LEFT * 3.0 + DOWN * 1.8)

        hw_bg = make_bar(8.0, 0.5, GREY_D, fill_op=0.4)
        hw_bg.move_to(RIGHT * 0.5 + DOWN * 2.5)

        hw_fill = make_bar(0.1, 0.5, C_TECH, fill_op=0.85)
        hw_fill.align_to(hw_bg, LEFT)

        hw_pct = Text("0%", font_size=24, color=C_TECH)
        hw_pct.next_to(hw_bg, RIGHT, buff=0.2)

        # Software contribution
        sw_label = Text("Contribuição do software:", font_size=28, color=WHITE)
        sw_label.move_to(LEFT * 3.0 + DOWN * 2.7)

        sw_bg = make_bar(8.0, 0.5, GREY_D, fill_op=0.4)
        sw_bg.move_to(RIGHT * 0.5 + DOWN * 3.4)

        sw_fill = make_bar(0.1, 0.5, GREEN, fill_op=0.85)
        sw_fill.align_to(sw_bg, LEFT)

        sw_pct = Text("0%", font_size=24, color=GREEN)
        sw_pct.next_to(sw_bg, RIGHT, buff=0.2)

        self.play(
            FadeIn(hw_label), FadeIn(hw_bg), FadeIn(hw_fill), FadeIn(hw_pct),
            FadeIn(sw_label), FadeIn(sw_bg), FadeIn(sw_fill), FadeIn(sw_pct),
            run_time=0.4,
        )

        # Animate bars
        hw_target_w = 8.0 * (5 / 1000)  # hardware ~4-5x out of 1000x
        sw_target_w = 8.0 * 0.995        # software ~995x out of 1000x

        new_hw_pct = Text("~0.5%", font_size=24, color=C_TECH)
        new_hw_pct.next_to(hw_bg, RIGHT, buff=0.2)

        new_sw_pct = Text("~99.5%", font_size=24, color=GREEN)
        new_sw_pct.next_to(sw_bg, RIGHT, buff=0.2)

        self.play(
            hw_fill.animate.set_width(max(hw_target_w, 0.1)).align_to(hw_bg, LEFT),
            FadeOut(hw_pct), FadeIn(new_hw_pct),
            run_time=0.6,
        )
        self.play(
            sw_fill.animate.set_width(sw_target_w).align_to(sw_bg, LEFT),
            FadeOut(sw_pct), FadeIn(new_sw_pct),
            run_time=1.2,
        )
        self.wait(1.0)

        note = Text(
            "Hardware: 4-5x mais rápido  |  Software: 200x mais eficiente  |  Total: 1000x",
            font_size=24, color=YELLOW,
        )
        note.move_to(DOWN * 3.8)
        self.play(Write(note), run_time=0.8)
        self.wait(2.0)

        all_objs = VGroup(
            seg_title, timeline, all_hw,
            hw_label, hw_bg, hw_fill, new_hw_pct,
            sw_label, sw_bg, sw_fill, new_sw_pct,
            note,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 10 — SPECULATIVE DECODING & BATCHING
    # ======================================================================
    def _seg10_speculative(self):
        seg_title = self._section_title("Técnica 7: Decodificação Especulativa")
        self.wait(0.5)

        # Small model (blue) generates drafts
        small_model = RoundedRectangle(
            width=2.5, height=1.2,
            corner_radius=0.2,
            color=C_TECH, fill_color=C_TECH, fill_opacity=0.2, stroke_width=2.5,
        )
        small_model.move_to(LEFT * 4.5 + UP * 1.5)
        sm_lbl = Text("Modelo\nPequeno", font_size=24, color=C_TECH, line_spacing=1.2)
        sm_lbl.move_to(small_model.get_center())
        sm_speed = Text("rápido", font_size=20, color=C_TECH)
        sm_speed.next_to(small_model, DOWN, buff=0.1)

        # Draft tokens (5 boxes)
        draft_tokens = self._make_token_seq(
            ["Eu", "gosto", "de", "IA", "muito"],
            colors=[C_TECH] * 5,
        )
        draft_tokens.move_to(ORIGIN + UP * 1.5)

        draft_label = Text("5 rascunhos gerados", font_size=24, color=C_TECH)
        draft_label.next_to(draft_tokens, UP, buff=0.15)

        self.play(
            FadeIn(small_model), FadeIn(sm_lbl), FadeIn(sm_speed),
            run_time=0.5,
        )
        self.play(FadeIn(draft_label), run_time=0.3)
        self.play(
            LaggedStart(*[FadeIn(t, scale=0.7) for t in draft_tokens],
                        lag_ratio=0.1, run_time=0.6)
        )
        self.wait(0.5)

        # Arrow to large model
        large_model = RoundedRectangle(
            width=2.5, height=1.2,
            corner_radius=0.2,
            color=GREEN, fill_color=GREEN, fill_opacity=0.2, stroke_width=2.5,
        )
        large_model.move_to(RIGHT * 4.5 + UP * 1.5)
        lg_lbl = Text("Modelo\nGrande", font_size=24, color=GREEN, line_spacing=1.2)
        lg_lbl.move_to(large_model.get_center())
        lg_verify = Text("verifica todos\nde uma vez", font_size=20, color=GREEN,
                         line_spacing=1.2)
        lg_verify.next_to(large_model, DOWN, buff=0.1)

        arr_to_large = Arrow(
            start=draft_tokens.get_right() + RIGHT * 0.1,
            end=large_model.get_left() + LEFT * 0.1,
            color=YELLOW, stroke_width=2.5, buff=0.05,
        )

        self.play(
            GrowArrow(arr_to_large),
            FadeIn(large_model), FadeIn(lg_lbl), FadeIn(lg_verify),
            run_time=0.6,
        )
        self.wait(0.5)

        # Accept 4, reject 1
        accepted_tokens = self._make_token_seq(
            ["Eu", "gosto", "de", "IA"],
            colors=[GREEN] * 4,
        )
        accepted_tokens.move_to(LEFT * 1.5 + DOWN * 0.3)

        rejected_token = self._make_token_seq(["muito"], colors=[RED])
        rejected_token.move_to(RIGHT * 2.5 + DOWN * 0.3)

        accept_lbl = Text("4 aceitos", font_size=24, color=GREEN)
        accept_lbl.next_to(accepted_tokens, UP, buff=0.12)

        reject_lbl = Text("1 rejeitado", font_size=24, color=RED)
        reject_lbl.next_to(rejected_token, UP, buff=0.12)

        result_note = Text(
            "Resultado: 4x mais rápido que gerar um por um",
            font_size=26, color=YELLOW,
        )
        result_note.move_to(DOWN * 1.5)

        self.play(
            LaggedStart(*[FadeIn(t) for t in accepted_tokens], lag_ratio=0.1, run_time=0.5),
            FadeIn(accept_lbl),
        )
        self.play(FadeIn(rejected_token), FadeIn(reject_lbl), run_time=0.4)
        self.play(Write(result_note), run_time=0.6)
        self.wait(1.0)

        # Other inference techniques
        self.play(
            FadeOut(VGroup(
                small_model, sm_lbl, sm_speed,
                draft_tokens, draft_label,
                arr_to_large,
                large_model, lg_lbl, lg_verify,
                accepted_tokens, accept_lbl,
                rejected_token, reject_lbl,
                result_note,
            )),
            run_time=0.5,
        )

        other_techs_title = Text("Outras técnicas de inferência:", font_size=32, color=WHITE)
        other_techs_title.move_to(UP * 2.0)
        self.play(FadeIn(other_techs_title), run_time=0.4)

        techs = VGroup(
            VGroup(
                Text("Batching:", font_size=28, color=YELLOW, weight=BOLD),
                Text("processar múltiplas requisições juntas", font_size=26, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Paralelismo de modelo:", font_size=28, color=YELLOW, weight=BOLD),
                Text("distribuir entre várias GPUs", font_size=26, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("Continuous Batching:", font_size=28, color=YELLOW, weight=BOLD),
                Text("trocar pedidos concluídos em tempo real", font_size=26, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
        )
        techs.arrange(DOWN, buff=0.5)
        techs.move_to(ORIGIN + DOWN * 0.3)

        for tech in techs:
            self.play(FadeIn(tech, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.5)

        self.wait(1.5)

        all_objs = VGroup(seg_title, other_techs_title, techs)
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 11 — LINHA DO TEMPO DE PREÇOS
    # ======================================================================
    def _seg11_price_timeline(self):
        seg_title = self._section_title("A Queda de Preços em Perspectiva")
        self.wait(0.5)

        # Axes for price over time
        axes = Axes(
            x_range=[2020, 2025.5, 1],
            y_range=[0, 65, 10],
            x_length=10,
            y_length=5.5,
            axis_config={"color": GREY_B, "stroke_width": 1.5},
            tips=False,
        )
        axes.move_to(ORIGIN + DOWN * 0.3)

        x_label = Text("Ano", font_size=24, color=C_DIM)
        x_label.next_to(axes, DOWN, buff=0.2)

        y_label = Text("$ por 1M tokens", font_size=24, color=C_DIM)
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.2)

        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.7)

        # Year labels on x-axis
        year_labels = VGroup()
        for year in [2020, 2021, 2022, 2023, 2024, 2025]:
            lbl = Text(str(year), font_size=18, color=C_DIM)
            lbl.next_to(axes.c2p(year, 0), DOWN, buff=0.2)
            year_labels.add(lbl)
        self.add(year_labels)

        # Proprietary model price points (top track)
        prop_data = [
            (2020.5, 60.0, "GPT-3\n$60",   RED),
            (2022.0, 2.0,  "GPT-3.5\n$2",  ORANGE),
            (2023.0, 30.0, "GPT-4\n$30",   RED),
            (2023.7, 5.0,  "GPT-4o\n$5",   YELLOW),
            (2024.5, 0.15, "GPT-4o-mini\n$0.15", GREEN),
        ]

        prop_dots = VGroup()
        prop_labels_grp = VGroup()
        prop_lines = VGroup()
        for x, y, label, color in prop_data:
            y_clamped = min(y, 62)
            dot = Dot(axes.c2p(x, y_clamped), color=color, radius=0.12)
            lbl = Text(label, font_size=18, color=color, line_spacing=1.1)
            lbl.next_to(dot, UP, buff=0.15)
            prop_dots.add(dot)
            prop_labels_grp.add(lbl)

        # Animate points sequentially with connecting lines
        prev_dot = None
        for i, (dot, lbl) in enumerate(zip(prop_dots, prop_labels_grp)):
            self.play(FadeIn(dot, scale=0.5), FadeIn(lbl), run_time=0.4)
            if prev_dot is not None:
                line = Line(
                    prev_dot.get_center(), dot.get_center(),
                    color=GREY_B, stroke_width=1.5, stroke_opacity=0.6,
                )
                prop_lines.add(line)
                self.play(Create(line), run_time=0.3)
            prev_dot = dot
            self.wait(0.3)

        self.wait(0.8)

        # Open source disruptions (bottom annotations)
        oss_data = [
            (2023.2, 2.0,  "LLaMA",   C_TEAL),
            (2023.9, 1.5,  "Mixtral",  BLUE),
            (2025.0, 0.05, "DeepSeek", PURPLE),
        ]

        oss_title = Text("Open Source:", font_size=22, color=C_TEAL)
        oss_title.move_to(axes.c2p(2020.5, -8))
        self.play(FadeIn(oss_title), run_time=0.3)

        oss_dots = VGroup()
        for x, y, name, color in oss_data:
            oss_dot = Dot(axes.c2p(x, max(y, 0.5)), color=color, radius=0.12)
            oss_lbl = Text(name, font_size=18, color=color)
            oss_lbl.next_to(oss_dot, DOWN, buff=0.2)
            self.play(FadeIn(oss_dot, scale=0.5), FadeIn(oss_lbl), run_time=0.4)
            oss_dots.add(VGroup(oss_dot, oss_lbl))
            self.wait(0.2)

        self.wait(1.5)

        # Zoom callout: dramatic drop
        final_note = Text(
            "GPT-3 (2020): $60/1M tokens\nGPT-4o-mini (2024): $0,15/1M tokens\n→ 400x mais barato em 4 anos",
            font_size=26, color=YELLOW, line_spacing=1.3,
        )
        final_note.move_to(RIGHT * 3.5 + UP * 0.5)
        final_box = SurroundingRectangle(
            final_note, color=YELLOW, stroke_width=1.5,
            buff=0.2, corner_radius=0.1,
        )
        self.play(FadeIn(VGroup(final_note, final_box)), run_time=0.6)
        self.wait(2.5)

        all_objs = VGroup(
            seg_title, axes, x_label, y_label, year_labels,
            prop_dots, prop_labels_grp, prop_lines,
            oss_title, oss_dots,
            final_note, final_box,
        )
        self.play(FadeOut(all_objs), run_time=0.6)

    # ======================================================================
    # SEG 12 — MAIS BARATO E MELHOR (CLOSING)
    # ======================================================================
    def _seg12_closing(self):
        seg_title = self._section_title("Mais Barato E Melhor")
        self.wait(0.5)

        # Two curves on same axes
        axes = Axes(
            x_range=[2020, 2025.5, 1],
            y_range=[0, 10, 2],
            x_length=8,
            y_length=4.5,
            axis_config={"color": GREY_B, "stroke_width": 1.5},
            tips=False,
        )
        axes.move_to(ORIGIN + LEFT * 1.0 + DOWN * 0.5)

        cost_curve = axes.plot(
            lambda x: 9.5 * np.exp(-0.85 * (x - 2020)),
            x_range=[2020, 2025],
            color=RED,
            stroke_width=3,
        )
        capability_curve = axes.plot(
            lambda x: 0.5 + 1.8 * (x - 2020),
            x_range=[2020, 2025],
            color=C_TECH,
            stroke_width=3,
        )

        cost_lbl = Text("Custo ↓", font_size=26, color=RED, weight=BOLD)
        cost_lbl.move_to(axes.c2p(2020.3, 8.5))

        cap_lbl = Text("Capacidade ↑", font_size=26, color=C_TECH, weight=BOLD)
        cap_lbl.move_to(axes.c2p(2024.5, 9.5))

        self.play(Create(axes), run_time=0.6)
        self.play(Create(cost_curve), FadeIn(cost_lbl), run_time=0.8)
        self.play(Create(capability_curve), FadeIn(cap_lbl), run_time=0.8)
        self.wait(0.8)

        # "A Era Dourada" region where curves cross
        era_label = Text("A Era Dourada", font_size=34, color=YELLOW, weight=BOLD)
        era_label.move_to(axes.c2p(2023.5, 5.5))
        era_box = SurroundingRectangle(era_label, color=YELLOW, stroke_width=2,
                                       buff=0.2, corner_radius=0.12)
        self.play(FadeIn(VGroup(era_label, era_box)), run_time=0.5)
        self.wait(1.0)

        self.play(
            FadeOut(VGroup(axes, cost_curve, capability_curve,
                           cost_lbl, cap_lbl, era_label, era_box)),
            run_time=0.5,
        )

        # Virtuous cycle diagram
        cycle_title = Text("Ciclo Virtuoso", font_size=36, color=YELLOW, weight=BOLD)
        cycle_title.move_to(UP * 3.0)
        self.play(FadeIn(cycle_title), run_time=0.4)

        cycle_items = [
            "Computação mais barata",
            "Treinar modelos maiores",
            "Modelos melhores",
            "Otimizar mais",
        ]
        cycle_colors = [GREEN, C_TECH, YELLOW, C_TEAL]

        # 4 nodes in a circle
        nodes_pos = [
            UP * 1.8,
            RIGHT * 3.5,
            DOWN * 1.8,
            LEFT * 3.5,
        ]

        cycle_nodes = VGroup()
        cycle_node_texts = VGroup()
        for i, (item, color, pos) in enumerate(zip(cycle_items, cycle_colors, nodes_pos)):
            node_bg = RoundedRectangle(
                width=3.5, height=0.75,
                corner_radius=0.18,
                color=color, fill_color=color, fill_opacity=0.2,
                stroke_width=2,
            )
            node_bg.move_to(pos)
            node_txt = Text(item, font_size=24, color=color)
            node_txt.move_to(pos)
            cycle_nodes.add(node_bg)
            cycle_node_texts.add(node_txt)

        # Arrows between nodes (circular)
        cycle_arrows = VGroup()
        for i in range(4):
            next_i = (i + 1) % 4
            arr = CurvedArrow(
                nodes_pos[i] + normalize(nodes_pos[next_i] - nodes_pos[i]) * 1.8,
                nodes_pos[next_i] + normalize(nodes_pos[i] - nodes_pos[next_i]) * 1.8,
                color=GREY_A,
                stroke_width=2.0,
                angle=-TAU / 8,
            )
            cycle_arrows.add(arr)

        self.play(
            LaggedStart(*[FadeIn(n) for n in cycle_nodes], lag_ratio=0.15, run_time=0.8),
            LaggedStart(*[FadeIn(t) for t in cycle_node_texts], lag_ratio=0.15, run_time=0.8),
        )
        self.play(
            LaggedStart(*[Create(a) for a in cycle_arrows], lag_ratio=0.2, run_time=1.0)
        )
        self.wait(1.5)

        # Pulse the cycle nodes
        for _ in range(2):
            for node, txt in zip(cycle_nodes, cycle_node_texts):
                self.play(
                    node.animate.set_fill(opacity=0.5),
                    run_time=0.15,
                )
                self.play(
                    node.animate.set_fill(opacity=0.2),
                    run_time=0.15,
                )

        self.wait(0.8)
        self.play(
            FadeOut(VGroup(cycle_title, cycle_nodes, cycle_node_texts, cycle_arrows)),
            run_time=0.6,
        )

        # Closing text
        closing_line1 = Text(
            "A tecnologia mais poderosa da história",
            font_size=42, color=WHITE, weight=BOLD,
        )
        closing_line2 = Text(
            "está ficando tão barata",
            font_size=42, color=WHITE, weight=BOLD,
        )
        closing_line3 = Text(
            "quanto eletricidade.",
            font_size=46, color=YELLOW, weight=BOLD,
        )

        closing_group = VGroup(closing_line1, closing_line2, closing_line3)
        closing_group.arrange(DOWN, buff=0.5)
        closing_group.move_to(ORIGIN)

        # Letter-by-letter reveal for line1
        self.play(
            LaggedStart(
                *[FadeIn(char, shift=UP * 0.15) for char in closing_line1],
                lag_ratio=0.03,
                run_time=1.2,
            )
        )
        self.play(
            LaggedStart(
                *[FadeIn(char, shift=UP * 0.15) for char in closing_line2],
                lag_ratio=0.03,
                run_time=1.0,
            )
        )
        self.play(FadeIn(closing_line3, scale=0.9), run_time=0.7)
        self.wait(3.0)

        # Final fade to black
        self.play(
            FadeOut(VGroup(seg_title, closing_group)),
            run_time=1.2,
        )
        self.wait(0.5)

    # ======================================================================
    # Utility: section title card
    # ======================================================================
    def _section_title(self, text: str):
        title_card = Text(text, font_size=52, color=WHITE, weight=BOLD)
        title_card.move_to(ORIGIN)

        underline = Line(
            title_card.get_left() + DOWN * 0.55,
            title_card.get_right() + DOWN * 0.55,
            color=YELLOW,
            stroke_width=3,
        )

        card_group = VGroup(title_card, underline)
        self.play(FadeIn(title_card, shift=UP * 0.2), Create(underline), run_time=0.6)
        self.wait(0.8)
        self.play(card_group.animate.scale(0.55).to_edge(UP, buff=0.2), run_time=0.5)

        return card_group
