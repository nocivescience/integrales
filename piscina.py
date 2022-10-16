from pathlib import Path
from manim import *
class PoolScene(Scene):
    def construct(self):
        pool=VMobject()
        pool.set_points_as_corners([
            ORIGIN,
            4*DOWN,
            2*RIGHT+4*DOWN,
            4*UP+4*DOWN+2*RIGHT
        ])
        self.play(Create(pool))
        self.wait()
        water=Rectangle(width=2,height=1).next_to(
            pool.get_center()
        )
        self.play(Create(water))
        self.wait()