from manim import *
import itertools as it
class MultiplePolygonScene(Scene):
    def construct(self):
        circle=Circle(radius=1)
        regular_3=RegularPolygon(n=3,radius=2)
        regular_4=RegularPolygon(n=4,radius=1.44)
        regular_5=RegularPolygon(n=5,radius=1.21)
        regular_6=RegularPolygon(n=6,radius=1.18)
        regular_7=RegularPolygon(n=7,radius=1.14)
        regular_8=RegularPolygon(n=8,radius=1.11)
        regular_9=RegularPolygon(n=9,radius=1.10)
        regular_10=RegularPolygon(n=10,radius=1.08)
        regular_11=RegularPolygon(n=11,radius=1.07)
        regular_12=RegularPolygon(n=12,radius=1.06)
        inner_3=RegularPolygon(n=3,radius=1)
        inner_4=RegularPolygon(n=4,radius=.95)
        inner_5=RegularPolygon(n=5,radius=.95)
        inner_6=RegularPolygon(n=6,radius=.95)
        inner_7=RegularPolygon(n=7,radius=.94)
        inner_8=RegularPolygon(n=8,radius=.93)
        inner_9=RegularPolygon(n=9,radius=.93)
        inner_10=RegularPolygon(n=10,radius=.93)
        inner_11=RegularPolygon(n=11,radius=.93)
        inner_12=RegularPolygon(n=12,radius=.93)
        for mob in [
            circle,
            regular_3,
            inner_3,
        ]:
            self.play(Create(mob))
        for mob, inner in zip([
            regular_3,
            regular_4,
            regular_5,
            regular_6,
            regular_7,
            regular_8,
            regular_9,
            regular_10,
            regular_11,
            regular_12,
        ],[
            inner_3,
            inner_4,
            inner_5,
            inner_6,
            inner_7,
            inner_8,
            inner_9,
            inner_10,
            inner_11,
            inner_12   
        ]):
            self.play(Transform(regular_3,mob),
                      Transform(inner_3,inner))
        self.wait()