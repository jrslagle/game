from source.abstract.location.model import model

from source.library.science.geology.rocks import ice

from source.systems.power_grid import power_grid
from source.concrete.entities.plant.corn import corn
from source.concrete.entities.plant.turnip import turnip
from source.concrete.entities.plant.tomato import tomato
from source.concrete.entities.plant.potato import potato
from source.concrete.entities.electronic.solar_panel import solar_panel
from source.concrete.entities.electronic.battery import battery
from source.concrete.entities.electronic.lightbulb import lightbulb
from source.concrete.entities.inanimate.rock import rock
from source.systems.logistics import logistics
from source.concrete.entities.electronic.elemental_storage_tank import elemental_storage_tank
from source.concrete.entities.electronic.refinery import refinery
from source.concrete.entities.electronic.replicator import replicator
from source.library.science.chemistry.element import elements

class Model(model.Model):
    power_grid      = None
    logistics       = None

    def __init__(self, parent = None):
        model.Model.__init__(self, parent)

        self.add_logistics()
        self.add_power_grid()
        self.add_crops()
        self.add_npc()
        self.add_rock()
        pass

    def add_crops(self):
        corn0 = corn.Corn(self)
        corn0.position.x = 150
        corn0.position.y = 250
        self.add_entity(corn0)

        turnip0 = turnip.Turnip(self)
        turnip0.position.x = 350
        turnip0.position.y = 250
        self.add_entity(turnip0)
        
        tomato0 = tomato.Tomato(self)
        tomato0.position.x = 250
        tomato0.position.y = 250
        self.add_entity(tomato0)

        potato0 = potato.Potato(self)
        potato0.position.x = 450
        potato0.position.y = 250
        self.add_entity(potato0)
        pass

    def add_logistics(self):
        self.logistics = logistics.Logistics(self)
        refinery0 = refinery.Refinery(self, self.logistics)
        refinery0.position.x = 50
        refinery0.position.y = 350
        self.add_entity(refinery0)
        
        replicator0 = replicator.Replicator(self, self.logistics)
        replicator0.position.x = 250
        replicator0.position.y = 350
        self.add_entity(replicator0)

        aluminum_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Aluminum, 100)
        aluminum_tank.position.x = 50
        aluminum_tank.position.y = 450
        self.logistics.add_tank(aluminum_tank)
        self.add_entity(aluminum_tank)
        
        carbon_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Carbon, 100)
        carbon_tank.position.x = 100
        carbon_tank.position.y = 450
        self.logistics.add_tank(carbon_tank)
        self.add_entity(carbon_tank)
        
        hydrogen_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Hydrogen, 100)
        hydrogen_tank.position.x = 150
        hydrogen_tank.position.y = 450
        self.logistics.add_tank(hydrogen_tank)
        self.add_entity(hydrogen_tank)
        
        iron_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Iron, 100)
        iron_tank.position.x = 200
        iron_tank.position.y = 450
        self.logistics.add_tank(iron_tank)
        self.add_entity(iron_tank)
        
        oxygen_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Oxygen, 100)
        oxygen_tank.position.x = 250
        oxygen_tank.position.y = 450
        self.logistics.add_tank(oxygen_tank)
        self.add_entity(oxygen_tank)
        
        silicon_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Silicon, 100)
        silicon_tank.position.x = 300
        silicon_tank.position.y = 450
        self.logistics.add_tank(silicon_tank)
        self.add_entity(silicon_tank)
        
        calcium_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Calcium, 100)
        calcium_tank.position.x = 350
        calcium_tank.position.y = 450
        self.logistics.add_tank(calcium_tank)
        self.add_entity(calcium_tank)
        
        titanium_tank = elemental_storage_tank.ElementalStorageTank(self, elements.Titanium, 100)
        titanium_tank.position.x = 400
        titanium_tank.position.y = 450
        self.logistics.add_tank(titanium_tank)
        self.add_entity(titanium_tank)

    def add_npc(self):
        #self.npc = npc.NPC(self)
        #self.npc.position.x = 50
        #self.npc.position.y = 250
        #self.add_entity(self.npc)
        pass

    def add_power_grid(self):
        self.power_grid = power_grid.PowerGrid()

        solar_panel_0 = solar_panel.SolarPanel(self)
        solar_panel_0.position.x = 50
        solar_panel_0.position.y = 50
        self.power_grid.attach_source(solar_panel_0)
        self.add_entity(solar_panel_0)

        solar_panel_1 = solar_panel.SolarPanel(self)
        solar_panel_1.position.x = 50
        solar_panel_1.position.y = 150
        self.power_grid.attach_source(solar_panel_1)
        self.add_entity(solar_panel_1)

        self.battery0 = battery.Battery(self)
        self.battery0.position.x = 150
        self.battery0.position.y = 50
        self.battery0.charge = 21
        self.power_grid.attach_store(self.battery0)
        self.add_entity(self.battery0)

        lightbulb0 = lightbulb.LightBulb(self)
        lightbulb0.position.x = 250
        lightbulb0.position.y = 50
        self.power_grid.attach_drain(lightbulb0)
        self.add_entity(lightbulb0)
        pass

    def add_rock(self):
        rock0 = rock.Rock(self, 100, ice.Ice())
        rock0.position.x = 50
        rock0.position.y = 250
        self.add_entity(rock0)
        pass

    def get_planet(self):
        print self.parent
        return self.parent.get_planet()
