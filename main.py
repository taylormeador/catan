import pygame as p
import sys
import time

import globals

# main function contains game loop
def main():
    p.init()
    p.display.set_caption('Conquerors of Catalan')
    screen = p.display.set_mode((globals.WIDTH, globals.HEIGHT))
    screen.fill(globals.BACKGROUND_COLOR)
    clock = p.time.Clock()

    # game loop
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False

        p.display.update()
        p.display.flip()
        clock.tick(globals.MAX_FPS)

p.quit()

if __name__ == "__main__":
    main()