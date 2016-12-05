import pygame

from source.action import action
from source.abstract.animate_entity import animate_entity_view

from animation_config import run
from animation_config import stand
from animation_config import walk

class AvatarView(animate_entity_view.AnimateEntityView):
    def __init__(self):
        animate_entity_view.AnimateEntityView.__init__(self)

        self.height = 74
        self.width = 32
        pass

    def on_render(self, camera):
        if self.velocity() == 0:
            if self.animation == None or self.animation.action != "stand":
                self.animation = action.Action(stand.stand_data)
            self.animation.on_render(camera, self.direction, camera.center)
        elif self.velocity() <= self.velocity_base:
            if self.animation == None or self.animation.action != "walk":
                self.animation = action.Action(walk.walk_data)
            self.animation.on_render(camera, self.direction, camera.center)
        elif self.velocity() <= self.max_velocity:
            if self.animation == None or self.animation.action != "run":
                self.animation = action.Action(run.run_data)
            self.animation.on_render(camera, self.direction, camera.center)
        else:
            print("Entity.on_render() invalid option.")
        pass
