from random import random
from manim import *
import itertools as it
class ImageScene(Scene):
    def construct(self):
        pre_imagenes=VGroup(*[MathTex('PreImagen_{%i}' %a) for a in range(1,10)])
        pre_imagenes.arrange(DOWN,buff=.3)
        pre_imagenes.set(height=config['frame_height']-3)
        rectangle=Rectangle(color=BLUE_B,
            height=pre_imagenes.get_height()+.5,
            width=pre_imagenes.get_width()+.5
        )
        black_rectangle=Rectangle(
            height=rectangle.get_height(),
            width=.3
        ).next_to(rectangle,RIGHT,buff=0)
        black_rectangle.set_stroke(color=BLACK,width=.2).set_fill(color=BLACK,opacity=1)
        pre_imagenes.add(black_rectangle)
        pre_imagenes.add(rectangle)
        imagenes=VGroup(*[MathTex('Imagen_{%i}' %a) for a in range(1,13)])
        imagenes.arrange(DOWN,buff=.3)
        imagenes.set(height=config['frame_height']-3)
        rectangle2=Rectangle(color=BLUE_B,
            height=imagenes.get_height()+.5,
            width=imagenes.get_width()+.5
        )
        imagenes.add(rectangle2)
        VGroup(pre_imagenes,imagenes).arrange(RIGHT,buff=4)
        self.play(LaggedStartMap(Create,pre_imagenes))
        self.play(LaggedStartMap(Create,imagenes))
        pre_imagenes_copy=pre_imagenes.copy()
        imagenes_copy=imagenes.copy()
        arrows_1=self.getting_arrows(pre_imagenes_copy,imagenes_copy)
        self.play(Create(arrows_1))
        self.wait()
        score=30
        while score:
            pre_imagenes_copy_2=pre_imagenes.copy()
            imagenes_copy_2=imagenes.copy()
            arrows=self.getting_arrows(pre_imagenes_copy_2, imagenes_copy_2)
            self.play(Transform(arrows_1,arrows))
            score-=1
        self.wait()
    def getting_arrows(self,pre_images,images):
        arrows=VGroup()
        while pre_images:
            rand_pre=int(np.random.uniform(0,len(pre_images)))
            rand_images=int(
                np.random.uniform(0,len(images))
            )
            arrow=Arrow(pre_images[rand_pre],images[rand_images])
            arrows.add(arrow)
            pre_images.remove(pre_images[rand_pre])
        return arrows