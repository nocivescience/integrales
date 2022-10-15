from manim import *
class ExhausionScene(Scene):
    def construct(self):
        circle=Circle(radius=2).set_z_index(6)
        poligono_1=RegularPolygon(n=6,radius=2).set_z_index(5)
        poligono_2=RegularPolygon(n=6,radius=2.32)
        for pol in [poligono_1, poligono_2]:
            pol.set_stroke(width=2,color=BLACK)
            pol.set_fill(color=YELLOW,opacity=1)
        for mob in [
            circle,
            poligono_1,
            poligono_2
        ]:
            self.play(FadeIn(mob))
        self.play(poligono_1.animate.set_color(BLACK))
        self.wait()