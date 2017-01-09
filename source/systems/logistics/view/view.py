from source.abstract.location.view import view

class View(view.View):
    def __init__(self):
        view.View.__init__(self)
        pass
    
    def pretty_print(self, i=0):
        print(("\t"*i)+self.name)
        for tank in self.elemental_storage_tanks:
            self.elemental_storage_tanks[tank].pretty_print(i+1)
        pass
