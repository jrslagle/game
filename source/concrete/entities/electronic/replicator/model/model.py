from source.abstract.entities.electronic.model import model

class Model(model.Model):
    name        = "Replicator"
    logistics   = None
    
    def __init__(self, parent = None, logistics = None):
        model.Model.__init__(self, parent)
        if logistics is not None:
            self.logistics = logistics
            self.logistics.replicator = self
        self.radius = 50
        self.mass = 30
        pass

    def activate(self):
        self.build_widget()

    def build_widget(self):
        from source.concrete.entities.inanimate.rock import rock
        from source.library.science.geology.rocks import bauxite

        widget = rock.Rock(self.parent, 100, bauxite.Bauxite())
        # TODO: widget = solarPanel

        element_requirements = widget.get_element_masses()
        if self.logistics.elemental_storage_unit.check_storage(element_requirements):
            print("\033[94m"+"Building Widget"+"\033[0m")
            self.logistics.elemental_storage_unit.take_elements(element_requirements)
            widget.position.x = self.position.x
            widget.position.y = self.position.y
            if self.parent is not None:
                self.parent.add_entity(widget)
            return widget
        else:
            print("\033[91m"+"Build Failed."+"\033[0m")
            return None
        pass
