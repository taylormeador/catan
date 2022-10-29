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
        print('Rolled:', first + second)
        self.distribute_resources(first + second)

    def distribute_resources(self, rolled):
        for hex in ResourceHex.resource_hexes:
            if hex.number == rolled:
                for vertex in hex.vertices:
                    if vertex:
                        if isinstance(vertex, City):
                            vertex.owner.resources[hex.resource] += 2
                        elif isinstance(vertex, Settlement):
                            vertex.owner.resources[hex.resource] += 1

    def find_longest_road(self):
        pass

    def check_for_win(self):
        for player in self.gs.players:
            if player.victory_points >= globals.VP_WIN_AMOUNT:
                return player
        return False

