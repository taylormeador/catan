from board import Board
from event import EventLog
from player import Player

# handles aspects of game related to state, turns, events, etc
class GameState:
    def __init__(self, game):
        self.game = game
        self.b = Board()
        self.event_log = EventLog()
        self.turns = -1
        self.phase = 'roll'

    def draw(self, screen):
        self.b.draw(screen)
        self.event_log.draw(screen)

    def get_turn(self):
        return self.game.players[self.turns % len(self.game.players)]

    def change_turns(self):
        self.turns += 1
        self.phase = 'roll'
        Player.current_player = self.get_turn()
        self.event_log.push(self.get_turn().name + '\'s turn. Roll the dice!')

    # keep track of when player needs to roll, build, etc
    def get_turn_phase(self):
        return self.phase

    def dice_rolled(self):
        self.phase = 'build'

    def robber(self):
        event = self.get_turn().name + ' is placing the robber'
