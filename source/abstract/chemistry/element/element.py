class Element:
    number          = None
    name            = None
    symbol          = None
    mass            = None

    abundance = {
        "universe"     : 0,
        "sun"          : 0,
        "meteorite"    : 0,
        "crust"        : 0,
        "ocean"        : 0,
        "human"        : 0
    }

    def __init__(self):
        pass

    def pretty_print(self, i=0):
        print(("\t"*i) + self.name)