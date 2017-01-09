from source.abstract.entities.plant.view import view
from source.library.action import action

from source.abstract.entities.plant.model.model import HealthState, GrowthState

from animation_config import healthy_seed, healthy_sprout, healthy_sapling, healthy_mature, healthy_ripe
from animation_config import damaged_seed, damaged_sprout, damaged_sapling, damaged_mature, damaged_ripe

class View(view.View):
    healthy_seed       = healthy_seed
    healthy_sprout     = healthy_sprout
    healthy_sapling    = healthy_sapling
    healthy_mature     = healthy_mature
    healthy_ripe       = healthy_ripe
    damaged_seed       = damaged_seed
    damaged_sprout     = damaged_sprout
    damaged_sapling    = damaged_sapling
    damaged_mature     = damaged_mature
    damaged_ripe       = damaged_ripe

    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(healthy_seed.data)
        pass
