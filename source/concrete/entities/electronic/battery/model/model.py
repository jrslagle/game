from source.abstract.entities.electronic.model import model


class ChargeState:
    PERCENT_000 = 0
    PERCENT_020 = 1
    PERCENT_040 = 2
    PERCENT_060 = 3
    PERCENT_080 = 4
    PERCENT_100 = 5

class Model(model.Model):
    name = "Battery"
    charge = 0
    charge_state = ChargeState.PERCENT_000

    grid = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 16
        self.mass = 30
        pass
