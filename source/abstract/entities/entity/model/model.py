import math
import pygame
from source.abstract.base_object.model import model
from source.library.science.math.geometry.g3d.sphere import sphere

class MoveState():
    STAND = 0

class Model(model.Model, sphere.Sphere):
    name            = "Entity"
    direction       = 0
    move_state      = MoveState.STAND
    velocity        = None
    free_fall       = False
    mass            = 0 # in kg
    material        = None
    element_masses  = None
    collisions      = []

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        sphere.Sphere.__init__(self)
        self.collisions = []
        self.radius = 1
        self.position = pygame.math.Vector3(0, 0, 0)
        self.velocity = pygame.math.Vector3(0, 0, 0)
        pass

    def translate(self):
        sphere.Sphere.translate(self)
        self.position += self.new_velocity()
        if self.free_fall: self.update_free_fall()
        pass

    def new_velocity(self):
        if self.free_fall: self.apply_gravity()
        return self.velocity

    def get_velocity(self):
        return self.velocity

    def apply_gravity(self):
        self.velocity.z -= self.get_planet().get_gravity()

    def update_free_fall(self):
        tile = self.get_tile()

        above_floor = self.position.z > self.get_tile().position.z
        # held = is held
        self.free_fall = above_floor # or held

        below_floor = self.position.z <= tile.position.z
        if below_floor:
            self.position.z = tile.position.z
            self.velocity.z = tile.velocity.z
            self.free_fall = False

        # TODO: add code for interrupting free fall and resetting object velocities when colliding with an object

    def stand(self):
        self.move_state = MoveState.STAND
        pass

    def drop(self):
        self.position = pygame.math.Vector3(
            self.position.x,
            self.position.y,
            self.position.z
        )
        self.update_free_fall()
        pass

    def get_collisions(self):
        for entity in self.parent.entities:
            if entity is not self:
                if self.collide(entity) == True:
                    self.__add_collisions(entity)
                else:
                    self.__remove_collisions(entity)
        self.__clean_collisions()
        return self.collisions

    def __add_collisions(self, entity):
        if entity not in self.collisions:
            self.collisions.append(entity)
            entity.on_collide(entity)
        pass

    def __remove_collisions(self, entity):
        if entity in self.collisions:
            self.collisions.remove(entity)
        pass

    def __clean_collisions(self):
        for entity in self.collisions:
            if entity not in self.parent.entities:
                self.collisions.remove(entity)
        pass

    def get_planet(self):
        return self.parent.get_planet()

    def get_kilometer(self):
        kilo = self.get_planet().kilometers[0][0]
        x = int(math.floor(self.position.x / 10000))
        y = int(math.floor(self.position.y / 10000))
        return kilo

    def get_hectare(self):
        hect = self.get_kilometer().hectares[0][0]
        x = int(math.floor(self.position.x / 1000))
        y = int(math.floor(self.position.y / 1000))
        return hect

    def get_tile(self):
        x = int(math.floor(self.position.x / 100))
        y = int(math.floor(self.position.y / 100))
        tile = self.get_hectare().get_tile(x, y)
        return tile

    def get_mass(self):
        return self.mass

    def set_mass(self, mass):
        self.mass = mass
        pass

    def get_material(self):
        return self.material

    def set_material(self, material):
        self.material = material
        pass

    def get_element_masses(self):
        if self.element_masses == None:
            element_masses = dict()
            for component in self.material.composition:
                portion = component[0]
                chemical = component[1]
                kmoles = portion * self.mass / chemical.molar_mass

                for element in chemical.elements:
                    element_kg = kmoles * element.mass
                    if element_masses.has_key(element.name):
                        element_masses[element.name] += element_kg
                    else:
                        element_masses[element.name] = element_kg
            self.element_masses = element_masses
        return self.element_masses
