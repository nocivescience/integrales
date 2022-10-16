from manim import *
import itertools as it
class MultiplePolygonScene(Scene):
    def construct(self):
        circle=Circle(radius=2).set_z_index(-1)
        poligonos=VGroup()
        angles=[180*(t-2)/(2*t) for t in range(3,20)]
        POLIGONOS=VGroup()
        for t, angle in zip(range(3,20),angles):
            poligono=RegularPolygon(n=t,radius=2)
            POLIGONO=RegularPolygon(n=t,radius=2/np.sin(angle*DEGREES))
            poligonos+=poligono
            POLIGONOS+=POLIGONO
        for mob in [poligonos[0],POLIGONOS[0],circle]:
            self.play(Create(mob))
        self.wait()
        for mob, MOB in zip(poligonos[1:],POLIGONOS[1:]):
            self.play(Transform(poligonos[0],mob),Transform(POLIGONOS[0],MOB))
        self.wait()