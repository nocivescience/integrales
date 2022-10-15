from manim import *
class OddScene(Scene):
    def construct(self):
        axes=Axes(x_range=[.1,6])
        function=lambda x: np.log(x)
        function=axes.plot(function)
        line_0=axes.get_horizontal_line(axes.c2p(8,3)).set_color(YELLOW)
        line_1=axes.get_horizontal_line(axes.c2p(8,-3)).set_color(RED)
        texto_0=MathTex(r'M_0')
        texto_1=MathTex(r'M_1')
        texto_0.next_to(axes.c2p(0,3),LEFT,buff=0.12)
        texto_1.next_to(axes.c2p(0,-3),LEFT,buff=0.12)
        for mob in [
            axes,
            function,
            line_0,
            line_1,
            texto_0,
            texto_1
        ]:
            self.play(Create(mob))
        self.wait()
        function=MathTex(
            r'M_1\leq f(x) \leq M_0'
        ).to_edge(UP,buff=0.3)
        self.play(
            TransformFromCopy(VGroup(texto_0,texto_1),function)
        )
        self.wait(2)