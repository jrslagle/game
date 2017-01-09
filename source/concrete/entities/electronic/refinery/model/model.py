from source.abstract.entities.electronic.model import model

class Model(model.Model):
    name        = "Refinery"
    logistics   = None

    def __init__(self, parent = None, logistics = None):
        model.Model.__init__(self, parent)
        if logistics is not None:
            self.logistics = logistics
            self.logistics.refinery = self
        self.radius = 50
        self.mass = 50
        pass

    def activate(self):
        for collidable in self.get_collisions():
            self.refine_object(collidable)
        pass

    def refine_object(self, entity):
        element_masses = entity.get_element_masses()
        for element_name in element_masses.keys():
            self.logistics.store_element(element_name, element_masses[element_name])
        self.parent.remove_entity(entity)
        pass
