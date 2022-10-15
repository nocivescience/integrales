from manim import *
class IntervalosScene(Scene):
    def construct(self):
        number_line=NumberLine(
            x_range=[-6,6,2],
            include_numbers=True
        ).move_to(2*DOWN)
        dot_1=Dot().set_color(YELLOW).move_to(number_line.n2p(-6))
        dot_2=Dot().set_color(RED).move_to(number_line.n2p(6))
        dot_1.set_z_index(2)
        dot_2.set_z_index(2)
        brace_wetween_points=BraceBetweenPoints(dot_1.get_center(),dot_2.get_center(),direction=UP)
        label_brace=Text('intervalos finitos')\
            .next_to(brace_wetween_points,UP,buff=.3)
        for mob in [
          number_line,
          dot_1,
          dot_2,  
          brace_wetween_points,
          label_brace,
        ]:
            self.play(DrawBorderThenFill(mob))
        self.wait(2)
        for mob in [
          brace_wetween_points,
          label_brace,
        ]:
            self.play(FadeOut(mob))
        dots=VGroup()
        for t in np.linspace(-6,6,30):
            dot=Dot().move_to(number_line.n2p(t))
            dots.add(dot)
        self.play(
            LaggedStartMap(Create,dots)
        )
        indices=VGroup()
        rectangulos=VGroup()
        for i in range(len(dots)):
            indice=MathTex('x_{%i}' %i).scale(.5)
            indice.next_to(dots[i].get_center(),UP,buff=.3)
            indices.add(indice)
            rectangulo=Rectangle(
                width=70/12/config['frame_width'],
                height=np.random.random()*2
            )
            rectangulos.add(rectangulo)
        for i,rectangulo in zip(np.linspace(-6,6,30),rectangulos):
            rectangulo.move_to(
                number_line.n2p(i),
                rectangulo.get_corner(DL)
            )
        self.play(
            LaggedStartMap(Write,indices)
        )
        self.wait(3)
        self.play(
            LaggedStartMap(Unwrite,indices)
        )
        self.wait()
        self.play(
            LaggedStartMap(Create,rectangulos)
        )
        self.wait()
        ecuacion_1=MathTex(
            r'\{ (x,y)|0\leq x \leq h \wedge 0\leq y \leq  k \}'
        )
        ecuacion_1.to_edge(UP,buff=0.5)
        self.play(Write(ecuacion_1))
        self.wait()
        rectangulo_0=rectangulos[0].copy()
        self.add(rectangulo_0)
        self.play(rectangulo_0.animate.move_to(
            np.array([-5,2.3,0])).scale(2)
        )
        self.wait()
        self.play(Wiggle(rectangulo_0))
        brace_rectangulo_0=always_redraw(
            lambda: Brace(rectangulo_0,direction=RIGHT)
        )
        brace_rectangulo_0_below=always_redraw(
            lambda: Brace(rectangulo_0,direction=DOWN)
        )
        self.play(Create(brace_rectangulo_0),Create(brace_rectangulo_0_below))
        texto_brazo=Tex('x').add_updater(
            lambda t: t.next_to(
                brace_rectangulo_0_below,direction=DOWN,buff=.1
          )
        )
        texto_brazo_bottom=Tex('y').add_updater(
            lambda t: t.next_to(
                brace_rectangulo_0,direction=RIGHT,buff=.1
            )
        )
        self.play(LaggedStartMap(Write,VGroup(texto_brazo,texto_brazo_bottom)))
        self.wait()
        t=np.random.random()*3
        for t in np.random.random(size=5):
            self.play(
                rectangulo_0.animate.stretch_to_fit_height(t),
                about_point=rectangulo_0.get_bottom()
            )
        self.wait()
        