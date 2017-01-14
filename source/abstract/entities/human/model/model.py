from source.abstract.entities.animate.model import model

class Model(model.Model):
    name    = "HumanEntity"
    holding = None
    reach   = 0
    
    def __init__(self, parent = None):
        model.Model.__init__(self, parent)
        self.radius = 50
        self.reach = self.radius
        pass
    
    def translate(self):
        model.Model.translate(self)
        if self.holding != None:
            self.holding.position.x = self.position.x
            self.holding.position.y = self.position.y
            self.holding.position.z = self.position.z

    def get_nearest_item(self):
        shortest_distance = None
        item = None
        for entity in self.parent.homestead.entities:
            distance = self.position.distance_to(entity.position)
            if distance < shortest_distance or shortest_distance == None:
                shortest_distance = distance
                item = entity
        return item

    def get_nearest_reachable_item(self):
        item = self.get_nearest_item() # could return None if there are no entities in homestead
        if item != None:
            distance = self.position.distance_to(item.position)
            if distance < self.reach:
                return item
            else:
                return None
        else:
            return None

    def activate(self):
        for collidable in self.get_collisions():
            collidable.on_activate()
        pass

    def drop_item(self):
        if self.holding != None:
            self.holding.on_drop()
            self.holding = None
        pass

    def pickup(self, item = None):
        if item != None:
            self.holding = item
            self.holding.on_pickup()
            return True
        else: # item = None
            if self.holding == None:
                self.holding = self.get_nearest_reachable_item()
                if self.holding != None:
                    self.holding.on_pickup()
                    return True
                else:
                    return False
            else:
                self.drop_item()
                return False
        return False

    def mine(self):
        # TODO: .get_tile() in Entity model doesn't work.
        # ore = self.get_tile().mine_ore()

        from source.concrete.entities.inanimate.tile import tile
        ore = tile.Tile().mine_ore()

        if ore != None:
            ore.parent = self.parent.homestead
            ore.position = self.position
            self.parent.homestead.add_entity(ore)
            self.pickup(ore)
        pass
