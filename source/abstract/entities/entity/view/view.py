from pygame import math
from source.library.action import action
from animation_config import stand

class View:
    dimensions      = None
    render_offset   = None

    animation       = None
    draw_radius     = True
    stroke          = 1
    stroke_color    = (0, 128, 0)

    def __init__(self):
        self.render_offset = math.Vector3(0, 0, 0)
        self.dimensions = math.Vector3(0, 0, 0)
        pass

    def get_render_offset(self):
        self.render_offset.x = -(self.dimensions.x / 2)
        self.render_offset.y = -(self.dimensions.y)
        return self.render_offset

    def set_animation(self):
        if abs(self.get_velocity().length()) == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.data)

    def on_render(self):
        self.set_animation()
        self.animation.on_render(self)
        pass

    def pretty_print(self, i = 0):
        print(" "*i)
