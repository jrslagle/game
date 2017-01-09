from source.abstract.location.model import model
from source.global_variables import camera
from source.systems.location.kilometer import kilometer
from source.systems.location.homestead import homestead
from source.concrete.entities.human.avatar import avatar

class Model(model.Model):
    position        = (0, 0)
    avatar          = None
    camera          = None
    homestead       = None
    gravity         = 1
    #instructions    = None

    size            = 1
    kilometers    = [[None]]

    def __init__(self, parent = None, gravity = 1):
        model.Model.__init__(self, parent)
        self.populate_kilometers()

        self.homestead = homestead.Homestead()

        self.avatar = avatar.Avatar(self)
        #self.avatar.position.x = 300
        #self.avatar.position.y = 300

        #self.instructions = instructions.Instructions(window)
        self.camera = camera.CAMERA
        self.camera.set_target(self.avatar)
        self.gravity = 3.711  # Mar's gravity in m/s^2
        pass

    def populate_kilometers(self):
        self.kilometers = [[kilometer.Kilometer(self) for x in range(self.size)] for y in range(self.size)]
        pass
