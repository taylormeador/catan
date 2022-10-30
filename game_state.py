from board import Board
from engine import Engine
from player import Player
import random

# handles aspects of game related to state, turns, events, etc
class GameState:
    def __init__(self, players):
        self.b = Board()
        self.players = [player for player in players]  # in order of turn taking
        self.turns = 0
        self.turn = self.get_current_player_turn()
        self.en = Engine(self)

    def get_current_player_turn(self):
        return self.players[self.turns % len(self.players)]


