from source.abstract.entities.plant.model import model

class Model(model.Model):
    name            = "Corn"

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 16
        pass
