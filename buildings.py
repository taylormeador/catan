from hex import HEX_RADIUS
import math
import pygame as p
import globals



# this class will handle the insertion/deletion of building objects to hex 
class Builder:
    def build(building, hex):
        if isinstance(building, Road):
            hex.edges[building.edge_int] = building

        elif isinstance(building, Settlement) or isinstance(building, City):
            hex.vertices[building.edge_int] = building


# base class for roads, settlements, and cities
class Building:
    buildings = []

    def __init__(self, owner, edge_int):
        self.owner = owner
        self.edge_int = edge_int
        Building.buildings.append(self)

    def make_triangle(self, scale, internal_angle, rotation, x_offset, y_offset):
        #define the points in a uint space
        ia = (math.radians(internal_angle) * 2) - 1
        p1 = (0, -1)
        p2 = (math.cos(ia), math.sin(ia))
        p3 = (math.cos(ia) * -1, math.sin(ia))

        #rotate the points
        ra = math.radians(rotation) 
        rp1x = p1[0] * math.cos(ra) - p1[1] * math.sin(ra)
        rp1y = p1[0] * math.sin(ra) + p1[1] * math.cos(ra)                 
        rp2x = p2[0] * math.cos(ra) - p2[1] * math.sin(ra)
        rp2y = p2[0] * math.sin(ra) + p2[1] * math.cos(ra)                        
        rp3x = p3[0] * math.cos(ra) - p3[1] * math.sin(ra)                         
        rp3y = p3[0] * math.sin(ra) + p3[1] * math.cos(ra)
        rp1 = (rp1x, rp1y)
        rp2 = (rp2x, rp2y)
        rp3 = (rp3x, rp3y)

        #scale the points 
        sp1 = [rp1[0] * scale + x_offset, rp1[1] * scale + y_offset]
        sp2 = [rp2[0] * scale + x_offset, rp2[1] * scale + y_offset]
        sp3 = [rp3[0] * scale + x_offset, rp3[1] * scale + y_offset]
                        
        return (sp1, sp2, sp3)


class Road(Building):
    def __init__(self, owner, edge_int):
        super().__init__(owner, edge_int)

    def get_coordinates(self, parent_x, parent_y):
        x_direction = 1 if self.edge_int < 3 else -1
        y_direction = -1 if self.edge_int == 0 or self.edge_int == 5 else 1

        x = parent_x + x_direction * HEX_RADIUS / 2.2
        y = parent_y + y_direction * HEX_RADIUS / 1.3

        if self.edge_int == 1 or self.edge_int == 4:
            x += x_direction * HEX_RADIUS / 2.3
            y = parent_y

        return x, y

    def draw(self, screen, parent_x, parent_y):
        rotations = [150, 90, 30, 150, 90, 30]
        x, y = self.get_coordinates(parent_x, parent_y)
        width = HEX_RADIUS * .7
        height = HEX_RADIUS * .2
        rotation = rotations[self.edge_int]
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
        p.draw.polygon(screen, globals.BLACK, points, width=3)
        return

    def __str__(self):
        return str(self.owner) + '\'s Road'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Road>'


class Settlement(Building):
    def __init__(self, owner, edge_int):
        super().__init__(owner, edge_int)

    def draw(self, screen, parent_x, parent_y):
        rect = p.Rect(parent_x - HEX_RADIUS / 4.4, parent_y - HEX_RADIUS * 1.1, HEX_RADIUS * .5, HEX_RADIUS * .5)
        triangle_points = self.make_triangle(15, 45, 0, parent_x - HEX_RADIUS * 0.001, parent_y - HEX_RADIUS * 1.25)
        p.draw.polygon(screen, self.owner.color, triangle_points)
        p.draw.polygon(screen, globals.BLACK, triangle_points, width=3)
        p.draw.rect(screen, self.owner.color, rect)
        p.draw.rect(screen, globals.BLACK, rect, width=3)
        return

    def __str__(self):
        return str(self.owner) + '\'s Settlement'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Settlement>'


class City(Building):
    def __init__(self, owner, edge_int):
        super().__init__(owner, edge_int)

    def draw(self, screen, parent_x, parent_y):
        rect = p.Rect(parent_x - HEX_RADIUS / 2.2, parent_y - HEX_RADIUS * 1.1, HEX_RADIUS * .9, HEX_RADIUS * .5)
        triangle_points = self.make_triangle(15, 45, 0, parent_x - HEX_RADIUS * 0.2, parent_y - HEX_RADIUS * 1.25)
        p.draw.polygon(screen, self.owner.color, triangle_points)
        p.draw.polygon(screen, globals.BLACK, triangle_points, width=3)
        p.draw.rect(screen, self.owner.color, rect)
        p.draw.rect(screen, globals.BLACK, rect, width=3)
        return

    def __str__(self):
        return str(self.owner) + '\'s City'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s City>'
