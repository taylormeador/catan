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
    print(gs.turn)
    for player in gs.players:
        print(player.resources)
    print(gs.e.roll_dice())
    hex = gs.b.get_hex(4, 3)
    player = gs.players[0]
    road = Road(player)
    Builder.build(road, hex, 0)
    print(hex.edges)

    settlement = Settlement(player)
    city = City(player)
    Builder.build(settlement, hex, 2)
    Builder.build(city, hex, 4)

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