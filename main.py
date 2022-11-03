import pygame as p
p.init()

import globals
from game_state import GameState
from buildings import Road, Settlement, City
from player import Player
from hex import Edge, Vertex
from game import Game
import mouse as m

# main function contains game loop
def main():
    p.display.set_caption('Conquerors of Catalan')
    screen = p.display.set_mode((globals.WIDTH, globals.HEIGHT))

    clock = p.time.Clock()

    players = [Player('Taylor', p.Color('blue')), Player('Manasi', p.Color('orange')), Player('JB', p.Color('red'))]
    game = Game(players)
    gs = game.gs
    en = game.en

    hex = gs.b.get_hex(1, 1)
    hex1 = gs.b.get_hex(3, 2)
    hex2 = gs.b.get_hex(3, 4)
    hex3 = gs.b.get_hex(4, 3)
    hex4 = gs.b.get_hex(4, 2)
    hex5 = gs.b.get_hex(0, 0)

    City(game.players[0], hex.vertices[0])
    City(game.players[1], hex1.vertices[3])
    Road(game.players[1], hex1.edges[3])
    Settlement(game.players[2], hex.vertices[2])
    Settlement(game.players[2], hex1.vertices[5])
    Road(game.players[0], hex.edges[0])

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            
            if e.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                print(m.get_clicked(pos))

        screen.fill(globals.BACKGROUND_COLOR)
        game.draw(screen)
        p.display.flip()
        clock.tick(globals.MAX_FPS)

p.quit()

if __name__ == "__main__":
    main()