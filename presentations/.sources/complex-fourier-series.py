from manim_tweaked import *
from manim_editor import PresentationSectionType

config.window_monitor = 0
config.fullscreen = 1

N = PresentationSectionType.NORMAL
SN = PresentationSectionType.SUB_NORMAL
CL = PresentationSectionType.SUB_COMPLETE_LOOP


class ComplexFunctions(Scene):
    def construct(self):
        self.next_section("Real", N)
        self.wait()
        self.next_section(type=SN)
        real_axis = Axes().add_coordinates()
        self.play(Write(real_axis))
        plot = real_axis.plot(np.sin, color=RED)
        self.play(Create(plot))

        self.next_section(type=SN)
        self.play(
            Indicate(real_axis.get_axes()[0]), Write(inp := Text("Input").to_corner(UR))
        )

        self.next_section(type=SN)
        self.play(
            Indicate(real_axis.get_axes()[1]),
            Unwrite(inp),
            Write(outp := Text("Output").to_corner(UL)),
        )

        self.next_section(type=SN)
        self.play(FadeOut(*self.mobjects))

        self.next_section("Complex", N)
        complex_axis = ComplexPlane().add_coordinates()
        self.play(Write(complex_axis))

        self.next_section(type=SN)
        self.play(Write(outp))

        self.next_section(type=SN)
        complex_func_tex = MathTex("f(t)=3\exp(it)", "+\exp(-it)").to_corner(UR)
        complex_func_tex[0].save_state().to_corner(UR)
        x_var = (
            Variable(0, "t")
            .next_to(complex_func_tex, DOWN)
            .add_updater(lambda m: m.to_edge(RIGHT))
        )
        fx_vect = always_redraw(
            lambda: Vector(
                complex_to_R3((lambda x: 3 * np.exp(x * 1j))(x_var.tracker.v)),
                color=RED,
            )
        )
        self.play(Write(complex_func_tex[0]), Write(x_var), GrowArrow(fx_vect))

        self.next_section(type=CL)
        dissipating = TracedPath(
            fx_vect.get_end, stroke_color=RED, dissipating_time=0.2
        )
        self.add(dissipating)
        self.play(x_var.tracker.a.set_value(2 * np.pi), run_time=3)

        self.next_section("Addition of functions", N)
        self.play(FadeOut(dissipating))
        fx_vect_2 = always_redraw(
            lambda: Vector(
                complex_to_R3((lambda x: np.exp(x * -1j))(x_var.tracker.v)), color=RED
            ).shift(fx_vect.get_end())
        )
        x_var.tracker.v = 0
        dissipating = TracedPath(
            fx_vect_2.get_end, stroke_color=RED, dissipating_time=0.2
        )
        self.play(
            Write(complex_func_tex[1]),
            Restore(complex_func_tex[0]),
            GrowArrow(fx_vect_2),
        )

        self.next_section(type=CL)
        self.add(dissipating)
        self.play(x_var.tracker.a.set_value(2 * np.pi), run_time=3)

        self.next_section(type=SN)
        fx_vect.clear_updaters()
        dissipating.clear_updaters()
        self.play(
            GrowArrow(fx_vect, reverse_rate_function=True),
            GrowArrow(fx_vect_2, reverse_rate_function=True),
            FadeOut(dissipating),
        )
        self.remove(fx_vect, fx_vect_2)

        fx_vect = always_redraw(
            lambda: Vector(
                complex_to_R3((lambda x: 3 * np.exp(x * 1j))(x_var.tracker.v)),
                color=RED,
            )
        )
        fx_vect_2 = always_redraw(
            lambda: Vector(
                complex_to_R3((lambda x: 3 * np.exp(x * -1j))(x_var.tracker.v)),
                color=RED,
            ).shift(fx_vect.get_end())
        )
        self.play(FadeOut(complex_func_tex, x_var))

        self.next_section(type=SN)
        self.play(
            ShowPassingFlashWithThinningStrokeWidth(
                complex_axis.get_axis(0).copy().set_stroke(color=YELLOW, width=5)
            )
        )

        self.next_section(type=SN)
        self.add(x_var.tracker)
        self.play(
            GrowArrow(fx_vect),
            GrowArrow(fx_vect_2),
        )
        x_var.tracker.v = 0

        self.next_section(type=CL)
        self.play(x_var.tracker.a.set_value(2 * np.pi), run_time=3)

        self.next_section(type=SN)
        self.play(FadeOut(fx_vect, fx_vect_2))
        x_var.tracker.v = 0

        self.next_section("Full example", N)

        amplitude_func = lambda n: 3 * 1j / n / np.pi * ((-1) ** n - 1)
        vects = [Vector(RIGHT * 0)]
        for i in range(1, 11):
            vects += [
                Vector(complex_to_R3(amplitude_func(i)), color=RED)
                .shift(vects[-1].get_end())
                .add_updater(lambda m, dt, i=i: m.rotate(i * dt))
            ]
            vects += [
                Vector(complex_to_R3(amplitude_func(-i)), color=RED)
                .shift(vects[-1].get_end())
                .add_updater(lambda m, dt, i=i: m.rotate(-i * dt))
            ]
        for n, i in enumerate(vects[1:]):
            i.add_updater(lambda m, n=n: m.shift(vects[n].get_end() - m.get_start()))
        dissipating = TracedPath(vects[-1].get_end, 5, YELLOW, 0.1)
        [i.suspend_updating() for i in vects]
        self.play(LaggedStart(*(GrowArrow(i) for i in vects)))
        [i.resume_updating() for i in vects]
        self.add(dissipating)
        self.next_section(type=CL)
        self.wait(2 * PI)
        self.next_section(type=SN)
        self.play(FadeOut(*self.mobjects))
        self.wait()
