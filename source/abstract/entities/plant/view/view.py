from source.abstract.entities.inanimate.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 32
        self.dimensions.y = 32

        self.height = 32
        self.width = 32
        pass
