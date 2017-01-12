from pygame import math

class Model:
    parent      = None
    postition   = None
    entities    = []

    def __init__(self, parent = None):
        self.parent = parent
        self.position = math.Vector3(0, 0, 0)
        pass

    def add_entity(self, object):
        object.parent = self
        self.entities.append(object)

    def remove_entity(self, object):
        object.parent = None
        self.entities.remove(object)
