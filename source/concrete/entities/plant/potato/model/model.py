from source.abstract.entities.inanimate.model import model

class GrowthState():
    SEED    = 0
    SPROUT  = 1
    RIPE    = 2
    PICKED  = 3

class HealthState():
    HEALTHY = 0
    DAMAGED = 1

class Model(model.Model):
    name            = "Potato"
    growth_state    = GrowthState.SEED
    health_state    = HealthState.HEALTHY

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 16
        self.mass = 10
        pass
