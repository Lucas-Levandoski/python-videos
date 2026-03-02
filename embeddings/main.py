from manim import *


class Main(Scene):
    def construct(self):
        ax = Axes( 
            [-5,5], [-5,5], 
            x_axis_config={ 'color': BLUE_C,  },
            y_axis_config={ 'color': RED_C },
            axis_config={ 'include_numbers': True, 'font_size': 16, 'tick_size': 0.05 }, 
            y_length=5, x_length=5, tips=False
        )

        self.play(Create(ax))
        self.wait()

        sol = Text("Solitário", color=BLUE_C, font_size=20)
        sol.next_to(ax, LEFT)

        soc = Text("Sociável", color=BLUE_C, font_size=20)
        soc.next_to(ax, RIGHT)

        di = Text("Diúrno", color=RED_C, font_size=20)
        di.next_to(ax, UP)

        noc = Text("Notúrno", color=RED_C, font_size=20)
        noc.next_to(ax, DOWN)

        self.play(Write(sol))
        self.play(Write(soc))
        self.play(Write(di))
        self.play(Write(noc))

        self.wait()
        chartGroup = VGroup(ax, sol, soc, di, noc)
        chartGroup.generate_target()
        chartGroup.target.shift(RIGHT * 3)
        chartGroup.target.scale(0.8)

        self.play(MoveToTarget(chartGroup))
        self.wait()

        samples = Text("Amostras", font_size=25).shift(LEFT * 4).shift(UP*3)

        sampleAnimals = [
            ["Lobo", 4, 2],        # Social, mostly diurnal
            ["Leopardo", -4, -3],  # Solitary, mostly nocturnal
            ["Elefante", 5, 4],    # Highly social, diurnal
            ["Coruja", -2, -5],    # Solitary, nocturnal
            ["Chimpanzé", 5, 3],   # Highly social, diurnal
            ["Tigre", -5, -2],     # Solitary, crepuscular/nocturnal
            ["Golfinho", 5, 5],    # Highly social, diurnal
            ["Urso", -1, 1],       # Mostly solitary, variable activity
            ["Suricato", 5, 5],    # Highly social, diurnal
            ["Gato", 2, -1], # Somewhat social, crepuscular
        ]

        exTable = MobjectTable(
            col_labels=[Text("Animal", weight=BOLD), Text("X", weight=BOLD, color=BLUE_C), Text("Y", weight=BOLD, color=RED_C)],
            table=[
                [Text(animal[0]), Text(str(animal[1]), color=BLUE_C), Text(str(animal[2]), color=RED_C)] for animal in sampleAnimals
            ],
        ).scale(0.4)

        exTable.next_to(samples, DOWN)
        self.play(DrawBorderThenFill(exTable))
        self.wait()
        exGroup = VGroup(samples, exTable)

        highlights: list[tuple[str, Mobject, Mobject]] = []

        for [name, x, y] in sampleAnimals:
            dot = Dot(ax.coords_to_point(x, y), color=GREEN_C)
            lines = ax.get_lines_to_point(ax.c2p(x, y))
            self.play(Write(dot), run_time=0.2)
            chartGroup.add(dot)

            if name in ["Lobo", "Leopardo"]:
                highlights.append([name, dot, lines])

        self.wait()

        for [name, dot, lines] in highlights:
            dot.generate_target()
            dot.target.set_color(YELLOW)
            text = Text(name, color=YELLOW, font_size=20, should_center=False)
            chartGroup.add(text, lines)
            if(name == "Lobo"):
                text.next_to(dot, UP * 0.5)
            elif(name == "Leopardo"):
                text.next_to(dot, DOWN * 0.5)
            self.play(Write(text), Create(lines), MoveToTarget(dot))
            self.wait()

        oldView = VGroup(exGroup, chartGroup)
        X = Text("X", color=BLUE_C)
        Y = Text("Y", color=RED_C)

        newView = VGroup(X, Y).arrange(RIGHT, buff=0.3)

        self.play(ReplacementTransform(oldView, newView))
        self.wait()

        letters = [
            ["Z", YELLOW],
            ["M", BLUE],
            ["N", RED],
            ["P", GREEN],
            ["A", TEAL],
            ["B", PINK],
            ["C", GOLD],
            ["...=1536", RED]
        ]

        for letter, color in letters:
            new_letter = Text(letter, color=color)
            newView.add(new_letter)
            self.play(Write(new_letter), newView.animate.arrange(RIGHT, buff=0.3))
            self.wait(0.2)
