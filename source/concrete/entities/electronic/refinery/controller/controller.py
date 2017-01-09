from source.abstract.entities.electronic.controller import controller


class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_refine(self, mineral):
        self.refine_mineral(mineral)
        pass

    def on_activate(self):
        self.activate()
        pass
