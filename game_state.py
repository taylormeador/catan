from board import Board
from event import EventLog

# handles aspects of game related to state, turns, events, etc
class GameState:
    def __init__(self, game):
        self.game = game
        self.b = Board()
        self.event_log = EventLog()
        self.turns = 0

    def draw(self, screen):
        self.b.draw(screen)
        self.event_log.draw(screen)

    def get_turn(self):
        return self.game.players[self.turns % len(self.players)]

    # keep track of when player needs to roll, build, etc
    def get_turn_phase(self):
        pass


