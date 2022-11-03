import random
from buildings import City, Settlement, Road
from hex import ResourceHex
import globals
from trade import Trade

# handles rule enforcement and calculation of game processes
class Engine:
    def __init__(self, game):
        self.game = game
        self.event_log = game.gs.event_log
        self.trade = Trade()

    def roll_dice(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        event = self.game.gs.get_turn().name + ' rolled ' + str(first + second)
        self.event_log.push(event)
        if first + second == 7:
            self.robber()
            self.game.gs.robber()
        else:
            self.distribute_resources(first + second)
        self.game.gs.dice_rolled()

    def distribute_resources(self, rolled):
        # loop through all resource hexes and give resources to building owners
        for hex in ResourceHex.resource_hexes:
            if hex.number == rolled:
                for vertex in hex.vertices:
                    if vertex:
                        if vertex.occupied:
                            if isinstance(vertex.building, City):
                                event = vertex.building.owner.name + ' gets 2 ' + hex.resource
                                self.event_log.push(event)
                                vertex.building.owner.resources[hex.resource] += 2
                            elif isinstance(vertex.building, Settlement):
                                event = vertex.building.owner.name + ' gets 1 ' + hex.resource
                                self.event_log.push(event)
                                vertex.building.owner.resources[hex.resource] += 1

    def find_longest_road(self):
        pass

    def check_for_win(self):
        for player in self.game.players:
            player.set_victory_points()
            if player.victory_points >= globals.VP_WIN_AMOUNT:
                return player
        return False

    def robber(self):
        for player in self.game.players:
            if sum(player.resources.values()) > 7:
                event = player.name + ' got robbed. Discard half your resources'
                self.event_log.push(event)
                player.robber()

