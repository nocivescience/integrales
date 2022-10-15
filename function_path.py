from tkinter import W
from manim import *
class PathScene(Scene):
    def construct(self):
        number_line=Axes(
            x_range=[-6,6,2],
            y_range=[0,4],
            tips=False,
            x_axis_config={
                'include_numbers':True,
            },
        )
        number_line[-1].set_stroke(opacity=0)
        path=VMobject()
        lines=VGroup()
        points=np.array([
            [i,np.random.random()*3-2,0] for i in range(-6,6)
        ])
        path.set_points_smoothly(
            points
        )
        for point in points.copy():
            if (point[1]+2)/3>.5:
                line=Line(LEFT,RIGHT).set_color(RED)
                line.move_to(point+UP*.2)
            else:
                line=DashedLine(LEFT,RIGHT).set_color(BLUE)
                line.move_to(point+DOWN*.2)
            lines.add(line)
        for mob in [
            number_line,
            path
        ]:
            self.play(Create(mob))
        self.wait()
        self.play(LaggedStartMap(
            Create,lines
        ))
        self.wait()
        explanation=Tex(
            'Aproxiomación por exceso y defecto de una función'
        ).to_edge(UP,buff=.2)
        self.play(Write(explanation))
        self.wait()
        integrales=MathTex(
            r'\int_a^b s(x)dx\leq \int_a^b f(x)dx \leq \int_a^b t(x)dx'
        ).next_to(explanation,DOWN,buff=.4)
        self.play(TransformFromCopy(explanation,integrales))        
        self.wait(5)