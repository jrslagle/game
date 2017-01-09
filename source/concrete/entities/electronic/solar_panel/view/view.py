from source.abstract.entities.electronic.view import view
from source.library.action import action

from animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 100
        self.dimensions.y = 64
        self.animation = action.Action(stand.data)
        pass

    def on_render(self):
        self.animation.on_render(self)
        pass
