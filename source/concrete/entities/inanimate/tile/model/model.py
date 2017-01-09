from source.abstract.entities.inanimate.model import model

class Model(model.Model):
    name    = "Tile"
    mined   = False

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        self.mass = 100
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def mine_ore(self):
        if self.mined == False:
            from source.concrete.entities.inanimate.rock import rock
            from source.library.science.geology.rocks import bauxite
            ore = rock.Rock(None, 100, bauxite.Bauxite())
            self.mined = True
            return ore
        else:
            return None
        return None
