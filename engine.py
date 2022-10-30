import random
from buildings import City, Settlement, Road
from hex import ResourceHex

# handles rule enforcement and calculation of game processes
class Engine:
    def __init__(self, gs):
        self.gs = gs

    def roll_dice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        print('> Rolled:', first + second)
        self.distribute_resources(first + second)

    def distribute_resources(self, rolled):
        # loop through all resource hexes and give resources to building owners
        for hex in ResourceHex.resource_hexes:
            if hex.number == rolled:
                print('> found hex with rolled number:', hex, hex.vertices)
                for vertex in hex.vertices:
                    if vertex:
                        if vertex.occupied:
                            if isinstance(vertex.building, City):
                                print('> ' + vertex.building.owner.name + ' gets 2 ' + hex.resource)
                                vertex.building.owner.resources[hex.resource] += 2
                            elif isinstance(vertex.building, Settlement):
                                print('> ' + vertex.building.owner.name + ' gets 1 ' + hex.resource)
                                vertex.building.owner.resources[hex.resource] += 1

    def find_longest_road(self):
        pass

    def check_for_win(self):
        for player in self.gs.players:
            if player.victory_points >= globals.VP_WIN_AMOUNT:
                return player
        return False

