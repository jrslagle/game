from source.abstract.entities.electronic.model import model


class CapacityState:
    PERCENT_000 = 0
    PERCENT_020 = 1
    PERCENT_040 = 2
    PERCENT_060 = 3
    PERCENT_080 = 4
    PERCENT_100 = 5

class Model(model.Model):
    name            = "Elemental Storage Tank"
    element         = None
    empty_mass      = 10
    stored          = 0 # in kg
    capacity        = 0 # in kg
    capacity_state  = CapacityState.PERCENT_000

    def __init__(self, parent, element, capacity = 1000):
        model.Model.__init__(self, parent)
        self.element = element
        self.capacity = capacity
        self.radius = 16
        self.empty_mass = self.capacity*0.02
        self.mass = self.empty_mass
        pass

    def add_element(self, kg):
        # spherical_cow: storage should be of chemicals rather than elements.
        overage = (self.stored + kg) - self.capacity
        if self.stored == self.capacity:
            # Oxygen tank is full. 1.3 kg of oxygen has been lost.
            print("\033[91m"+self.element.name+" tank is full. "+str(overage)+" kg of "+self.element.name+" has been lost.\033[0m")
        elif self.capacity - self.stored < kg:
            # Oxygen tank is full. 0.7 kg of oxygen has been lost.
            print("\033[91m"+self.element.name+" tank is full. "+str(overage)+" kg of "+self.element.name+" has been lost.\033[0m")
            self.stored = self.capacity
        else:
            # 0.7 kg of oxygen has been stored.
            print("\033[92m"+str(kg)+" kg of "+self.element.name+" has been stored.\033[0m")
            self.stored += kg
        self.mass = self.stored + self.empty_mass
        pass

    def remove_kg(self, kg):
        self.stored -= kg

    def get_stored_percent(self):
        return float(self.stored) / float(self.capacity)
