from source.library.action import action

from source.abstract.entities.electronic.view import view

from animation_config import stand

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 100
        self.dimensions.y = 100
        self.animation = action.Action(stand.data)
        pass

    def get_render_offset(self):
        self.render_offset = -(self.dimensions / 2)
        return self.render_offset

