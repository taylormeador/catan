from hex import HEX_RADIUS
import math
import pygame as p


# this class will handle the insertion/deletion of building objects to hex 
class Builder:
    def __init__(self):
        pass

    def build(building, hex, position):
        if isinstance(building, Road):
            hex.edges[position] = building

        elif isinstance(building, Settlement) or isinstance(building, City):
            hex.vertices[position] = building


class Building:
    def __init__(self, owner):
        self.owner = owner

class Road(Building):
    def __init__(self, owner):
        super().__init__(owner)

    def draw(self, screen):
        rotations = [150, 90, 30, 150, 90, 30]
        x, y = self.get_road_coordinates()
        width = HEX_RADIUS * .8
        height = HEX_RADIUS / 4
        rotation = rotations[self.trade_edge_int]
        points = []

        # The distance from the center of the rectangle to one of the corners is the same for each corner
        radius = math.sqrt((height / 2)**2 + (width / 2)**2)

        # Get the angle to one of the corners with respect to the x axis
        angle = math.atan2(height / 2, width / 2)

        # Transform that angle to reach each corner of the rectangle
        angles = [angle, -angle + math.pi, angle + math.pi, -angle]

        # Convert rotation from degrees to radians
        rot_radians = (math.pi / 180) * rotation

        # Calculate the coordinates of each point
        for angle in angles:
            y_offset = -1 * radius * math.sin(angle + rot_radians)
            x_offset = radius * math.cos(angle + rot_radians)
            points.append((x + x_offset, y + y_offset))

        p.draw.polygon(screen, self.owner.color, points)
        return

    def __str__(self):
        return str(self.owner) + '\'s Road'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Road>'


class Settlement(Building):
    def __init__(self, owner):
        super().__init__(owner)

    def __str__(self):
        return str(self.owner) + '\'s Settlement'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Settlement>'


class City(Building):
    def __init__(self, owner):
        super().__init__(owner)

    def __str__(self):
        return str(self.owner) + '\'s City'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s City>'
