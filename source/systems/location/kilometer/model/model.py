from source.abstract.location.model import model

from source.systems.location.hectare import hectare

class Model(model.Model):
    position    = (0, 0)
    size        = 1
    hectares  = [[None]]

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.populate_hectares()
        pass

    def populate_hectares(self):
        self.hectares = [[hectare.Hectare(self) for x in range(self.size)] for y in range(self.size)]
        pass

    def north(self):
        pass

    def east(self):
        pass

    def south(self):
        pass

    def west(self):
        pass

    def get_hectare(self, position):
        pos = position / 10
        return self.hectares(
            int(math.floor(pos.x)),
            int(math.floor(pos.y))
        )

    def get_kilometer(self):
        return self

    def get_planet(self):
        return self.parent.get_planet()

    def get_tile(self, position):
        pos = position / 100
        tile = self.get_hectare().get_tile(
            int(math.floor(pos.x)),
            int(math.floor(pos.y))
        )
        return tile
