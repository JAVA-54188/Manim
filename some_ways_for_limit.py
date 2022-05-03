from manim import *
# import manimpango


class some_ways_for_limit(Scene):

    FONT_EN = "Arial"
    FONT_CN = "STZhongsong"

    # 开头
    def begin(self):

        background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"

        bg = Square(color=background_color, side_length=config["frame_width"], fill_opacity=1)

        self.add(bg)

        triangle = Triangle(color=logo_red,
                            fill_opacity=1).shift(RIGHT + RIGHT * 1)

        self.play(Create(triangle))

        square = Square(color=logo_blue, fill_opacity=1).shift(UP + RIGHT * 1)

        self.play(Create(square))

        circle = Circle(color=logo_green,
                        fill_opacity=1).shift(LEFT + RIGHT * 1)

        self.play(Create(circle))

        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)

        self.play(Write(ds_m))

        self.play(ds_m.animate.shift(2.25 * LEFT + 1.5 * UP + RIGHT * 1))

        logo = VGroup(bg, triangle, square, circle, ds_m)

        self.play(FadeOut(logo))

    # 第一部分
    def section_1(self):
        proverb_en = Text(
            "There are no easy answers; there's only living through the questions.",
            font_size=30,
            font=self.FONT_EN)
        proverb_cn = Text("生活没有容易的答案，只有去克服重重问题。",
                          font_size=30,
                          font=self.FONT_CN)
        author = Text("————Elizabeth George", font_size=30, font=self.FONT_EN)
        group = VGroup(proverb_en, author, proverb_cn).arrange(DOWN, buff=0.5)
        group[1].to_corner(RIGHT)

        self.play(Write(group, run_time=8))
        self.wait()
        self.play(FadeOut(group, shift=DOWN))
        self.next_section()

    # 第二部分
    def section_2(self):
        title = Text("极限的几种计算方法", font_size=40, font=self.FONT_CN)
        method_1 = Text(
            "1.利用基本极限求极限",
            font_size=30,
            font=self.FONT_CN,
        ).to_corner(UL)

        self.play(Write(title, run_time=2))
        self.play(TransformMatchingShapes(title, method_1))

        equation_1 = MathTex(r'\lim_{x \to \infty}',
                             r'\frac{x^{x+1}}{(x+1)^x}', r'\sin\frac{1}{x}')

        equation_2 = MathTex(r'\lim_{x \to \infty}', r'\frac{x^{x}x}{(x+1)^x}',
                             r'\sin\frac{1}{x}')

        equation_3 = MathTex(r'\lim_{x \to \infty}', r'\frac{x^{x}}{(x+1)^x}',
                             r'\frac{\sin\frac{1}{x}}{\frac{1}{x}}')

        equation_4 = MathTex(r'\lim_{x \to \infty}',
                             r'\left[\frac{x}{(x+1)}\right ]^{x}',
                             r'\frac{\sin\frac{1}{x}}{\frac{1}{x}}')
        equation_5 = MathTex(r'\lim_{x \to \infty}',
                             r'\left[\frac{1}{(1+\frac{1}{x})}\right ]^{x}',
                             r'\frac{\sin\frac{1}{x}}{\frac{1}{x}}')
        equation_6 = MathTex(r'\lim_{x \to \infty}',
                             r'\frac{1}{(1+\frac{1}{x})^{x}}',
                             r'\frac{\sin\frac{1}{x}}{\frac{1}{x}}')

        because_1 = MathTex(
            r'\because \lim_{x \to \infty} (1+\frac{1}{x})^{x}=e')

        therefore_1 = MathTex(
            r'\therefore \lim_{x \to \infty} \frac{1}{(1+\frac{1}{x})^{x}}=\frac{1}{e}'
        )

        be_there_1 = VGroup(because_1, therefore_1).arrange(DOWN)

        because_2 = MathTex(r'\because \lim_{x \to 0} \frac{\sin x}{x} =1')

        therefore_2 = MathTex(
            r'\therefore \lim_{x \to \infty} \frac{\sin\frac{1}{x}}{\frac{1}{x}} =1'
        )

        self.play(Write(equation_1))
        self.wait()
        self.play(ReplacementTransform(equation_1, equation_2))
        self.wait()
        self.play(ReplacementTransform(equation_2, equation_3))
        self.wait()
        self.play(ReplacementTransform(equation_3, equation_4))
        self.wait()
        self.play(ReplacementTransform(equation_4, equation_5))
        self.wait()
        self.play(ReplacementTransform(equation_5, equation_6))
        self.wait()
        self.play(equation_6.animate.shift(UP * 3))
        self.wait()
        self.play(Write(be_there_1), run_time=2)
        self.wait()
        self.play(be_there_1.animate.shift(LEFT * 3))
        self.wait()

        be_there_2 = VGroup(because_2,
                            therefore_2).arrange(DOWN).shift(RIGHT * 3)

        self.play(Write(be_there_2), run_time=2)
        self.wait()

        wiggle_1 = VGroup(equation_6[1], therefore_1)

        self.play(Wiggle(wiggle_1))
        self.wait()

        wiggle_2 = VGroup(equation_6[2], therefore_2)

        self.play(Wiggle(wiggle_2))
        self.wait()

        fadeout_1 = VGroup(because_1, because_2)

        self.play(FadeOut(fadeout_1, shift=UP))
        self.wait()

        equation_7 = MathTex(
            r'=\lim_{x \to \infty}',
            r'\frac{1}{e}',
            r'\quad1',
        ).next_to(equation_6, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_7[0]))
        self.wait()
        self.play(TransformMatchingShapes(therefore_1, equation_7[1]))
        self.wait()
        self.play(TransformMatchingShapes(therefore_2, equation_7[2]))
        self.wait()

        equation_8 = MathTex(r'=\frac{1}{e}').next_to(equation_7,
                                                      DOWN,
                                                      aligned_edge=LEFT)
        self.play(Write(equation_8))
        self.wait()

        destroy = VGroup(method_1, equation_6, equation_7, equation_8)

        self.play(Unwrite(destroy))
        self.next_section()

    # 第三部分
    def section_3(self):

        method_2 = Text(
            "2.利用等价无穷小求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_2))
        self.wait()
        self.play(method_2.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(r'\lim_{x \to 0}', r'\frac{\ln(\cos x)}{x^2}')

        self.play(Write(equation_1))
        self.wait()

        equation_2 = MathTex(r'\lim_{x \to 0}',
                             r'\frac{\ln\left[1+(\cos x -1)\right]}{x^2}')

        self.play(ReplacementTransform(equation_1, equation_2))
        self.wait()

        equation_3 = MathTex(r'\lim_{x \to 0}',
                             r'\ln\left[1+(\cos x -1)\right]',
                             r'\frac{1}{x^2}')

        self.play(ReplacementTransform(equation_2, equation_3))
        self.wait()
        self.play(equation_3.animate.shift(UP * 3 + RIGHT * 0.5))
        self.wait()

        because_1 = MathTex(r'\because x \to 0,x\sim \ln (1+x)')

        therefore_1 = MathTex(
            r'\therefore \ln\left[1+(\cos x -1)\right]\sim \cos x -1')

        be_there_1 = VGroup(because_1, therefore_1).arrange(DOWN)

        self.play(Write(be_there_1))
        self.wait()

        indicate_1 = VGroup(equation_3[1], therefore_1)

        self.play(Indicate(indicate_1, color=None))
        self.wait()
        self.play(FadeOut(because_1, shift=RIGHT))
        self.wait()

        equation_4 = MathTex(r'=\lim_{x \to 0}', r'(\cos x -1)',
                             r'\frac{1}{x^2}').next_to(equation_3,
                                                       DOWN,
                                                       aligned_edge=LEFT)
        self.play(Write(equation_4[0]))
        self.wait()

        self.play(TransformMatchingShapes(therefore_1, equation_4[1]))
        self.play(Write(equation_4[2]))
        self.wait()

        because_2 = MathTex(r'\because x\to 0, 1-\cos x\sim \frac{1}{2}x^2')

        therefore_2 = MathTex(r'\therefore \cos x-1\sim -\frac{1}{2}x^2')

        be_there_2 = VGroup(because_2, therefore_2).arrange(DOWN)

        self.play(Write(be_there_2))
        self.wait()

        indicate_2 = VGroup(equation_4[1], therefore_2)

        self.play(Indicate(indicate_2, color=None))
        self.wait()
        self.play(FadeOut(because_2, shift=LEFT))

        equation_5 = MathTex(r'=\lim_{x \to 0}', r'-\frac{x^2}{2}',
                             r'\frac{1}{x^2}').next_to(equation_4,
                                                       DOWN,
                                                       aligned_edge=LEFT)

        self.play(Write(equation_5[0]))
        self.wait()
        self.play(TransformMatchingShapes(therefore_2, equation_5[1]))
        self.wait()
        self.play(Write(equation_5[2]))
        self.wait()

        equation_6 = MathTex(r'=-\frac{1}{2}').next_to(equation_5,
                                                       DOWN,
                                                       aligned_edge=LEFT)

        self.play(Write(equation_6))
        self.wait()

        destroy = VGroup(method_2, equation_3, equation_4, equation_5,
                         equation_6)

        self.play(Uncreate(destroy))
        self.wait()
        self.next_section()

    # 第四部分
    def section_4(self):

        method_3 = Text(
            "3.利用有理运算法则求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_3))
        self.wait()
        self.play(method_3.animate.to_corner(UL))
        self.wait()

        str_1 = Text(
            '若',
            font_size=30,
            font=self.FONT_CN,
        )
        equation = MathTex(
            r'\lim_{x \to 0}  \left [ \frac{1}{x} -(\frac{1}{x}-a)e^x  \right ] =1 '
        )
        str_2 = Text(
            ',则a等于？',
            font_size=30,
            font=self.FONT_CN,
        )

        question = VGroup(str_1, equation, str_2).arrange(RIGHT)

        self.play(Write(question))
        self.wait()
        self.play(question.animate.shift(UP * 2))
        self.wait()

        equation_1 = question[1].copy()

        self.play(equation_1.animate.shift(DOWN * 2))
        self.wait()

        equation_2 = MathTex(
            r'\lim_{x \to 0}  \left [ \frac{1}{x} -\frac{e^x}{x}+ae^x  \right ] =1'
        )

        self.play(ReplacementTransform(equation_1, equation_2))
        self.wait()

        equation_3 = MathTex(
            r'\lim_{x \to 0}  \left [ \frac{1-e^x}{x}+ae^x  \right ] =1')

        self.play(ReplacementTransform(equation_2, equation_3))
        self.wait()

        equation_4 = MathTex(
            r'\lim_{x \to 0} \frac{1-e^x}{x}+\lim_{x \to 0} ae^x  =1')

        self.play(ReplacementTransform(equation_3, equation_4))
        self.wait()

        equation_5 = MathTex(
            r'\lim_{x \to 0} \frac{-x}{x}+\lim_{x \to 0} ae^x  =1')

        self.play(ReplacementTransform(equation_4, equation_5))
        self.wait()

        equation_6 = MathTex(r'{{-1}}+{{a}}={{1}}')

        self.play(ReplacementTransform(equation_5, equation_6))
        self.wait()

        equation_7 = MathTex(r'{{a}}={{1}}+{{1}}')

        self.play(TransformMatchingTex(equation_6, equation_7))
        self.wait()

        equation_8 = MathTex(r'{{a}}={{2}}')

        self.play(TransformMatchingTex(equation_7, equation_8))
        self.wait()

        destroy = VGroup(method_3, question, equation_8)

        self.play(Unwrite(destroy))
        self.wait()
        self.next_section()

    # 第五部分
    def section_5(self):
        method_4 = Text(
            "4.利用洛必达法则求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_4))
        self.wait()
        self.play(method_4.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(r'\lim_{x \to 0}', r'\frac{\ln(\cos x)}{x^2}')

        self.play(Write(equation_1))
        self.wait()

        framebox_1 = SurroundingRectangle(equation_1[1])

        self.play(Create(framebox_1))
        self.wait()

        equation_2 = MathTex(r'\longrightarrow \frac{0}{0} ').next_to(
            equation_1, RIGHT)

        self.play(Write(equation_2))
        self.wait()

        group_1 = VGroup(framebox_1, equation_2)

        self.play(Unwrite(group_1))
        self.wait()
        self.play(equation_1.animate.shift(UP * 3))
        self.wait()

        equation_3 = MathTex(
            r'=\lim_{x \to 0}',
            r"\frac{\left [ \ln(\cos x) \right ]'}{\left [ x^2 \right ]'}"
        ).next_to(equation_1, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_3))
        self.wait()

        equation_4 = MathTex(r"\left [ \ln(\cos x) \right ]'=",
                             r'\frac{-\sin x}{\cos x}').shift(DOWN * 0.1)

        equation_5 = MathTex(r"\left [ x^2 \right ]'=",
                             r'2x').next_to(equation_4, DOWN)

        derivation_1 = VGroup(equation_4, equation_5)

        self.play(Write(derivation_1))
        self.wait()

        equation_6 = MathTex(r'-\tan x').next_to(derivation_1[0],
                                                 RIGHT,
                                                 aligned_edge=LEFT,
                                                 buff=0.7)

        self.play(TransformMatchingShapes(derivation_1[0][1], equation_6))
        self.wait()

        equation_7 = MathTex(r"\frac{-\tan x}{2x}").next_to(
            equation_3[0], RIGHT)

        self.play(TransformMatchingShapes(equation_3[1], equation_7))
        self.wait()

        derivation_group_1 = VGroup(equation_4[0], equation_5, equation_6)

        self.play(FadeOut(derivation_group_1))
        self.wait()

        framebox_2 = SurroundingRectangle(equation_7)

        self.play(Create(framebox_2))
        self.wait()

        equation_8 = MathTex(r'\longrightarrow \frac{0}{0} ').next_to(
            framebox_2, RIGHT)

        self.play(Write(equation_8))
        self.wait()

        group_2 = VGroup(framebox_2, equation_8)

        self.play(Uncreate(group_2))
        self.wait()

        equation_9 = MathTex(
            r"\frac{\left [  -\tan x \right ]'}{\left [  2x \right ]’}"
        ).next_to(equation_3[0], RIGHT)

        self.play(TransformMatchingShapes(equation_7, equation_9))
        self.wait()

        equation_10 = MathTex(
            r"\left [ \ln(\cos x) \right ]''= \left [  -\tan x \right ]'=-\sec ^2 x"
        )

        equation_11 = MathTex(
            r"\left [  x^2 \right ]’'=\left [  2x \right ]’=2")

        derivation_2 = VGroup(equation_10, equation_11).arrange(DOWN)

        self.play(Write(derivation_2))
        self.wait()

        self.remove(equation_9)

        equation_12 = MathTex(r'\frac{-\sec ^2 x}{2}').next_to(
            equation_3[0], RIGHT)

        self.play(TransformMatchingShapes(derivation_2, equation_12))
        self.wait()

        equation_13 = MathTex(r'=-\frac{1}{2}').next_to(equation_3[0],
                                                        DOWN,
                                                        aligned_edge=LEFT)

        self.play(Write(equation_13))
        self.wait()

        destroy = VGroup(method_4, equation_1, equation_3[0], equation_12,
                         equation_13)

        self.play(Uncreate(destroy))
        self.wait()
        self.next_section()

    # 第六部分
    def section_6(self):
        equation_scale = 0.75
        process_scale = 0.6

        method_5 = Text(
            "5.利用泰勒公式求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_5))
        self.wait()
        self.play(method_5.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(
            r'\lim_{x \to 0} \frac{\ln(1+x)-(x-\frac{5}{2} x^2)}{x^2} ').scale(
                equation_scale)

        self.play(Write(equation_1))
        self.wait()
        self.play(equation_1.animate.shift(UP * 2.5))
        self.wait()

        because_1 = MathTex(
            r"\because &f(x) = f(x_0)+f'(x_0)(x-x_0)+\frac{f''(x_0)}{2!} (x-x_0)^2+\cdots +\frac{f^{(n)}(x_0)}{n!} (x-x_0)^n+o(x-x_0)^n\\&x_0=0"
        ).scale(process_scale)

        therefore_1 = MathTex(
            r"\therefore f(x) = f(0)+f'(0)x+\frac{f''(0)}{2!} x^2+\cdots +\frac{f^{(n)}(0)}{n!}x^n+o(x^n)"
        ).scale(process_scale)

        therefore_2 = MathTex(
            r"\ln (1+x) =x-\frac{x^2}{2}+\cdots+(-1)^{n-1}\frac{x^n}{n}+o(x^n)"
        ).scale(process_scale)

        process = VGroup(because_1, therefore_1, therefore_2).arrange(DOWN)

        sub_process = VGroup(because_1, therefore_1)

        self.play(Write(process), run_time=6)
        self.wait()
        self.play(FadeOut(sub_process))
        self.wait()

        equation_2 = MathTex(
            r'=\lim_{x \to 0} ',
            r'\frac{(x-\frac{x^2}{2})-(x-\frac{5}{2} x^2)}{x^2} ').scale(
                equation_scale).next_to(equation_1, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_2[0]))
        self.wait()
        self.play(TransformMatchingShapes(therefore_2, equation_2[1]))

        equation_3 = equation_2.copy()

        equation_4 = MathTex(r'=\lim_{x \to 0}\frac{\frac{4}{2} x^2}{x^2}'
                             ).scale(equation_scale).next_to(equation_2,
                                                             DOWN,
                                                             aligned_edge=LEFT)

        self.play(TransformMatchingShapes(equation_3, equation_4))
        self.wait()

        equation_5 = equation_4.copy()

        equation_6 = MathTex(r'=2').scale(equation_scale).next_to(
            equation_4, DOWN, aligned_edge=LEFT)

        self.play(TransformMatchingShapes(equation_5, equation_6))
        self.wait()

        destroy = VGroup(method_5, equation_1, equation_2, equation_4,
                         equation_6)

        self.play(Unwrite(destroy))
        self.wait()
        self.next_section()

    # 第七部分
    def section_7(self):

        method_6 = Text(
            "6.利用夹逼原理求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_6))
        self.wait()
        self.play(method_6.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(
            r'\lim_{n \to \infty}(\frac{1}{n^2+n+1}+\frac{2}{n^2+n+2}+\dots+\frac{n}{n^2+n+n})'
        )

        self.play(Write(equation_1))
        self.wait()

        equation_2 = MathTex(
            r'\lim_{n \to \infty}\sum_{i=1}^{n} \frac{i}{n^2+n+i}')

        self.play(ReplacementTransform(equation_1, equation_2))
        self.wait()

        lte_1 = MathTex(r'\le').next_to(equation_2, LEFT)

        lte_2 = MathTex(r'\le').next_to(equation_2, RIGHT)

        equation_3 = MathTex(
            r'\lim_{n \to \infty}\sum_{i=1}^{n} \frac{i}{n^2+n+n}').next_to(
                lte_1, LEFT)

        equation_4 = MathTex(
            r'\lim_{n \to \infty}\sum_{i=1}^{n} \frac{i}{n^2+n+1}').next_to(
                lte_2, RIGHT)

        self.play(Write(lte_1))
        self.wait()
        self.play(Write(equation_3))
        self.wait()
        self.play(Write(lte_2))
        self.wait()
        self.play(Write(equation_4))
        self.wait()

        equation_5 = MathTex(
            r'\lim_{n \to \infty}\frac{\sum\limits_{i=1}^{n}i}{n^2+n+n}'
        ).next_to(lte_1, LEFT)

        equation_6 = MathTex(
            r'\lim_{n \to \infty}\frac{\sum\limits_{i=1}^{n}i}{n^2+n+1}'
        ).next_to(lte_2, RIGHT)

        self.play(ReplacementTransform(equation_3, equation_5))
        self.wait()
        self.play(ReplacementTransform(equation_4, equation_6))
        self.wait()

        equation_7 = MathTex(
            r'\lim_{n \to \infty}\frac{1+2+\cdots+n}{n^2+n+n}').next_to(
                lte_1, LEFT).scale(0.9)

        equation_8 = MathTex(
            r'\lim_{n \to \infty}\frac{1+2+\cdots+n}{n^2+n+1}').next_to(
                lte_2, RIGHT).scale(0.9)

        self.play(ReplacementTransform(equation_5, equation_7))
        self.wait()
        self.play(ReplacementTransform(equation_6, equation_8))
        self.wait()

        equation_9 = MathTex(
            r'\lim_{n \to \infty}\frac{\frac{n(n+1)}{2} }{n^2+n+n}').next_to(
                lte_1, LEFT).scale(0.9)

        equation_10 = MathTex(
            r'\lim_{n \to \infty}\frac{\frac{n(n+1)}{2} }{n^2+n+1}').next_to(
                lte_2, RIGHT).scale(0.9)

        self.play(ReplacementTransform(equation_7, equation_9))
        self.wait()
        self.play(ReplacementTransform(equation_8, equation_10))
        self.wait()

        equation_11 = MathTex(r'\frac{1}{2}').next_to(lte_1, LEFT)

        equation_12 = MathTex(r'\frac{1}{2}').next_to(lte_2, RIGHT)

        self.play(ReplacementTransform(equation_9, equation_11))
        self.wait()
        self.play(ReplacementTransform(equation_10, equation_12))
        self.wait()

        equation_13 = MathTex(r'=\frac{1}{2}').next_to(equation_2,
                                                       DOWN,
                                                       aligned_edge=LEFT)

        self.play(Write(equation_13))
        self.wait()

        destroy = VGroup(method_6, equation_2, lte_1, lte_2, equation_11,
                         equation_12, equation_13)

        self.play(Uncreate(destroy))
        self.wait()
        self.next_section()

    # 第八部分
    def section_8(self):

        equation_scale = 0.75
        process_scale = 0.6

        method_7 = Text(
            "7.拉格朗日中值定理求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_7))
        self.wait()
        self.play(method_7.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(
            r'\lim_{x \to +\infty} (\sqrt[]{x^2+x}-\sqrt[]{x^2-x})').scale(
                equation_scale)

        self.play(Write(equation_1))
        self.wait()

        equation_2 = MathTex(
            r'\lim_{x \to +\infty} x(\sqrt[]{1+\frac{1}{x} }-\sqrt[]{1-\frac{1}{x}})'
        ).scale(equation_scale)

        self.play(ReplacementTransform(equation_1, equation_2))
        self.wait()
        self.play(equation_2.animate.shift(UP * 2.9))
        self.wait()

        text_1 = Text('令')

        equation_3 = MathTex(r'f(u) = \sqrt[]{1+u}')

        process_1 = VGroup(
            text_1, equation_3).scale(process_scale).arrange(RIGHT).next_to(
                equation_2, DOWN)

        text_2 = Text('则')

        equation_4 = MathTex(
            r"f(\frac{1}{x})-f(-\frac{1}{x}) =",
            r"f'(\xi)(\frac{1}{x}+\frac{1}{x}),-\frac{1}{x}<\xi<\frac{1}{x}")

        process_2 = VGroup(
            text_2, equation_4).scale(process_scale).arrange(RIGHT).next_to(
                process_1, DOWN)

        self.play(Write(process_1))
        self.wait()
        self.play(Write(process_2))
        self.wait()

        process_3 = MathTex(
            r'f(\frac{1}{x})-f(-\frac{1}{x}) =\frac{1}{x\sqrt[]{1+\xi}},-\frac{1}{x}<\xi<\frac{1}{x}'
        ).scale(process_scale).next_to(process_2, DOWN)

        self.play(Write(process_3))
        self.wait()

        process_4 = MathTex(
            r'\because x \to +\infty\therefore -\frac{1}{x}\to 0^-,\frac{1}{x}\to 0^+,\xi=0'
        ).scale(process_scale).next_to(process_3, DOWN)

        self.play(Write(process_4))
        self.wait()

        process_5 = MathTex(
            r'f(\frac{1}{x})-f(-\frac{1}{x})=\sqrt[]{1+\frac{1}{x} }-\sqrt[]{1-\frac{1}{x}}=\frac{1}{x} '
        ).scale(process_scale).next_to(process_4, DOWN)

        self.play(Write(process_5))
        self.wait()

        destroy_1 = VGroup(process_1, process_2, process_3, process_4)

        self.play(Uncreate(destroy_1))
        self.wait()

        equation_5 = MathTex(r'=\lim_{x \to +\infty}x\frac{1}{x}').scale(
            equation_scale).next_to(equation_2, DOWN, aligned_edge=LEFT)

        self.play(TransformMatchingShapes(process_5, equation_5))
        self.wait()

        equation_6 = MathTex(r'=1').scale(equation_scale).next_to(
            equation_5, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_6))
        self.wait()

        destroy_2 = VGroup(method_7, equation_2, equation_5, equation_6)

        self.play(Uncreate(destroy_2))
        self.wait()
        self.next_section()

    # 第九部分
    def section_9(self):

        method_8 = Text(
            "8.利用定积分定义求极限",
            font_size=30,
            font=self.FONT_CN,
        )

        self.play(Write(method_8))
        self.wait()
        self.play(method_8.animate.to_corner(UL))
        self.wait()

        equation_1 = MathTex(
            r'\lim_{n \to \infty}(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{n+n})'
        )

        self.play(Write(equation_1))
        self.wait()
        self.play(equation_1.animate.shift(UP * 2.5))
        self.wait()

        equation_2 = MathTex(
            r'=\lim_{n \to \infty}\frac{1}{n} (\frac{1}{1+\frac{1}{n}}+\frac{1}{1+\frac{2}{n}}+\cdots+\frac{1}{1+\frac{n}{n}})'
        ).next_to(equation_1, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_2))
        self.wait()

        equation_3 = MathTex(
            r'=\lim_{n \to \infty}\frac{1}{n}\sum_{i=1}^{n}(\frac{1}{1+\frac{i}{n}})'
        ).next_to(equation_2, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_3))
        self.wait()

        equation_4 = MathTex(r'=\int_{0}^{1}\frac{1}{1+x}dx').next_to(
            equation_3, DOWN, aligned_edge=LEFT)

        self.play(Write(equation_4))
        self.wait()

        equation_5 = MathTex(r'=\ln (1+x)\bigg|_{0}^{1}').next_to(
            equation_3, DOWN, aligned_edge=LEFT)

        self.play(ReplacementTransform(equation_4, equation_5))
        self.wait()

        equation_6 = MathTex(r'=\ln2').next_to(equation_5,
                                               DOWN,
                                               aligned_edge=LEFT)

        self.play(Write(equation_6))
        self.wait()

        destroy = VGroup(method_8, equation_1, equation_2, equation_3,
                         equation_5, equation_6)

        self.play(Unwrite(destroy))
        self.wait()
        self.next_section()

    # 结束
    def end(self):
        end_text = Text('Thank you for watching !',
                        t2g={
                            '[0:-1]': (BLUE_A, BLUE_E),
                        })
        self.play(Write(end_text))
        self.next_section()

    def construct(self):

        self.begin()

        self.section_1()

        self.section_2()

        self.section_3()

        self.section_4()

        self.section_5()

        self.section_6()

        self.section_7()

        self.section_8()

        self.section_9()

        self.end()