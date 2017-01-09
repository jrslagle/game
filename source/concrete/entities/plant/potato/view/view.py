from source.abstract.entities.plant.view import view
from source.library.action import action

from source.abstract.entities.plant.model.model import HealthState, GrowthState

from animation_config import healthy_seed, healthy_sprout, healthy_ripe
from animation_config import damaged_seed, damaged_sprout, damaged_ripe

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        self.animation = action.Action(healthy_seed.data)
        pass

    def on_render(self):
        if self.health_state == HealthState.HEALTHY:
            if self.created_delta() <= 10:
                if self.growth_state != GrowthState.SEED:
                    self.growth_state = GrowthState.SEED
                    self.animation = action.Action(healthy_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != GrowthState.SPROUT:
                    self.growth_state = GrowthState.SPROUT
                    self.animation = action.Action(healthy_sprout.data)
            elif self.created_delta() > 20:
                if self.growth_state != GrowthState.RIPE:
                    self.growth_state = GrowthState.RIPE
                    self.animation = action.Action(healthy_ripe.data)
        
        if self.health_state == HealthState.DAMAGED:
            if self.created_delta() <= 10:
                if self.growth_state != GrowthState.SEED:
                    self.growth_state = GrowthState.SEED
                    self.animation = action.Action(damaged_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != GrowthState.SPROUT:
                    self.growth_state = GrowthState.SPROUT
                    self.animation = action.Action(damaged_sprout.data)
            elif self.created_delta() > 20:
                if self.growth_state != GrowthState.RIPE:
                    self.growth_state = GrowthState.RIPE
                    self.animation = action.Action(damaged_ripe.data)
        
        self.animation.on_render(self)
        pass

