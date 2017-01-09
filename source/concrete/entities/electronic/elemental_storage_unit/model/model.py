from source.abstract.entities.electronic.model import model
from source.concrete.entities.electronic.elemental_storage_tank.elemental_storage_tank import ElementalStorageTank
from source.library.science.chemistry.element import elements

class Model(model.Model):
    name        = "Elemental Storage Unit"
    tanks       = dict()
    logistics   = None
    inherent_mass = 30

    def __init__(self, parent = None, logistics = None):
        model.Model.__init__(self, parent)
        if logistics is not None:
            self.logistics = logistics
            self.logistics.elemental_storage_unit = self

        self.radius = 50
        self.add_tank(elements.Aluminum)
        self.add_tank(elements.Carbon)
        self.add_tank(elements.Hydrogen)
        self.add_tank(elements.Iron)
        self.add_tank(elements.Oxygen)
        self.add_tank(elements.Silicon)
        self.add_tank(elements.Calcium)
        self.add_tank(elements.Titanium)
        self.update_mass()
        pass

    def add_tank(self,element):
        self.tanks[element.name] = ElementalStorageTank(self, element, 100)

    def update_mass(self):
        mass = self.inherent_mass
        for tank in self.tanks:
            mass += tank.mass
        self.mass = mass

    def store_element(self, element_name, kg):
        self.tanks[element_name].add_element(kg)
        self.update_mass()
        pass

    def check_storage(self, element_masses):
        have_enough = True
        print("\033[92m"+"Checking Storage To See If There Are Enough Elements To Build."+"\033[0m")

        for element_name in element_masses.keys():
            if self.tanks[element_name].stored < element_masses[element_name]:
                short_by = element_masses[element_name] - self.tanks[element_name].stored
                print("\033[91m"+"You need "+str(short_by)+" kg more "+element_name+" to build that."+"\033[0m")
                have_enough = False
        return have_enough

    def take_elements(self, element_masses):
        for element_name in element_masses:
            self.tanks[element_name].remove_kg(element_masses[element_name])
        self.update_mass()
