from source.abstract.entities.electronic.model import model
from datetime import datetime

class Model(model.Model):
    name        = "Solar Panel"
    charge      = 0
    charge_time = 0

    grid = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.charge_time = datetime.now()
        self.radius = 50
        self.mass = 30
        pass

    def delta_charge(self):
        self.charge += (datetime.now() - self.charge_time).total_seconds() / 100
        pass
