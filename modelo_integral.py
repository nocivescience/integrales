from manimlib.imports import *
class MyGraph(GraphScene):
        CONFIG={
                "graph_origin":ORIGIN,
                "x_max":FRAME_X_RADIUS,
                "x_min":-FRAME_X_RADIUS,
                "y_max":FRAME_Y_RADIUS,
                "y_min":-FRAME_Y_RADIUS,
                "x_axis_label":None,
                "y_axis_label":None,
                "dot_style":{
                        "radius":.06,
                        "color":BLUE,
                        "stroke_width":1,
                        "stroke_color":WHITE,
                }
        }
        @staticmethod
        def curve(x):
                return 2*np.cos(x)-2*np.cos(1.6*x)
        def construct(self):
                self.setup_axes(animate=True)
                texto=TextMobject("This is my fisrt experience on ManimPython").set_width(FRAME_WIDTH)
                texto.scale(0.7).to_edge(UP,buff=0.1)
                texto_function=TexMobject("2\\cdot\\cos(x)-2\\cdot\\cos(1.6\\cdot x)")
                texto_function.set_color_by_tex("\\cdot\\cos(",BLUE)
                texto_function.next_to(texto,DOWN,buff=0.2)
                texto.set_color(RED)
                graph=self.get_graph(self.curve)
                self.play(ShowCreation(graph),*list(map(Write,[texto,texto_function])))
                group_tex=VGroup(texto,texto_function)
                self.play(group_tex.set_color,YELLOW,group_tex.set_fill,opacity=0)
                self.get_my_dot(graph)
                self.wait()
        def get_my_dot(self,graph):
                dot=Dot(**self.dot_style)
                dot.move_to(graph.point_from_proportion(0))
                function=lambda x: np.cos(x) 
                self.play(PhaseFlow(function,dot),run_time=4)
              

################################################################
#
#def get_path_pending(path,proportion,dx=0.001):
#        if proportion < 1:
#                coord_i = path.point_from_proportion(proportion)
#                coord_f = path.point_from_proportion(proportion+dx)
#        else:
#                coord_i = path.point_from_proportion(proportion-dx)
#                coord_f = path.point_from_proportion(proportion)
#        line = Line(coord_i,coord_f)
#        angle = line.get_angle()
#        return angle
#
#class ShiftAndRotateAlongPath(Animation):
#        CONFIG = {
#                "run_time": 5,
#                "rate_func": smooth,
#                "dx":0.01
#        }
#        def __init__(self, mobject, path,**kwargs):
#                assert(isinstance(mobject, Mobject))
#                digest_config(self, kwargs)
#                self.mobject = mobject
#                self.path = path
#
#        def interpolate_mobject(self, alpha):
#                self.mobject.become(self.starting_mobject)
#                self.mobject.move_to(
#                self.path.point_from_proportion(alpha)
#                )
#                angle = get_path_pending(self.path,alpha,self.dx)
#                self.mobject.rotate(
#                        angle,
#                        about_point=self.mobject.get_center(),
#                )
#
#class MoveAlongPathWithRotation(Scene):
#        def construct(self):
#                path = Line(LEFT*5, RIGHT*5, stroke_opatity=0.5)
#                path.points[1] += UP * 4
#                path.points[2] += DOWN * 4
#                start_angle = get_path_pending(path, 0)
#
#                triangle = Triangle().set_height(0.5)
#                triangle.move_to(path.get_start())
#                triangle.rotate(- PI / 2)
#
#                self.add(triangle,path)
#                self.play(
#                        ShiftAndRotateAlongPath(triangle,path),
#                        run_time=4
#                )
#                self.wait()
#
###############################################################################

class MyGraphWithUpate(Scene):
        CONFIG={
                "graph_origin":ORIGIN,
                "x_max":FRAME_X_RADIUS,
                "x_min":-FRAME_X_RADIUS,
                "y_max":FRAME_Y_RADIUS,
                "y_min":-FRAME_Y_RADIUS,
                "x_axis_label":None,
                "y_axis_label":None,
                "dot_style":{
                        "radius":.06,
                        "color":BLUE,
                        "stroke_width":1,
                        "stroke_color":WHITE,
                },
                "path_style":{
                        "troke_width":1.4,
                        "stroke_color":GREEN,
                },
                "t_offset":0,
                "rate":0.05,
                "number":18
        }
        def construct(self):
                graph=self.curve(0)
                dots=self.get_dots(graph,self.number)
                graph.add_updater(self.update_graph)
                def update_dot(dots):
                        for dot,m in zip(dots,range(len(dots))):
                                dot.move_to(graph.point_from_proportion(m/len(dots)))
                dots.add_updater(update_dot)
                self.play(ShowCreation(graph))
                self.play(GrowFromCenter(dots))
                self.wait(5)
                graph.clear_updaters()
                self.wait()
                my_plane=NumberPlane()
        def curve(self,dx):
                my_func=FunctionGraph(lambda x: 2*dx*np.cos(x)-2*dx*np.cos(1.6*x))
                return my_func
        def get_dots(self,graph,number):
                dots=VGroup()
                for m in range(number):
                        point=graph.point_from_proportion(m/number)
                        dot=Dot(**self.dot_style).move_to(point)
                        dots.add(dot)
                return dots
        def update_graph(self,curve,dt):
                rate=self.rate*dt
                curve.become(self.curve(rate+self.t_offset))
                self.t_offset+=rate
                return curve

class MyThirdCutScene(Scene):
        CONFIG={

        }
        def construct(self):
                my_line=Line(4*LEFT,4*RIGHT)
                dot=Dot(color=RED)
                first_proportion=my_line.point_from_proportion(0)
                second_proportion=my_line.point_from_proportion(.5)
                interaction=interpolate(first_proportion,second_proportion,.5)
                dot.move_to(interaction)
                self.add(my_line,dot)
                self.wait()

class MyAnimation(Animation):
        def __init__(self,mobject,path,my_proportion,kwargs):
                digest_config(self,kwargs)

class MyFourthCutScene(Scene):
        @staticmethod
        def my_curve(x):
                return 2*np.cos(x)
        def construct(self):
                my_graph=FunctionGraph(self.my_curve)
                self.add(my_graph)
                self.wait()
        def my_update(self,graph,position):
                dot=Dot().move_to(graph.point_from_propotion(0))
                self.add(dot)
                def update_dot(dot,alpha):
                        pass

class RollAlongVector(Animation):
    CONFIG = {
        "rotation_vector" : OUT,
    }
    def __init__(self, mobject, vector, **kwargs):
        radius = mobject.get_width()/2
        radians = get_norm(vector)/radius
        last_alpha = 0
        digest_config(self, kwargs, locals())
        Animation.__init__(self, mobject, **kwargs)

    def interpolate_mobject(self, alpha):
        d_alpha = alpha - self.last_alpha
        self.last_alpha = alpha
        self.mobject.rotate_in_place(
            d_alpha*self.radians, 
            self.rotation_vector
        )
        self.mobject.shift(d_alpha*self.vector)

class PruebaVector(Scene):
        def construct(self):
                square=Square()
                vector=np.array([5,3,0])
                self.add(square)
                self.play(RollAlongVector(square,vector))

def my_own_graph(my_graph,proportion,dx=0.001):
        if proportion<1:
                i_coord=my_graph.point_from_proportion(proportion)
                j_coord=my_graph.point_from_proportion(proportion+dx)
        else:
                i_coord=my_graph.point_from_proportion(proportion-dx)
                j_coord=my_graph.point_from_proportion(proportion)
        line=Line(i_coord,j_coord)
        return line
class MyAnimation(Animation):
        def __init__(self,mobject,path,proportion,**kwargs):
                assert(isinstance(mobject,Mobject))
                digest_config(self,kwargs)
                self.mobject=Mobject
                self.path=path
                self.proportion=proportion
        def interpolate_mobject(self,path,proportion):
                pass

        
class MoveAlongPath1(Animation):
        CONFIG = {
                "suspend_mobject_updating": False,
        }

        def __init__(self, mobject, path,proportion, **kwargs):
                self.path = path
                self.proportion=proportion
                super().__init__(mobject, **kwargs)

        def interpolate_mobject(self, alpha):
                initial_point=self.mobject.point_from_proportion(0)
                pos_point=self.mobject.point_from_proportion(self.proportion)
                point = self.path.point_from_proportion(np.all(interpolate(initial_point,pos_point,alpha)))
                self.mobject.move_to(point)
class MakeAExperiment(Scene):
        def construct(self):
                my_function=lambda x: np.cos(x)
                my_graph=FunctionGraph(my_function)
                dot=Dot(color=RED)
                dot.move_to(my_graph.point_from_proportion(1))
                self.play(ShowCreation(my_graph),ShowCreation(dot))
                time=0
                while time<3:
                        my_time=np.random.random()
                        my_position=np.random.random()
                        time+=my_time
                        self.play(MoveAlongPath1(dot,my_graph,my_position),run_time=3)
                self.wait()

class MyDotsCurve(FunctionGraph):
        CONFIG={
                "t_offset":0,
                "rate":0.1,
        }
        def __init__(self,a,number,**kwargs):
                digest_config(self,kwargs)
                curve=super().__init__(
                        lambda x: a*np.cos(x)-a*np.cos(1.6*x)
                )
                self.number=number
                dots=self.get_dots()
                self.add(dots,curve)
                        
        def get_dots(self):
                dots=VGroup()
                for m in range(self.number):
                        dot=Dot().move_to(self.point_from_proportion(m/self.number))
                        dots.add(dot)
                return dots
class MyPrueba(Scene):
        def construct(self):
                my_project=MyDotsCurve(1.4,42,color=BLUE)
                self.play(ShowCreation(my_project),run_time=3)
                self.wait()

class MyDotsCurve2(FunctionGraph):
        CONFIG={
                "t_offset":0,
                "rate":0.1,
        }
        def __init__(self,number,dx,**kwargs):
                digest_config(self,kwargs)
                self.curve=super().__init__(
                        lambda x: dx*np.cos(x)-dx*np.cos(1.6*x)
                )
                self.number=number
                dots=self.get_dots()
                self.add(dots)
                self.add_updater(lambda mob,dt: mob.get_update(dt))
        def get_update(self,dt):
                rate=dt*self.rate
                self.become(self.curve(self.number,rate+self.t_offset))
                self.t_offset+=rate
                        
        def get_dots(self):
                dots=VGroup()
                for m in range(self.number):
                        dot=Dot().move_to(self.point_from_proportion(m/self.number))
                        dots.add(dot)
                return dots
class MyPrueba2(Scene):
        def construct(self):
                my_project=MyDotsCurve2(13,0,color=BLUE)
                self.play(ShowCreation(my_project))
                self.wait()

class medition(VGroup):
        CONFIG={
                "dashed":False
        }
        def __init__(self,object,**kwargs):
                pass

class MyDot(Dot):
        def __init__(self):
                Dot().__init__(self)
class Prueba2(Scene):
        def construct(self):
                my_dot=MyDot()
                self.play(ShowCreation(my_dot))
                self.wait()

class Meditions(VGroup):
        CONFIG={
                "dashed":False,
                "line_style":{
                        "stroke_width":1.4,
                        "color":RED,
                },
                "rotar":False
        }
        def __init__(self,objeto,**kwargs):
                VGroup.__init__(self,**kwargs)
                if self.dashed==True:
                        Medicion=DashedLine(UP,LEFT,**self.line_style)
                else:
                        Medicion=Line(UP,LEFT,**self.line_style)
                if self.rotar:
                        Medicion.rotate(PI/2)
                        Medicion.next_to(objeto,DOWN,buff=0.1)
                else:
                        Medicion.rotate(0)
                        Medicion.next_to(objeto,RIGHT)
                self.add(Medicion)
                
class MyRects(Scene):
        CONFIG={

        }
        def construct(self):
                my_rectangles=VGroup(*[
                        self.get_rectangles(4*np.random.random(),2) for _ in range(2)
                ])
                my_rectangles.arrange(RIGHT,buff=0.001)
                self.play(ShowCreation(my_rectangles))
                self.wait()
                self.play(my_rectangles.arrange,RIGHT,buff=6)
                lines=VGroup()
                for my_rectangle in my_rectangles:
                        line_horizontal=Line(ORIGIN,RIGHT).match_width(my_rectangle.get_width())
                        line_vertical=Line(ORIGIN,UP).match_height(my_rectangle.get_height())
                        lines.add(line_horizontal,vertical)
                medicion_vertical_1=Meditions(lines[0][0],rotar=False,dashed=True).set_width(my_rectangle)
                medicion_horizontal_1=Meditions(lines[0,1],rotar=True,dashed=True).set_height(my_rectangle)
                medicion_vertical_2=Meditions(lines[1][0],rotar=False,dashed=True).set_width(my_rectangle)
                medicion_horizontal_2=Meditions(lines[1][1],rotar=True,dashed=True).set_height(my_rectangle)
                self.play(ShowCreation(medicion_vertical),ShowCreation(medicion_horizontal))
                self.wait()
        def get_rectangles(self,alto,ancho):
                rectangle=Rectangle(width=ancho,height=alto)
                color=interpolate_color(RED,ORANGE,np.random.random())
                return rectangle

class MyFirstProject(Line):
        def __init__(self,a,b,**kwargs):
                Line.__init__(self,a*DOWN,b*UP,**kwargs)
                self.move_to(UP)
class MyAxis(Scene):
        def construct(self):
                my_axes=MyFirstProject(a=3,b=6,color=RED)
                self.play(ShowCreation(my_axes))
                self.wait()

class MySecondProj(Line):
        def __init__(self,**kwargs):
                digest_config(self,kwargs)
                
                Line.__init__(self,**kwargs)
                self.set_color(GREEN)
class MySecondProject(Scene):
        def construct(self):
                my_proj=MySecondProj()
                self.play(ShowCreation(my_proj))
                self.wait()

class MyGraph6(FunctionGraph):
        CONFIG={
                "dot_style":{
                        "radius":0.06,
                        "color":RED,
                        "stroke_width":1,
                        "stroke_color":WHITE
                }
        }
        def __init__(self,b,num,**kwargs):
                digest_config(self,kwargs)
                super().__init__(
                        lambda x: np.cos(2*x+b)+np.cos(2.6*x+b)
                )
                self.num=num
                self.add(self.get_dots())
        def get_dots(self):
                dots=VGroup()
                for n in range(self.num):
                        point=self.point_from_proportion(n/self.num)
                        dot=Dot(**self.dot_style).move_to(point)
                        dots.add(dot)
                return dots
class MyProj4(Scene):
        CONFIG={
                "t_offset":0,
                "rate":2
        }
        def construct(self):
                my_graph=MyGraph6(2,20)
                my_graph.add_updater(self.update)
                self.play(ShowCreation(my_graph))
                self.wait(15)
        def update(self,curve,dt):
                rate=self.rate*dt
                curve.become(MyGraph6(self.t_offset+rate,20))
                self.t_offset-=rate
                return curve
        
class MyCurve7(GraphScene):
        CONFIG={
                "rate":2,
                "t_offset":0,
                "x_min":-FRAME_X_RADIUS,
                "x_max":FRAME_X_RADIUS,
                "y_min":-FRAME_Y_RADIUS,
                "y_max":FRAME_Y_RADIUS,
                "graph_origin":ORIGIN,
                "x_axis_width":2*FRAME_X_RADIUS,
                "x_axis_height":2*FRAME_Y_RADIUS,
        }
        @staticmethod
        def curve(dx):
                return lambda x:np.cos(x+dx)-np.cos(1.6*x+dx)
        def construct(self):
                self.setup_axes(animate=True)
                my_curve=self.get_my_curve(0)
                my_rects=self.my_rectangles(my_curve)
                my_curve.add_updater(self.update_curve)
                my_rects.add_updater(self.rectangles_updates)
                self.play(ShowCreation(my_curve))
                self.play(FadeIn(my_rects))
                self.wait(10)
        def get_my_curve(self,dt):
                my_curve=self.get_graph(self.curve(dt))
                return my_curve
        def update_curve(self,curve,dt):
                rate=self.rate*dt
                curve.become(self.get_my_curve(rate+self.t_offset))
                self.t_offset-=rate
                return curve
        def my_rectangles(self,curve):
                my_rects=self.get_riemann_rectangles(curve,x_min=-FRAME_WIDTH,x_max=FRAME_WIDTH)
                return my_rects
        def rectangles_updates(self,rects,dt):
                rate=self.rate*dt
                rects.become(self.my_rectangles(self.get_my_curve(rate+self.t_offset)))
                self.t_offset-=rate
                return rects

class MyExplainAboutIntegrating(GraphScene):
        CONFIG={
                "x_min":-5,
                "x_max":5,
                "x_axis_width":10,
                "graph_origin":ORIGIN+2*DOWN,
                "y_max":1.2,
                "y_min":0,
                "y_axis_height":4,
                "t_offset":0,
                "rate":0.1,
                "style_path":{
                        "color":BLUE
                }
        }
        @staticmethod
        def curve(dx):
                return lambda x: 1/(1+dx)*np.exp(-.5/(1+dx)*x**2)
        def construct(self):
                self.setup_axes(animate=True)
                self.x_axis.remove(self.x_axis)
                self.get_my_graph()
        def get_my_graph(self):
                graph=self.get_graph(self.curve(0),**self.style_path)
                my_rects=self.get_riemann_rectangles(
                        graph=graph,
                        input_sample_type="center",
                        dx=0.5
                )
                self.play(ShowCreation(graph))
                braces=VGroup()
                for rect in my_rects.submobjects:
                        brace=Brace(rect,DOWN,buff=0.1)
                        texto=TexMobject("dx").next_to(brace,DOWN,buff=0.1)
                        texto.scale(0.4)
                        braces.add(brace,texto)
                self.play(ShowCreation(my_rects))
                self.play(LaggedStartMap(Write,braces),run_Time=4,lag_ratio=.6)
                graph.add_updater(self.my_update)
                my_rects.add_updater(self.my_rects_update)
                self.add(graph,my_rects)
                self.wait(8)
        def my_update(self,graph,dt):
                rate=self.rate*dt
                graph.become(self.get_graph(self.curve(self.t_offset+rate),**self.style_path))
                self.t_offset+=rate
                return graph
        def my_rects_update(self,rects,dt):
                rate=self.rate*dt
                rects.become(self.get_riemann_rectangles(self.get_graph(self.curve(self.t_offset+rate)),input_sample_type="center",dx=0.5))
                self.t_offset+=rate
                return rects

class MyWindmill(Scene):
        CONFIG={
                "dot_style":{
                        "radius":0.06,
                        "color":ORANGE,
                        "stroke_width":WHITE,
                        "strogle_color":BLUE
                },
                "line_style":{
                        "color":YELLOW,
                        "stroke_width":1
                },
                "length":3*FRAME_X_RADIUS,
                "leave_shadows":False,
                "rot_speed":0.25
        }
        def get_points(self,n_points=20):
                return np.array([
                        [
                                np.random.uniform(-FRAME_X_RADIUS,FRAME_X_RADIUS),
                                np.random.uniform(-FRAME_Y_RADIUS,FRAME_Y_RADIUS),
                                0
                        ]
                        for _ in range(n_points)
                ])
        def get_dots(self,points):
                return VGroup(*[
                        Dot(**self.dot_style).move_to(point) for point in points
                ])
        def get_my_windimill(self,points,pivot=None,angle=30*DEGREES):
                line=Line(**self.line_style)
                line.get_length(self.get_length)
                line.set_angle(angle)
                line.my_points=points
                line.rot_speed=self.rot_speed
                if pivot is not None:
                        line.pivot=pivot
                else:
                        line.pivot=points[0]
                line.add_updater(lambda t: t.move_to(t.pivot))
                return line
        def start_leaving_shadow(self):
                self.leave_shadows=True
                self.add(self.get_windimill_shadows())
        def get_windimill_shadows(self):
                if not hasattr(self,"windmill_shadows"):
                        self.windmill_shadows=VGroup()
                return self.windmill_shadows
        def next_pivot_and_angle(self,windmill):
                current_angle=windmill.get_angle()
                pivot=windmill.pivot
                non_pivots=list(filter(lambda t: not np.all(t-pivot),windmill.my_points))
                angles=np.array([
                        -(angle_of_vector(point-pivot)-curr_angle)%PI
                        for point in non_pivots
                ])
                tiny_indices=angles<1e-6
                if np.all(tiny_indices):
                        return non_pivots[0],PI
                angles[tiny_indices]=np.inf
                return non_pivots[index],angles[index]
        def rotate_to_next_pivot(self,windmill,max_time=None,added_anims=None):
                new_pivot,angle=self.next_pivot_and_angle(windmill)
                change_pivot_at_end=True
                if added_anims is None:
                        added_anims=[]
                run_time=angle/windmill.rot_speed
                if max_time is not None and run_time>max_time:
                        ratio=max_time/run_time
                        rate_func=lambda t: ratio*t
                        run_time=max_time
                        change_pivot_At_end=False
                else:
                        rate_func=linear
                for anim in added_anims:
                        if anim.run_time>run_time:
                                anim.run_time=run_time
                self.play(Rotate(windmill,-angle,rate_func=rate_func,run_time=run_time),added_anims)
                if change_pivot_at_end:
                        self.handle_pivot_change(windmill,new_pivot)
                return [self.get_hit_flash(new_pivot)],run_time
        def handle_pivot_chenge(self,windmill,new_pivot):
                windmill.pivot=new_pivot
                if self.leave_shadows:
                        new_shadow=windmill.copy()
                        new_shadow.fade(.5)
                        new_shadow.set_stroke(width=0)
                        new_shadow.clear_updaters()
                        shadows=self.get_windmill_shadows()
                        shadows.add(shadow)
        def let_windmill_run(self,windmill,time):
                anims_from_last_hit=[]
                while time>0:
                        anims_from_last_hit,last_run_time=self.rotate_to_next_pivot(windmill,max_time=time)
                        time-=last_run_time
        def add_dot_color_updater(self,dots,windmill,**kwargs):
                for dot in dots:
                        dot.add_updater(lambda t: self.update_color(d,windmill,**kwargs))
        def update_dot_color(self,dot,windmill,color1=BLUE_A,color2=RED_A):
                perp=rotate_vector(windmill.get_vector(),TAU/4)
                dot_product=np.dot(perp,dot.get_center()-windmill.pivot)
                if dot_product>0:
                        dot.set_color(color1)
                else:
                        dot.set_color(color2)
                dot.set_stroke(WHITE,width=2,background=True)
        def get_hit_flash(self,point):
                flash=Flash(point,line_length=0.1,flash_radius=0.2,run_time=0.5,remover=True)
                flash_mob=flash.mobject
                for submob in flash_mob:
                        submob.reverse_points()
                return Uncreate(flash.mobject,run_time=0.25,lag_ratio=0)
        def get_pivot_counters(self,windmill,counter_height=0.25,buff=0.2,color=WHITE):
                points=windmill.my_points
                counters=VGroup()
                for point in points:
                        counter=Integer(0)
                        counter.set_color(color)
                        counter.set_height(counter_height)
                        counter.next_to(point,UP,buff=buff)
                        counter.point=point
                        counter.windmill=windmill
                        counter.is_pivot=False
                        counter.add_updater(self.update_counter)
                        counters.add(counter)
                return counters
        def update_counter(self,counter):
                dist=get_norm(counter.point-counter.windmill.pivot)
                counter.will_be_pivot=dist<1e-6
                if (not counter.is_pivot) and counter.will_be_pivot:
                        counter.increment_value()
                counter.is_pivot=counter.will_be_pivot
        def get_orientation_arrows(self,windmill,n_tips=20):
                tips=VGroup(*[
                        ArrowTip(start_angle=0)
                        for x in range(n_tips)
                ])
                tips.stretch(0.75,1)
                tips.scale(0.5)
                tips.rotate(windmill.get_angle())
                tips.match_color(windmill)
                tips.set_stroke(BLACK,width=1,background=True)
                for tip, a in zip(tips,np.linspace(0,1,n_tips)):
                        tip.shift(
                                windmill.point_from_proportion(a)-tip.points[0]
                        )
                return tips
        def get_left_right_coloring(self,windmill,opacity=0.4):
                rects=VGroup(VMobject(),VMobject())
                retcs.const_opacity=opacity
                def update_regions(rects):
                        p0,p1=windmill.get_start_and_end()
                        v=p1-p0
                        vl=rotate_vector(v,90*DEGREES)
                        vr=rotate_vecot(v,-90*DEGREES)
                        p2=p1+vl
                        p3=p0+vl
                        p4=p1+vr
                        p5=p0+vr
                        rects[0].set_point_as_corner(p0,p1,p2,p3)
                        rects[1].set_point_as_corner(p0,p1,p4,p5)
                        rects.set_stroke(width=0)
                        rects[0].set_fill(BLUE,rects.const_opacity)
                        rects[1].set_fill(GRAY,rects.const_opacity)
                        return rects
                rects.add_updater(update_regions)
                return rects
class Introoduce(MyWindmill):
        CONFIG={

        }
        def construct(self):
                pass

class MyIntegral1(Scene):
        def construct(self):
                self.my_dots()
                my_dots=self.my_dots()
                my_text=self.get_text("hola")
                self.play(*list(map(ShowCreation,[my_dots,my_text])))
                my_dots[1].add_updater(self.my_update_dot_mov)
                self.add(my_dots[1])
                self.wait(2)
        def my_dots(self):
                my_center=Dot(color=RED,stroke_color=WHITE,stroke_width=1)
                dot_mov=Dot(color=BLUE,stroke_color=WHITE,stroke_width=1)
                dot_mov.center=op.add(
                        3*LEFT,UP
                )
                my_center.move_to(ORIGIN)
                return VGroup(my_center,dot_mov)  
        def my_update_dot_mov(self,dot,dt):
                dot.center+=dt*RIGHT
                dot.move_to(dot.center)
                return dot
        def get_text(self,texto):
                my_dot_center,my_dot_mov=self.my_dots()
                mi_texto=TextMobject(texto)
                mi_texto.scale(0.5)
                mi_texto.my_dot_center=my_dot_center
                mi_texto.my_dot_mov=my_dot_mov
                mi_texto.add_updater(lambda t: t.move_to(mi_texto.my_dot_mov))
                mi_texto.my_transform=False
                dist=get_norm(mi_texto.my_dot_center.get_center()-mi_texto.my_dot_mov.get_center())
                mi_texto.will_be_transform=dist<1e-4
                if (not mi_texto.my_transform) and mi_texto.will_be_transform:
                        self.play(Transform(my_dot_mov,mi_texto))
                mi_texto.my_transform=mi_texto.will_be_transform
                return mi_texto

class MySecondExampleWithFalse(Scene):
        CONFIG={

        }
        def construct(self):
                my_dots=self.get_dots()
                my_text=self.get_texto(my_dots)
                self.play(FadeIn(my_dots),Write(my_text))
                my_text.add_updater(self.dot_edge_update)
        def get_dots(self):
                dot_central=Dot(color=RED)
                dot_edge=Dot(color=BLUE)
                return VGroup(dot_central,dot_edge)
        def get_texto(self,dots):
                texto=TextMobject("Las integrales no son difíciles")
                dot_central,dot_edge=self.get_dots()
                dot_edge.center=op.add(5*LEFT,0)
                texto.dot_edge=dot_edge
                texto.move_to(dot_edge.get_center())
                texto.copy=texto.copy()
                texto.in_transform=False
                return texto
        def dot_edge_update(self,texto,dt):
                texto.become(texto.copy)
                dot_edge=texto.dot_edge
                dot_edge.center+=dt*.5
                texto.move_to(dot_edge.get_center())
                return texto

class MyThirdFalse(Scene):
        CONFIG={
                "t_offset":0,
        }
        def construct(self):
                texto=self.get_dots()[2]
                dot_edge,dot_center=self.get_dots()[:2]
                self.play(FadeIn(dot_edge),FadeIn(dot_center))
                dot_edge.add_updater(self.get_update_collition)
                self.add(dot_edge)
                self.wait(3)
                self.play(Transform(dot_edge,dot_edge.texto))
                self.wait()
        def get_my_tex(self,texto):
                texto=TextMobject(texto)
                texto.set_color(RED)
                texto.set_width(FRAME_WIDTH-0.5)
                texto.set_stroke(width=1,color=WHITE,background=True)
                return texto
        def get_dots(self):
                dot_edge=Dot(color=RED,stroke_width=1,stroke_color=WHITE)
                dot_center=self.dot_center=Dot(color=BLUE,stroke_width=1,stroke_color=WHITE)
                dot_edge.center=op.add(4*LEFT,0)
                texto=self.get_my_tex("Las integrales no son tus enemigas")
                dot_edge.texto=texto
                dot_center.move_to(ORIGIN)
                return VGroup(dot_edge,dot_center,texto)
        def get_update_collition(self,dot_ed,dt):
                texto=dot_ed.texto
                
                dot_ed.move_to(dot_ed.center)
                dot_ed.transform=False
                dist=get_norm(dot_ed.get_center()-self.dot_center.get_center())
                dot_ed.center+=dt*RIGHT*1.5
                dot_ed.will_be_transform=dist<1e-6
                if not(dot_ed.transform) and dot_ed.will_be_transform:
                        dot_ed.center=dt*RIGHT*1.5
                dot_ed.will_be_transform=dot_ed.transform
                return dot_ed

class WhatIsAIntegral(Scene):
        def construct(self):
                texto=TextMobject("A in tegral is just a area below of a every curve")
                self.play(Write(texto))
                self.wait()
                example=TexMobject("Example...")
                self.play(Transform(texto,example))
                self.wait()
class MakingACurve(GraphScene):
        CONFIG={
                "x_min":-4,
                "x_max":4,
                "y_min":-3,
                "y_max":3,
                "x_axis_width":8,
                "y_axis_height":6,
                "graph_origin":ORIGIN
        }
        @staticmethod
        def curve(x):
                return np.cos(x)+np.cos(1.6*x)
        def construct(self):
                self.setup_axes(animate=True)
                titulo=TextMobject("My First Integrate")
                titulo.to_corner(UL).scale(0.5)
                titulo.set_color(RED)
                self.play(Write(titulo))
                graph=self.get_my_graph()
                my_dots=self.get_my_dots(graph)
                my_dots.save_state()
                for anim in [graph,my_dots]:
                        self.play(ShowCreation(anim))
                self.play(MoveAlongPath(my_dots[0],graph),my_dots[1].move_to,np.array([4,0,0]),run_time=16,rate_func=smooth)
                self.wait()
                self.play(FadeOut(my_dots))
                second=TextMobject("How to make my fisrt integrate").to_corner(UL).scale(0.5)
                second.set_color(GREEN)
                self.play(Transform(titulo,second))
                self.wait()
                my_rects=self.get_riemann_rectangles(graph,dx=1)
                self.play(ShowCreation(my_rects),run_time=6)
                self.wait()
                for my_rect in my_rects.submobjects:
                        self.play(WiggleOutThenIn(my_rect))
                self.wait()
                my_rects_center=self.get_riemann_rectangles(graph,dx=1,input_sample_type="center")
                self.play(Transform(my_rects,my_rects_center))
                self.wait()
                for anim in [self.x_axis,self.y_axis]:
                        self.play(FadeOut(anim))
                self.play(FadeOut(graph))
                self.wait()
                for anim in my_rects.submobjects:
                        if anim is my_rects.submobjects[3]:
                                continue
                        self.play(FadeOut(anim))
                self.wait()
                self.my_special_rect(my_rects.submobjects[3],second=second)
                self.wait()
        def my_special_rect(self,my_rect,second):
                self.play(my_rect.shift,ORIGIN+3*RIGHT,my_rect.scale,2)
                my_brace=always_redraw(lambda: Brace(my_rect,DOWN))
                my_tex_brace=TexMobject("\\Delta x").add_updater(lambda t: t.next_to(my_brace,DOWN,buff=0.1))
                my_tex_brace_dx=TexMobject("d x").add_updater(lambda t: t.next_to(my_brace,DOWN,buff=0.1))
                self.play(Write(my_tex_brace),FadeIn(my_brace))
                my_formula=TexMobject("\\sum_i^{n \\in Z} fx\\cdot", "\\Delta x")
                my_formula.next_to(second,DOWN,buff=0.5,aligned_edge=second.get_bottom())
                self.play(TransformFromCopy(my_tex_brace,my_formula))
                my_formula_dx=TexMobject("\\int_R fx\\cdot dx").next_to(my_formula,DOWN,buff=0.3,aligned_edge=second.get_bottom())
                for t in np.linspace(1,0.1,5):
                        if t==.1:
                                self.play(Transform(my_tex_brace,my_tex_brace_dx),Transform(my_formula,my_formula_dx))
                        self.play(my_rect.set_width,t,{"stretch":True})
                self.wait()
        def get_my_graph(self):
                graph=self.get_graph(self.curve,color=YELLOW_B)
                return graph
        def get_my_dots(self,graph):
                dot_graph=Dot(self.coords_to_point(-4,self.curve(-4)))
                dot_base=Dot(self.coords_to_point(-4,0))
                line_v=Line()
                line_v.put_start_and_end_on(dot_graph.get_center(),dot_base.get_center())
                def update_line(line_v):
                        line_v.put_start_and_end_on(dot_graph.get_center(),dot_base.get_center())
                line_v.add_updater(update_line)
                return VGroup(dot_graph,dot_base,line_v)
class MyRectToIntegrate(Scene):
        def construct(self):
                my_rects=VGroup(*[
                        Rectangle(width=1,height=4)
                        for _ in range(10)
                ])
                my_rects.set_stroke(width=1)
                my_rects.set_fill(color=BLUE_B,opacity=1)
                my_rects.set_color_by_gradient(RED,YELLOW_A)
                my_rects.arrange(RIGHT,buff=0,aligned_edge=my_rects[0].get_bottom())
                self.play(ShowCreation(my_rects),lag_ratio=.5)
                for t in [2,3,5,3,4]:
                        self.play(my_rects.set_height,t,{"stretch":True},aligned_edge=my_rects[0],lag_ratio=.5)
                self.wait()
                my_rects.save_state()
                self.play(my_rects.arrange,RIGHT,buff=0.8,lag_ratio=.5)
                self.wait()                
                self.play(Restore(my_rects),lag_ratio=.5)
                self.play(my_rects.arrange,RIGHT,buff=0.001,lag_ratio=.5)
                self.wait()
        
class MicroRectangle(ZoomedScene):
        CONFIG={
                "anim_kwargs":{
                        "run_time":1,
                        "rate_Func":linear
                },
        }
        def setup(self):
                ZoomedScene.setup(self)
        def construct(self):
                self.get_my_rect()
        def get_my_rect(self):
                my_rects=Rectangle(width=3,height=4,fill_color=RED,fill_opacity=.8)
                my_rects.set_color_by_gradient(RED,YELLOW)
                my_rects.set_stroke(width=1,color=RED)
                my_rects.save_state()
                my_camera=self.zoomed_camera.frame
                my_camera.move_to(my_rects.get_bottom())
                my_brace_h=always_redraw(lambda: Brace(my_rects,DOWN))
                my_brace_v=always_redraw(lambda: Brace(my_rects,RIGHT))
                my_text_1=TexMobject("\\Delta x").add_updater(lambda t: t.next_to(my_brace_h,DOWN,buff=0.1))
                my_text_2=TexMobject("f(x)").add_updater(lambda t: t.next_to(my_brace_v,RIGHT,buff=0.1))
                self.play(ShowCreation(my_rects),**self.anim_kwargs)
                for brace in [my_brace_h,my_brace_v]:
                        self.play(FadeIn(brace),**self.anim_kwargs)
                for texto in [my_text_1,my_text_2]:
                        self.play(Write(texto),**self.anim_kwargs)
                self.wait()
                for t in range(1,12):
                        if t%2==0:
                                self.play(my_rects.set_width,np.random.uniform(1,4),{"stretch":True},**self.anim_kwargs)
                        elif t%2==1:
                                self.play(my_rects.set_height,np.random.uniform(2,6),{"stretch":True},**self.anim_kwargs)
                self.play(Restore(my_rects),**self.anim_kwargs)
                self.wait()
                self.play(FadeOut(my_text_1),FadeOut(my_text_2),**self.anim_kwargs)
                self.wait()
                num_h=DecimalNumber(my_rects.get_width()).add_updater(lambda t:t.set_value(my_rects.get_width()))
                num_v=DecimalNumber(my_rects.get_height()).add_updater(lambda m:m.set_value(my_rects.get_height()))
                num_h.add_updater(lambda t:t.next_to(my_brace_h,DOWN,buff=0.1))
                num_v.add_updater(lambda t:t.next_to(my_brace_v,RIGHT,buff=0.1))
                my_rects.save_state()
                for anim in [num_h,num_v]:
                        self.play(Write(anim),**self.anim_kwargs)
                for t in range(1,12):
                        if t%2==0:
                                self.play(my_rects.set_width,np.random.uniform(1,4),{"stretch":True},
                                num_h.set_value,my_rects.get_width(),**self.anim_kwargs)
                        elif t%2==1:
                                self.play(my_rects.set_height,np.random.uniform(2,6),{"stretch":True},
                                num_v.set_value,my_rects.get_height(),**self.anim_kwargs)
                self.wait()
                self.play(Restore(my_rects),**self.anim_kwargs)
                self.play(FadeOut(my_brace_v),FadeOut(num_v),**self.anim_kwargs)
                for t in [3,2,1,.5,.4,.3,.2,.1,.09,.08,.07]:
                        if t==0.5:
                                self.activate_zooming(animate=True)
                                self.play(FadeOut(my_brace_h,num_h),**self.anim_kwargs)
                        self.play(my_rects.set_width,t,{"stretch":True},**self.anim_kwargs)
                self.wait()

class Exa(Scene):
        def construct(self):
                r1=Square()
                r2=Circle().move_to(3*LEFT)
                self.play(ShowCreation(r1))
                self.play(TransformFromCopy(r1,r2))
                self.wait()
        
class Transforming(Scene):
        def construct(self):
                my_function=TexMobject("\\sum_R f(x) \\Delta x", "=","\\int_R f(x)dx")
                my_function.arrange(RIGHT,buff=0.1)
                self.play(Write(my_function[0]))
                for t in [1,2]:
                        self.play(TransformFromCopy(my_function[0],my_function[t]))
                        self.wait(2)
                self.wait(2)

class ThisIsTheEnd(GraphScene):
        CONFIG={
                "x_min":-4,
                "x_max":4,
                "y_min":-3,
                "y_max":3,
                "x_axis_width":8,
                "y_axis_height":6,
                "graph_origin":ORIGIN
        }
        def count_area(i_from,i_to,function,dx):
                x=np.arange(i_from+10*dx,i_to+dx,dx)
                dy=func(x)*dx
                return np.sum(dy)
        def curve(x,dx):
                return lambda x: np.cos(x+dx)+np.sin(1.7*(x+dx))
        def construct(self):
                self.setup_axes(animate=True)
                my_graph=self.get_graph(self.curve(0))
                my_rects=self.get_riemann_rectangles_list(
                        graph=my_graph,max_dx=1,input_sample_type="center",n_iterations=7
                )
                self.play(ShowCreation(my_graph))
                self.play(FadeIn(my_rects[0]))
                for t in my_rects[1:]:
                        self.transform_between_riemann_rects(my_rects[0],t,run_time=3)
                self.wait(2)