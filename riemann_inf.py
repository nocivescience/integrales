from manim import *
class RiemmanListScene(Scene):
    def construct(self):
        axes=Axes()
        function=axes.plot(lambda t: np.cos(t)-np.cos(1.6*t))
        for mob in [axes,function]:
            self.play(Create(mob))
        self.wait()
        rectangles=axes.get_riemann_rectangles(function,dx=2,input_sample_type='center')
        self.play(Create(rectangles))
        for t in reversed(np.linspace(0.01,1.9,30)):
            rectangles_list=axes.get_riemann_rectangles(function,input_sample_type='center',dx=t)
            self.play(Transform(rectangles,rectangles_list))
        self.wait()