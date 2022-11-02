import pygame as p
import globals

# aim is to keep track of events that affect the game
# for now, it will basically be a list of strings which are descriptions of what happened
# e.g. "Taylor rolled a 4", "JB's turn", "Manasi placed the robber on (3, 4)"
# but it could expand to something more formal
class EventLog:
    def __init__(self):
        self.events = []
        self.width, self.height = globals.WIDTH * .25, globals.HEIGHT * .5
        self.x, self.y = globals.WIDTH * .72, globals.HEIGHT * .05

    def push(self, event):
        assert isinstance(event, str)
        print(event)
        self.events.insert(0, event)
        if len(self.events) > 26:
            self.events = self.events[:26]

    def draw(self, screen):
        # background
        background = p.Rect(self.x, self.y, self.width, self.height)
        p.draw.rect(screen, globals.ISLAND_COLOR, background)

        # event text
        for i in range(len(self.events)):
            p.font.init()
            font = p.font.Font(p.font.get_default_font(), 14)
            text_surface = font.render('> ' + self.events[i], True, globals.BLACK)
            screen.blit(text_surface, (self.x + 5, self.y + 5 + i * 15))
            
