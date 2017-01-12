from source.library.action import action
from source.abstract.entities.entity.view import view

from animation_config import run
from animation_config import walk

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 32
        self.dimensions.y = 32
        pass

    def set_animation(self):
        view.View.set_animation(self)
        s= abs(self.get_velocity().length())
        if s > 0 and s <= 4:
            if self.animation == None or self.animation.action != "walk":
                self.animation = action.Action(walk.data)
        elif s > 4:
            if self.animation == None or self.animation.action != "run":
                self.animation = action.Action(run.data)
        pass
