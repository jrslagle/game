from source.abstract.entities.inanimate.model import model

from datetime import datetime, timedelta

class Model(model.Model):
    charge = 0
    charge_time = 0

    grid = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.charge_time = datetime.now()
        pass

    def delta_charge(self):
        self.charge += (datetime.now() - self.charge_time).total_seconds() / 100