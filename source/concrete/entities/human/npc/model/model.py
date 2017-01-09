from source.abstract.entities.human.model import model

class Model(model.Model):
    name    = "NPC"

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.mass = 62
        pass
