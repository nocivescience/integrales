from manim import *
class InfimoScene(Scene):
    def construct(self):
        axes=Axes(
            x_range=[-1,1],
            y_range=[-3,3],
            x_length=2,
            y_length=4,
            
        ).to_corner(UL)
        self.play(Create(axes))
        self.wait()
        function=axes.plot(
            lambda x: np.cos(3*x)
        )
        function_up=function.copy()
        function_down=function.copy()
        function_up.shift(UP)
        function_down.shift(DOWN)
        function_up.set_color(YELLOW)
        function_down.set_color(RED)
        dot_up=Dot(color=YELLOW).move_to(axes.c2p(0,2))
        dot_down=Dot(color=RED).move_to(axes.c2p(0,0))
        self.play(Create(function))
        self.play(TransformFromCopy(function,VGroup(function_up,function_down)))
        self.wait()
        self.play(Create(dot_up),Create(dot_down))
        self.wait()
        integral=Tex('¿Cómo saber si una función se puede integrar?')
        integral.to_edge(UP,buff=0.5)
        integral_2=Tex('Pues no todas las relaciones son integrables')
        integral_2.next_to(integral,DOWN,buff=1)
        self.play(Write(integral))
        self.wait()
        self.play(TransformFromCopy(integral,integral_2))
        self.wait()
        ecuacion=MathTex(r's(x)\leq f(x) \leq t(x)')
        ecuacion.to_edge(UP)
        self.play(Transform(
            VGroup(integral,integral_2),ecuacion
        ))
        self.wait()
        ecuacion_2=VGroup(
            MathTex(r'\int_a^b s(x)dx'),
            MathTex(r'\leq'),
            MathTex(r'\int_a^b f(x)dx'),
            MathTex(r'\leq'),
            MathTex(r'\int_a^b t(x)dx')
        ).arrange(RIGHT)
        ecuacion_2.next_to(ecuacion,DOWN,buff=.5)
        self.play(FadeIn(ecuacion_2[1]),FadeIn(ecuacion_2[3]))
        self.wait()
        self.play(TransformFromCopy(function_down,ecuacion_2[0]))
        self.play(TransformFromCopy(function,ecuacion_2[2]))
        self.play(TransformFromCopy(function_up,ecuacion_2[4]))
        self.wait()
        ecuacion_3=VGroup(
            MathTex(r'\{\int_a^b s(x)dx |s \leq f  \},~~'),
            MathTex(r'\{\int_a^b t(x)dx |f \leq t  \}')            
        ).arrange(RIGHT).next_to(ecuacion_2,DOWN,buff=.5)
        self.play(TransformFromCopy(ecuacion_2,ecuacion_3))
        self.wait()
        ecuacion_4=MathTex(
            r'\int_a^b s(x)dx\leq sup S \leq inf T \leq \int_a^b t(x)dx'
        ).next_to(ecuacion_3,DOWN,buff=.5)
        self.play(TransformFromCopy(ecuacion_3,ecuacion_4))
        self.wait()
        ecuacion_5=MathTex(
            r'\int_a^b f(x)=sup S=inf T'
        ).next_to(ecuacion_4,DOWN,buff=0.5)
        ecuacion_6=VGroup(
            MathTex(r'\underbar{I}='),
            MathTex(r'sup\{ \int_a^b s(x)dx | s\leq f\},~~'),
            MathTex(r'\bar{I}='),
            MathTex(r'inf\{ \int_a^b t(x)dx | f\leq t\}'),
        ).arrange(RIGHT).next_to(ecuacion_5,DOWN,buff=0.5)
        self.play(Create(ecuacion_6))
        self.wait()