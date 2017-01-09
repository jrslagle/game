from source.abstract.entities.inanimate.view import view
from source.library.action import action

from ..model import model

class View(view.View):
    healthy_seed       = None
    healthy_sprout     = None
    healthy_sapling    = None
    healthy_mature     = None
    healthy_ripe       = None
    damaged_seed       = None
    damaged_sprout     = None
    damaged_sapling    = None
    damaged_mature     = None
    damaged_ripe       = None

    def __init__(self):
        view.View.__init__(self)
        self.dimensions.x = 32
        self.dimensions.y = 32

        self.height = 32
        self.width = 32
        pass

    def on_render(self):
        if self.health_state == model.HealthState.HEALTHY:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    if self.healthy_seed is not None:
                        self.growth_state = model.GrowthState.SEED
                        self.animation = action.Action(self.healthy_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    if self.healthy_sprout is not None:
                        self.growth_state = model.GrowthState.SPROUT
                        self.animation = action.Action(self.healthy_sprout.data)
            elif self.created_delta() <= 30:
                if self.growth_state != model.GrowthState.SAPLING:
                    if self.healthy_sapling is not None:
                        self.growth_state = model.GrowthState.SAPLING
                        self.animation = action.Action(self.healthy_sapling.data)
            elif self.created_delta() <= 40:
                if self.growth_state != model.GrowthState.MATURE:
                    if self.healthy_mature is not None:
                        self.growth_state = model.GrowthState.MATURE
                        self.animation = action.Action(self.healthy_mature.data)
            elif self.created_delta() > 40:
                if self.growth_state != model.GrowthState.RIPE:
                    if self.healthy_ripe is not None:
                        self.growth_state = model.GrowthState.RIPE
                        self.animation = action.Action(self.healthy_ripe.data)
        
        if self.health_state == model.HealthState.DAMAGED:
            if self.created_delta() <= 10:
                if self.growth_state != model.GrowthState.SEED:
                    if self.damaged_seed is not None:
                        self.growth_state = model.GrowthState.SEED
                        self.animation = action.Action(self.damaged_seed.data)
            elif self.created_delta() <= 20:
                if self.growth_state != model.GrowthState.SPROUT:
                    if self.damaged_sprout is not None:
                        self.growth_state = model.GrowthState.SPROUT
                        self.animation = action.Action(self.damaged_sprout.data)
            elif self.created_delta() <= 30:
                if self.growth_state != model.GrowthState.SAPLING:
                    if self.damaged_sapling is not None:
                        self.growth_state = model.GrowthState.SAPLING
                        self.animation = action.Action(self.damaged_sapling.data)
            elif self.created_delta() <= 40:
                if self.growth_state != model.GrowthState.MATURE:
                    if self.damaged_mature is not None:
                        self.growth_state = model.GrowthState.MATURE
                        self.animation = action.Action(self.damaged_mature.data)
            elif self.created_delta() > 40:
                if self.growth_state != model.GrowthState.RIPE:
                    if self.damaged_ripe is not None:
                        self.growth_state = model.GrowthState.RIPE
                        self.animation = action.Action(self.damaged_ripe.data)
        
        self.animation.on_render(self)
        pass
