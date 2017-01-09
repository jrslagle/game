from source.abstract.entities.electronic.controller import controller


class Controller(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)
        pass

    def on_loop(self):
        self.discharge()
        pass
