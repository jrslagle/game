from source.abstract.location.model import model

from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator

class Model(model.Model):
    name = "Logistics"
    refinery                = None
    replicator              = None
    elemental_storage_tanks = dict()

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        pass

    def add_tank(self, tank):
        self.elemental_storage_tanks[tank.element.name] = tank

    def store_element(self, element_name, kg):
        self.elemental_storage_tanks[element_name].add_element(kg)
        pass

    def check_storage(self, element_masses):
        have_enough = True
        print("\033[92m"+"Checking Storage To See If There Are Enough Elements To Build."+"\033[0m")

        for element_name in element_masses.keys():
            if self.elemental_storage_tanks[element_name].stored < element_masses[element_name]:
                short_by = element_masses[element_name] - self.elemental_storage_tanks[element_name].stored
                print("\033[91m"+"You need "+str(short_by)+" kg more "+element_name+" to build that."+"\033[0m")
                have_enough = False
        return have_enough

    def take_elements(self, element_masses):
        for element_name in element_masses:
            self.elemental_storage_tanks[element_name].remove_kg(element_masses[element_name])
