from hex import HEX_RADIUS
import math
import pygame as p


class Road:
    def __init__(self):
        pass

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


class Settlement:
    def __init__(self):
        pass


class City:
    def __init__(self):
        pass