from source.abstract.entities.electronic.model import model


class UseState:
    OFF = 0
    ON  = 1

class Model(model.Model):
    name      = "Lightbulb"
    use_state = UseState.OFF

    grid = None

    discharge = -0.5

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        self.mass = 10
        pass

    def discharge(self):
        if self.use_state == UseState.ON:
            c = self.grid.discharge(self.discharge)
            if(c >= 0):
                self.use_state = UseState.ON
            else:
                self.use_state = UseState.OFF
