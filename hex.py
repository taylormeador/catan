import random
import pygame as p
import math

import globals

HEX_RADIUS = 50
HEX_WIDTH = HEX_RADIUS * 2
WOOD_COLOR = p.Color('darkorange4')
BRICK_COLOR = p.Color('firebrick')
SHEEP_COLOR = p.Color('chartreuse2')
WHEAT_COLOR = p.Color('gold')
ORE_COLOR = p.Color('azure4')
WATER_COLOR = p.Color('aqua')
DESERT_COLOR = p.Color('darkgoldenrod3')
CHIT_COLOR = p.Color('beige')


class Hex:
    hexes = []
    types = ['desert', 'water', 'harbor', 'wood', 'brick', 'sheep', 'wheat', 'ore']
    instantiated = {'desert': 0, 'water': 0, 'harbor': 0, 'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}

    def __init__(self, type, row, col):
        assert type in Hex.types
        self.type = type
        self.row = row
        self.col = col
        self.x, self.y = self.get_coordinates(row, col)
        Hex.hexes.append(self)
        Hex.instantiated[type] += 1

    def get_coordinates(self, row, col):
        x_offset = globals.WIDTH / 6
        y_offset = globals.HEIGHT / 16
        x = col * HEX_WIDTH * .88 + ((6 - row) * HEX_RADIUS * .88) + x_offset
        if row > 2:
            x = col * HEX_WIDTH * .88 + (row * HEX_RADIUS * .88) + x_offset
        y = row * HEX_RADIUS * 1.55 + HEX_WIDTH + y_offset
        return x, y

    def generate_random_resource_hex(i, j):
        return ResourceHex(i, j)

    def generate_random_harbor_hex(i, j):
        return HarborHex(i, j)

    def generate_water_hex(i, j):
        return WaterHex(i, j)

    def generate_desert_hex(i, j):
        return DesertHex(i, j)

    def draw_hexagon(self, surface, color, r, x, y):
        n = 6
        offset = 32.988
        point_list = [
            (x + r * math.cos(2 * math.pi * i / n + offset), y + r * math.sin(2 * math.pi * i / n + offset))
            for i in range(n)
        ]
        p.draw.polygon(surface, color, point_list, 0)
        p.draw.polygon(surface, globals.BLACK, point_list, 3)


    def draw(self, screen):
        self.draw_hexagon(screen, self.color, HEX_RADIUS, self.x, self.y)

    def __str__(self):
        if self.type in ResourceHex.resource_types:
            return self.type + " - " + str(self.number)
        return self.type

    def __repr__(self):
        return self.__str__()


class ResourceHex(Hex):
    resource_hexes = []
    chit_numbers = [5, 10, 8, 2, 9, 3, 4, 6, 11, 6, 11, 3, 4, 5, 12, 8, 10, 9]
    resource_types = ['wood', 'brick', 'sheep', 'wheat', 'ore']
    resource_colors = {'wood': WOOD_COLOR, 'brick': BRICK_COLOR, 'sheep': SHEEP_COLOR, 'wheat': WHEAT_COLOR, 'ore': ORE_COLOR}

    def __init__(self, row, col):
        self.type = ResourceHex.get_random_type()
        super().__init__(self.type, row, col)
        self.number = ResourceHex.chit_numbers[len(ResourceHex.resource_hexes)]
        self.color = ResourceHex.resource_colors[self.type]
        self.resource_hexes.append(self)

    def get_random_type():
        random_number = random.randint(0, len(ResourceHex.resource_types) - 1)
        type = ResourceHex.resource_types[random_number]
        existing_hexes_of_type = Hex.instantiated[type]

        if (type == 'wood' or type == 'wheat' or type == 'sheep') and existing_hexes_of_type == 4:
            return ResourceHex.get_random_type()
        elif (type == 'ore' or type == 'brick') and existing_hexes_of_type == 3:
            return ResourceHex.get_random_type()
        return type

    def draw(self, screen):
        super().draw(screen)
        self.draw_chit(screen)

    def draw_chit(self, screen):
        # draw circle
        chit_radius = 20
        p.draw.circle(screen, CHIT_COLOR, (self.x, self.y), chit_radius)
        p.draw.circle(screen, globals.BLACK, (self.x, self.y), chit_radius, width=2)
        
        # draw number in chit
        p.font.init()
        font = p.font.Font(p.font.get_default_font(), 18)
        text_surface = font.render(str(self.number), True, globals.BLACK)
        font_x = self.x - (chit_radius / 2)
        font_y = self.y - (chit_radius / 2)
        if len(str(self.number)) == 1:
            font_x = self.x - (chit_radius / 4)
        screen.blit(text_surface, (font_x, font_y))

        # draw dots below number
        num_dots_hash = {2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 8: 5, 9: 4, 10: 3, 11: 2, 12: 1}
        num_dots = num_dots_hash[self.number]
        for i in range(num_dots):
            direction = (-1) ** i
            offset = (i + 1) // 2
            if i == 0:
                direction = 0
            # even amounts split center, odd amounts start at center
            if num_dots % 2 == 0: 
                p.draw.circle(screen, globals.BLACK, (self.x + 3 + direction * 5 * offset, self.y + chit_radius / 2), 2)
            else:
                p.draw.circle(screen, globals.BLACK, (self.x + direction * 5 * offset, self.y + chit_radius / 2), 2)

class DesertHex(Hex):
    color = DESERT_COLOR

    def __init__(self, row, col):
        super().__init__('desert', row, col)


class HarborHex(Hex):
    color = WATER_COLOR
    trade_resources = ['any', 'wood', 'brick', 'sheep', 'wheat', 'ore']
    harbors_instantiated = {'any': 0, 'wood': 0, 'brick': 0, 'sheep': 0, 'wheat': 0, 'ore': 0}
    harbors_remaining = {'any': 4, 'wood': 1, 'brick': 1, 'sheep': 1, 'wheat': 1, 'ore': 1}

    def __init__(self, row, col):
        super().__init__('harbor', row, col)
        self.trade_resource = HarborHex.get_random_trade_resource()
        HarborHex.harbors_instantiated[self.trade_resource] += 1
        HarborHex.harbors_remaining[self.trade_resource] -= 1

    def get_random_trade_resource():
        random_int = random.randint(0, len(HarborHex.trade_resources) - 1)
        resource = HarborHex.trade_resources[random_int]
        if HarborHex.harbors_remaining[resource] == 0:
            return HarborHex.get_random_trade_resource()
        return resource


class WaterHex(Hex):
    color = WATER_COLOR
    def __init__(self, row, col):
        super().__init__('water', row, col)
