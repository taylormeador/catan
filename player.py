import globals
import pygame as p

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.resources = {'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
        self.dev_cards = {'knight': 0, 'road building': 0, 'year of plenty': 0, 'monopoly': 0, 'victory point': 0}
        self.settlements = []
        self.cities = []
        self.roads = []
        self.longest_road = 0
        self.victory_points = 0

    # helper for drawing stash
    def draw_line(self, screen, text):
        text_surface = self.font.render(text, True, globals.BLACK)
        screen.blit(text_surface, (self.x + 5, self.y + 5 + self.i * 15))
        self.i += 1

    # draw stash
    def draw(self, screen):
        # background
        self.x = globals.WIDTH * .02
        self.y = globals.HEIGHT * .54
        background = p.Rect(self.x, self.y, 160, 350)
        p.draw.rect(screen, globals.ISLAND_COLOR, background)

        # resources, dev cards, victory_points
        p.font.init()
        self.font = font = p.font.Font(p.font.get_default_font(), 14)
        self.i = 0

        # line by line
        self.draw_line(screen, 'Resources')
        for k, v in self.resources.items():
            self.draw_line(screen, k + ': ' + str(v))
        self.draw_line(screen, '')
        self.draw_line(screen, 'Dev Cards')
        for k, v in self.dev_cards.items():
            self.draw_line(screen, k + ': ' + str(v))
        self.draw_line(screen, '')
        self.draw_line(screen, 'Buildings Remaining')
        self.draw_line(screen, 'roads: ' + str(15 - len(self.roads)))
        self.draw_line(screen, 'settlements: ' + str(5 - len(self.settlements)))
        self.draw_line(screen, 'cities: ' + str(4 - len(self.cities)))
        self.draw_line(screen, '')
        self.draw_line(screen, 'Standing')
        self.draw_line(screen, 'longest road: ' + str(self.longest_road))
        self.draw_line(screen, 'army: ' + str(self.dev_cards['knight']))
        self.draw_line(screen, 'victory points: ' + str(self.victory_points))
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return "<Player '" + self.name + "'>"
