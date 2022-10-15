from telnetlib import RCP
from manim import *
class FirstExample(Scene):
    def construct(self):
        axes=Axes(
            x_range=[0,10,2],
            y_range=[0,10,2],
        )
        grafico=axes.plot(lambda x:x+np.cos(x), x_range=[0,10], use_smoothing=False)
        rectangles=axes.get_riemann_rectangles(grafico,dx=1,input_sample_type="right")
        rectangles.set_z_index(-2)
        rectangles_2=axes.get_riemann_rectangles(grafico,dx=1,input_sample_type="left")
        rectangles_2.set_z_index(-2)
        x_label=axes.get_x_axis_label('x',direction=RIGHT)
        y_label=axes.get_y_axis_label('y',direction=UP)
        axes.add(x_label,y_label)
        self.play(Create(axes),Create(grafico))
        self.play(FadeIn(rectangles))
        self.wait()
        self.play(
            TransformFromCopy(rectangles,rectangles_2),run_time=3)
        self.wait()
        self.play(rectangles_2.animate.set_color(BLACK),run_time=4)
        self.wait(4)