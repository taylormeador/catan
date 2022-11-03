from game_state import GameState
from player import Player
from engine import Engine


class Game:
    def __init__(self, players):
        self.gs = GameState(self)
        self.en = Engine(self)
        self.players = players
        for player in players:
            player.game = self
        Player.current_player = players[0]

    def draw(self, screen):
        self.gs.draw(screen)
        self.gs.get_turn().draw(screen)  # TODO
        if self.gs.phase != 'roll':
            self.en.trade.draw(screen)