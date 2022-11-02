from game_state import GameState
from player import Player
from engine import Engine


class Game:
    def __init__(self, players):
        self.gs = GameState(self)
        self.en = Engine(self)
        self.players = players
        self.me = 0  # TODO

    def draw(self, screen):
        self.gs.draw(screen)
        self.players[self.me].draw(screen)