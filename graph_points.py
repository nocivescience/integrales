from manim import *
class GraphPointScene(Scene):
    def construct(self):
        axes=self.axes=self.getting_axes()
        dots=self.getting_dots(axes=axes)
        function=self.getting_function(axes)
        self.play(Create(axes))
        self.play(LaggedStartMap(Create,dots))
        self.play(Create(function))
        self.wait()
        function_up=function.copy()
        function_down=function.copy()
        function_up.set_color(YELLOW).shift(UP)
        function_down.set_color(RED).shift(DOWN)
        self.play(TransformFromCopy(
            function,function_up
        ),TransformFromCopy(function,function_down))
        self.wait()
    def getting_axes(self):
        axes=Axes(
            x_range=[-5,5],
            y_range=[-4,4],
            axis_config={
                'include_numbers':False
            }
        )
        return axes
    def getting_dots(self,axes):
        dots=VGroup()
        for i in np.arange(-4,4,.27):
            for j in np.arange(-3,3,.27):
                dot=Dot().move_to(
                    axes.c2p(i,j)
                ).set_color(BLUE).set_opacity(.3)
                dots+=dot
        return dots
    def getting_function(self,axes):
        function=axes.plot(lambda t: 2*np.cos(4*t))
        return function