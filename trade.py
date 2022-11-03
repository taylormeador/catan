import pygame as p
import globals

class Trade:
    trade = None

    def __init__(self):
        self.offering_player = None
        self.accepting_player = None
        self.offer = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}  # dict of resources offered
        self.accept = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}  # dict of resources wanted
        self.declines = [] # list of players who declined trade
        self.offered = False # True when offering player offers the trade
        self.x = globals.WIDTH * .01
        self.y = globals.HEIGHT * .02
        Trade.trade = self

    def make_trade(self):
        event = self.offering_player.name + ' and ' + self.accepting_player.name + ' traded'
        # TODO push to event log

        # loop through the resources in the offer/accept dicts and distribute accordingly
        for resource, amount in self.offer:
            self.offering_player.resources[resource] -= amount
            self.accepting_player.resources[resource] += amount
        for resource, amount in self.accept:
            self.offering_player.resources[resource] += amount
            self.accepting_player.resources[resource] -= amount

    # helper for drawing offer/accept resources
    def draw_line(self, screen, x, text):
        text_surface = self.font.render(text, True, globals.BLACK)
        screen.blit(text_surface, (x + 5, self.y + 5 + self.i * 15))
        self.i += 1

    def draw_text(self, screen):
        # TODO this needs to be altered to draw different text based on if it's your turn or not
        p.font.init()
        self.font = p.font.Font(p.font.get_default_font(), 14)
        self.i = 0

        # offered resources line by line
        self.draw_line(screen, self.x, 'Offer')
        for k, v in self.offer.items():
            self.draw_line(screen, self.x, k + ': ' + str(v))

        # accepting resources in right column
        self.i = 0
        x = self.x + 80
        self.draw_line(screen, x, 'Accept')
        for k, v in self.accept.items():
            self.draw_line(screen, x, k + ': ' + str(v))

        # offer/accept buttons in right corners
        self.i = 0
        x = self.x + 160
        self.draw_line(screen, x, 'Make Offer')
        self.draw_line(screen, x, '')
        self.draw_line(screen, x, '')
        self.draw_line(screen, x, '')
        self.draw_line(screen, x, '')

    def button_clicked(self, pos):
        offer_x = self.x + 180
        offer_y = self.y + 15
        if abs(offer_x - pos[0]) < 20 and abs(offer_y - pos[1]) < 10:
            return True
        return False

    def draw_background(self, screen):
        # background

        background = p.Rect(self.x, self.y, 250, 100)
        p.draw.rect(screen, globals.ISLAND_COLOR, background)

    def draw(self, screen):
        self.draw_background(screen)
        self.draw_text(screen)

