from pygame import math
from source.library.action import action
from animation_config import stand

class View:
    height = None
    width  = None

    animation = None

    render_offset = None

    def __init__(self):
        self.height = 32
        self.width = 32
        self.render_offset = math.Vector3(0, 0, 0)
        self.render_offset.x = -(self.width / 2)
        self.render_offset.y = -(self.height / 2)
        pass

    def set_animation(self):
        if abs(self.speed().length()) == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)

    def on_render(self):
        self.set_animation()
        self.animation.on_render(self)
        pass

    def pretty_print(self, i = 0):
        print(" "*i)
