from manim import *
import itertools as it
class PointCircleScene(Scene):
    CONFIG={
        'functs':[
            lambda x: 2*x,
            lambda x: x**2,
            lambda x: np.cos(x*TAU),
            lambda x: np.sin(x),
            lambda x: np.exp(x),
        ]
    }
    def construct(self):
        axes=Axes(
            x_range=[-4,4,2],
            y_range=[-3,3,2]
        )
        colors=it.cycle([RED,BLUE,GREEN,YELLOW])
        points=[]
        for x,y in zip(np.random.randint(-4,5,40),np.random.randint(-3,3,40)):
            point=axes.c2p(x,y)
            points.append(point)
        dots=VGroup(*[
            Dot(color=next(colors)).move_to(point) for point in points
        ])
        self.play(
            LaggedStartMap(Create,VGroup(
                axes,
                dots
            )), run_time=5
        )
        self.wait(2)
        self.play(LaggedStartMap(
            Flash,dots
        ))
        circle=Circle(radius=2.5)
        self.wait(2)
        self.play(ReplacementTransform(dots,circle))
        self.wait(2)
        self.play(FadeOut(circle))
        self.wait(2)
        functions=VGroup()
        for func in self.CONFIG['functs']:
            graphing=axes.plot(func)
            functions.add(graphing)
        self.play(Create(functions[0]))
        for plot in functions[1:]:
            self.play(Transform(functions[0],plot))
        self.wait(2)