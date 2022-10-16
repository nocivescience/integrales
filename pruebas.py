from manim import *
# pre_images=VGroup(*[MathTex('PreImagen_{%i}' %a) for a in range(1,10)])
# images=VGroup(*[MathTex('Imagen_{%i}' %a) for a in range(1,13)])
# rands=[]
# for _ in range(len(pre_images)):
#     rand=int(np.random.uniform(0,len(pre_images))
#     )
#     # arrow=Arrow(pre_images[rand],images[-1])
#     # arrows.add(arrow)
#     rands.append(rand)
# print(rands)
# number_line=Axes()
# points=number_line.c2p(
#     [i,np.random.random()*3] for i in range(-3,3)
# )
# print(points)
angles=[180*(t-2)/(2*t) for t in range(3,20)]
print(angles)
print(angles[0]*DEGREES)