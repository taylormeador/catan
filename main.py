import pygame as p
import sys
import time
p.init()

import globals
from game_state import GameState
from buildings import Builder, Road, Settlement, City

# main function contains game loop
def main():
    p.display.set_caption('Conquerors of Catalan')
    screen = p.display.set_mode((globals.WIDTH, globals.HEIGHT))
    screen.fill(globals.BACKGROUND_COLOR)
    clock = p.time.Clock()

    gs = GameState(['Taylor', 'Manasi', 'JB'])

    hex = gs.b.get_hex(3, 3)
    hex1 = gs.b.get_hex(3, 2)
    hex2 = gs.b.get_hex(3, 4)
    hex3 = gs.b.get_hex(4, 3)
    hex4 = gs.b.get_hex(4, 2)
    player = gs.players[1]
    road = Road(player, 0)
    road1 = Road(player, 1)
    road2 = Road(player, 2)
    road3 = Road(player, 3)
    road4 = Road(player, 4)
    road5 = Road(player, 5)
    settlement = Settlement(player, 2)
    city = City(player, 4)

    Builder.build(road, hex)
    Builder.build(road1, hex)
    Builder.build(road2, hex)
    Builder.build(road3, hex)
    Builder.build(road4, hex)
    Builder.build(road5, hex)
    Builder.build(road, hex1)
    Builder.build(road1, hex1)
    Builder.build(road2, hex1)
    Builder.build(road3, hex1)
    Builder.build(road4, hex1)
    Builder.build(road5, hex1)
    Builder.build(road, hex2)
    Builder.build(road1, hex2)
    Builder.build(road2, hex2)
    Builder.build(road3, hex2)
    Builder.build(road4, hex2)
    Builder.build(road5, hex2)
    Builder.build(road, hex3)
    Builder.build(road1, hex3)
    Builder.build(road2, hex3)
    Builder.build(road3, hex3)
    Builder.build(road4, hex3)
    Builder.build(road5, hex3)
    Builder.build(road, hex4)
    Builder.build(road1, hex4)
    Builder.build(road2, hex4)
    Builder.build(road3, hex4)
    Builder.build(road4, hex4)
    Builder.build(road5, hex4)
    Builder.build(settlement, hex1)
    Builder.build(settlement, hex2)
    Builder.build(city, hex1)
    Builder.build(city, hex4)
    Builder.build(city, hex)

    print(hex.edges)
    print(hex.vertices)



    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        gs.b.draw(screen)
        p.display.flip()
        clock.tick(globals.MAX_FPS)

p.quit()

if __name__ == "__main__":
    main()