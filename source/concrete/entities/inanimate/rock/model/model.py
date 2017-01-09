from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Rock"

    def __init__(self, parent, mass = 100, material = None):
        model.Model.__init__(self, parent)
        self.radius = 16
        self.mass = mass  # in kg
        self.set_material(material)
        pass
