from hex import HEX_RADIUS, Edge, Vertex
import math
import pygame as p
import globals


# base class for roads, settlements, and cities
class Building:
    buildings = []

    def __init__(self, owner, location):
        self.owner = owner
        self.location = location
        self.build()
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

    def build(self):
        self.location.building = self
        self.location.occupied = True
        if isinstance(self, Road):
            self.owner.roads.append(self)
            # TODO update longest road here?
        elif isinstance(self, Settlement):
            self.owner.settlements.append(self)
        elif isinstance(self, City):
            self.owner.cities.append(self)


class Road(Building):
    def __init__(self, owner, edge):
        super().__init__(owner, edge)
        self.cost = {'wood': 1, 'brick': 1}

    def draw(self, screen):
        rotations = [150, 90, 30, 150, 90, 30]
        x, y = self.location.x, self.location.y
        width = HEX_RADIUS * .7
        height = HEX_RADIUS * .2
        rotation = rotations[self.location.position]
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
        p.draw.polygon(screen, globals.BLACK, points, width=2)
        return

    def __str__(self):
        return str(self.owner) + '\'s Road'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Road>'


class Settlement(Building):
    def __init__(self, owner, vertex):
        super().__init__(owner, vertex)
        self.cost = {'wood': 1, 'brick': 1, 'sheep': 1, 'wheat': 1}

    def draw(self, screen):
        x, y = self.location.x, self.location.y
        rect = p.Rect(x - 11, y - 10, HEX_RADIUS * .4, HEX_RADIUS * .4)
        triangle_points = self.make_triangle(11, 45, 0, x - 1.5, y - 15)
        p.draw.polygon(screen, self.owner.color, triangle_points)
        p.draw.polygon(screen, globals.BLACK, triangle_points, width=2)
        p.draw.rect(screen, self.owner.color, rect)
        p.draw.rect(screen, globals.BLACK, rect, width=2)


    def __str__(self):
        return str(self.owner) + '\'s Settlement'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s Settlement>'


class City(Building):
    def __init__(self, owner, vertex):
        super().__init__(owner, vertex)
        self.cost = {'ore': 3, 'wheat': 2}

    def draw(self, screen):
        x, y = self.location.x, self.location.y
        rect = p.Rect(x - 16, y - 8, HEX_RADIUS * .6, HEX_RADIUS * .4)
        triangle_points = self.make_triangle(11, 45, 0, x - 6, y - 13)
        p.draw.polygon(screen, self.owner.color, triangle_points)
        p.draw.polygon(screen, globals.BLACK, triangle_points, width=2)
        p.draw.rect(screen, self.owner.color, rect)
        p.draw.rect(screen, globals.BLACK, rect, width=2)
        return

    def __str__(self):
        return str(self.owner) + '\'s City'

    def __repr__(self):
        return '<' + str(self.owner) + '\'s City>'
