from source.library.action import action
from source.abstract.entities.entity.view import view

from animation_config import run
from animation_config import walk

class View(view.View):
    height = 32
    width = 32

    def __init__(self):
        view.View.__init__(self)
        pass

    def set_animation(self):
        view.View.set_animation(self)
        s= abs(self.speed().length())
        if s > 0 and s <= 4:
            if self.animation == None or self.animation.action != "walk":
                self.animation = action.Action(walk.walk_data)
        elif s > 4:
            if self.animation == None or self.animation.action != "run":
                self.animation = action.Action(run.run_data)
        pass
