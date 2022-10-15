from manim import *
class BackgroundScene(Scene):
    CONFIG={
        't_offset':0,
        'rate':2,
    }
    @staticmethod
    def curve(dx):
        return lambda x: np.cos(x+dx)
    def construct(self):
        axes=self.axes=Axes()
        curve=self.getting_curve(0)
        rectangles=self.getting_riemann(curve)
        curve.add_updater(lambda t,dt:self.update_curve(t,dt))
        rectangles.add_updater(lambda t,dt: self.getting_update_riemann(t,dt))
        for mob in [
            axes,
            curve,
            rectangles
        ]:
            self.play(Create(mob))
        self.wait(20)
    def getting_curve(self,t):
        curve=self.axes.plot(self.curve(t)).set_color(RED)
        return curve
    def update_curve(self,curve,dt):
        rate=self.CONFIG['rate']*dt
        curve.become(self.getting_curve(rate+self.CONFIG['t_offset']))
        self.CONFIG['t_offset']-=rate
        return curve
    def getting_riemann(self,curve):
        rectangles=self.axes.get_riemann_rectangles(curve,x_range=[-3,3],input_sample_type='center')
        return rectangles
    def getting_update_riemann(self,rects,dt):
        rate=self.CONFIG['rate']*dt
        rects.become(self.getting_riemann(self.getting_curve(rate+self.CONFIG['t_offset'])))
        self.CONFIG['t_offset']-=rate
        return rects