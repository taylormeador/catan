import pygame as p
p.init()

import globals
from game_state import GameState
from buildings import Builder, Road, Settlement, City
from player import Player

# main function contains game loop
def main():
    p.display.set_caption('Conquerors of Catalan')
    screen = p.display.set_mode((globals.WIDTH, globals.HEIGHT))
    screen.fill(globals.BACKGROUND_COLOR)
    clock = p.time.Clock()
    
    gs = GameState([Player('Taylor', p.Color('blue')), Player('Manasi', p.Color('orange')), Player('JB', p.Color('red'))])
    en = gs.en

    hex = gs.b.get_hex(3, 3)
    hex1 = gs.b.get_hex(3, 2)
    hex2 = gs.b.get_hex(3, 4)
    hex3 = gs.b.get_hex(4, 3)
    hex4 = gs.b.get_hex(4, 2)
    hex5 = gs.b.get_hex(0, 0)

    print(hex, hex.neighbors)
    print()
    print(hex1, hex1.neighbors)
    print()
    print(hex2, hex2.neighbors)
    print()
    print(hex3, hex3.neighbors)
    print()
    print(hex4, hex4.neighbors)
    print()
    print(hex5, hex5.neighbors)

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            if e.type == p.MOUSEBUTTONDOWN:
                en.roll_dice()
                for player in gs.players:
                    print(player.resources)


        gs.b.draw(screen)
        p.display.flip()
        clock.tick(globals.MAX_FPS)

p.quit()

if __name__ == "__main__":
    main()