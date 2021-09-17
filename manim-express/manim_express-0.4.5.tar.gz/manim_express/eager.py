import random
import time
import sys
from functools import wraps
import shutil
import numpy as np
from manimlib.utils.config_ops import digest_config
# from manimlib.scene.scene_file_writer import SceneFileWriter
from manimlib import Scene, Point, Camera, ShowCreation, Write, Color, VGroup, VMobject
from manimlib.utils.rate_functions import linear, smooth
from manimlib.extract_scene import get_scene_config
import manimlib.config
from manimlib.utils.color import rgb_to_hex
from manimlib.config import Size
from sparrow import ppath
from .plot import Plot, PlotObj, xyz_to_points
from .onlinetex import tex_to_svg_file_online
import manimlib.mobject.svg.tex_mobject
from pyglet.window import key
from .jupyter import JupyterDisplay
from pathlib import Path
from .jupyter import video

__all__ = ["EagerModeScene", "JupyterModeScene", "Size", "CONFIG", "PlotObj", "xyz_to_points"]


class CONFIG:
    # skip_animations = False  # "Save the last frame"
    color = None  # Background color"
    full_screen = False
    gif = False
    resolution = '1920x1080'

    # Render to a movie file with an alpha channel,
    # if transparent is True, .mov file will be generated.
    transparent = False
    save_pngs = False  # Save each frame as a png
    hd = False
    uhd = False
    quiet = True
    open = False  # Automatically open the saved file once its done
    finder = False  # Show the output file in finder
    frame_rate = 30
    write_file = False
    file_name = None
    video_dir = None  # directory to write video
    start_at_animation_number = None
    use_online_tex = False


class EagerModeScene(Scene):
    def __init__(
            self,
            screen_size=Size.big,
            scene_name='EagerModeScene',
            # CONFIG=None,
    ):
        # self.CONFIG = CONFIG
        args = manimlib.config.parse_cli()
        args_dict = vars(args)
        args_dict['file'] = None
        args_dict['scene_names'] = scene_name
        args_dict['screen_size'] = screen_size
        for key, value in CONFIG.__dict__.items():
            args_dict[key] = value

        if CONFIG.gif is True:
            args_dict['write_file'] = True
            # if CONFIG.gif is True:
            #     args_dict["transparent"] = False

        if CONFIG.use_online_tex:
            print("Use online latex compiler")
            manimlib.mobject.svg.tex_mobject.tex_to_svg_file = tex_to_svg_file_online

        self.config = manimlib.config.get_configuration(args)
        self.scene_config = get_scene_config(self.config)

        super().__init__(**self.scene_config)

        self.virtual_animation_start_time = 0
        self.real_animation_start_time = time.time()
        self.file_writer.begin()

        self.setup()
        self.plt = Plot()
        self.is_axes_line_gen_ed = False

        self.clips = []
        self.current_clip = 1
        self.current_clip = 0
        self.saved_states = []
        self.animation_list = []
        self.animation_func_dict = {}
        self.loop_start_animation = None
        self.pause_start_animation = 0

    def play(self, *args, run_time=1, rate_func=linear, **kwargs):
        """TODO:"""
        super().play(*args, run_time=run_time, rate_func=rate_func, **kwargs)

    # def clip1(self):
    #     pass

    def get_animate_name_func(self, n=10):
        animation_func_dict = {}
        for i in range(n):
            try:
                func_name = f"clip{i}"
                func = getattr(self, func_name)
                animation_func_dict.setdefault(func_name, func)
            except:
                continue
        self.animation_func_dict = animation_func_dict

    def render(self):
        self.get_animate_name_func()
        for name, func in self.animation_func_dict.items():
            self.save_state()
            self.saved_states.append(self.saved_state)
            self.current_clip += 1
            func()
            self.animation_list.append(func)
            self.hold_on()

    def replay(self, animation_index=None):
        if animation_index is None:
            animation_index = self.current_clip
        self.saved_state = self.saved_states[animation_index - 1]
        self.restore()
        self.animation_list[animation_index - 1]()

    def loop_animate(self, animation_index=None, num=10):
        while num:
            num -= 1
            self.replay(animation_index)

    def next_animate(self):
        self.current_clip += 1

    def _clip_control(self, symbol):
        # play preview clip
        if symbol in (key.LEFT, key.COMMA, key.NUM_1, key._1):
            self.current_clip -= 1
            try:
                self.replay(self.current_clip)
            except IndexError:
                self.current_clip += 1

        # play next clip
        elif symbol in (key.RIGHT, key.PERIOD, key._3, key.NUM_3):
            self.current_clip += 1
            try:
                self.replay(self.current_clip)
            except IndexError:
                self.current_clip -= 1

        # play current clip
        elif symbol in (key.NUM_DIVIDE, key.DOWN, key._2, key.NUM_2):
            self.replay(self.current_clip)

    def hold_on(self):
        """ Equal to self.tear_down(). """
        self.stop_skipping()
        self.file_writer.finish()
        if self.window and self.linger_after_completion:
            self.interact()

    def tear_down(self):
        super().tear_down()

    def get_config(self):
        return self.config

    def save_default_config(self):
        """Save the default config file to current directory."""
        shutil.copy(ppath("custom_config.yml", __file__), 'custom_config.yml')

    def get_scene_config(self):
        return self.scene_config

    def save_start(self, file_name):
        """TODO"""
        pass

    def save_end(self):
        # self.file_writer.finish()
        pass

    def embed(self):
        super().embed()

    # FIXME: Remove method `plot` from EagerModeScene.
    def plot(self,
             x,
             y,
             color=None,
             width=2,
             axes_ratio=0.62,
             scale_ratio=None,
             num_decimal_places=None,
             show_axes=True,
             include_tip=True,
             x_label='x',
             y_label='y'):

        """
        params
        ------

        scale_ratio: Scale ratio of coordinate axis. i.e. y / x .
        num_decimal_places: Number of significant digits of coordinate_labels.
        """
        self.plt.plot(x, y, color, width, axes_ratio, scale_ratio, show_axes, include_tip, num_decimal_places,
                      x_label, y_label)

    def plot3d(self, x, y, z, width=2, axes_ratio=0.62, show_axes=True):
        """TODO"""
        pass

    def get_plot_mobj(self):
        if self.is_axes_line_gen_ed is False:
            self.plt.gen_axes_lines()
        self.is_axes_line_gen_ed = True
        axes_lines_dict = self.plt.get_axes_lines()
        axes_mobj = VGroup(*axes_lines_dict["axes"])
        lines_mobj = VGroup(*axes_lines_dict["line"])
        return axes_mobj, lines_mobj

    def get_plot_axes(self):
        return self.plt.get_axes()

    def reset_plot(self):
        self.plt = Plot
        self.is_axes_line_gen_ed = False

    def show_plot(self, play=True, reset=True):
        axes_mobj, lines_mobj = self.get_plot_mobj()
        random.seed(time.time())
        if play:
            def play_func(Func):
                if len(axes_mobj):
                    self.play(ShowCreation(axes_mobj),
                              run_time=1, rate_func=smooth)
                self.play(Func(lines_mobj), run_time=1, rate_func=smooth)

            if random.random() > 0.5:
                play_func(Write)
            else:
                play_func(ShowCreation)
        else:
            self.add(VGroup(axes_mobj,
                            lines_mobj))

        if reset:
            self.plt = Plot()


class JupyterModeScene(EagerModeScene):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def finish(self):
        self.file_writer.finish()

    def embed(self):
        """We don't need it in jupyter lab/notebook."""
        pass

    @property
    def video_path(self):
        self.file_writer.finish()
        path = Path(self.file_writer.get_movie_file_path())
        relative_path = path.relative_to(Path.cwd())
        # video(relative_path)
        return relative_path


    def quit(self):
        """Please use exit() or quit() in jupyter cell."""
        pass
