from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Refinery"

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        pass

    def activate(self):
        pos_0x = self.position.x - (self.width / 2)
        pos_0y = self.position.y - (self.height / 2)
        pos_1x = self.position.x + (self.width / 2)
        pos_1y = self.position.y + (self.height / 2)

        print pos_0x
        print pos_0y
        print pos_1x
        print pos_1y

        for entity in self.parent.parent.entities:
            if entity.position.x >= self.position.x - (self.width / 2):
                if entity.position.y >= self.position.y - (self.height / 2):
                    if entity.position.x <= self.position.x + (self.width / 2):
                        if entity.position.y <= self.position.y + (self.height / 2):
                            self.refine_object(entity)
        pass

    def refine_object(self, entity):
        element_masses = entity.get_element_masses()
        for element_name in element_masses.keys():
            self.parent.elemental_storage_unit.store_element(element_name, element_masses[element_name])
        self.parent.parent.remove_entity(entity)
        pass
