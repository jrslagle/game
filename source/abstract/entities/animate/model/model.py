import pygame

from source.abstract.entities.entity.model import model
from source.global_variables import global_variables

class MoveState():
    STAND   = 0
    WALK    = 1
    RUN     = 2

class Model(model.Model):
    name        = "AnimateEntity"
    walk_speed  = 4
    run_speed   = 4
    velocity    = None

    vision      = 800
    resolution  = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.resolution = pygame.math.Vector3(self.vision, self.vision, 0)
        self.velocity   = pygame.math.Vector3()
        pass
    
    def rotate(self):
        model.Model.rotate(self)
        if self.velocity.y < 0:
            self.direction = global_variables.NORTH
        if self.velocity.x > 0:
            self.direction = global_variables.EAST
        if self.velocity.y > 0:
            self.direction = global_variables.SOUTH
        if self.velocity.x < 0:
            self.direction = global_variables.WEST
        pass
    
    def new_velocity(self):
        model.Model.new_velocity(self)
        run_modifier = 0
        if(self.move_state == MoveState.RUN):
            run_modifier = self.run_speed
        modifier = self.walk_speed + run_modifier
        v = self.velocity * modifier
        return v

    def move_x(self, value):
        self.velocity.x = value
        pass

    def move_y(self, value):
        self.velocity.y = value
        pass
    
    def run(self):
        self.move_state = MoveState.RUN
        pass

    def walk(self):
        self.move_state = MoveState.WALK
        pass
