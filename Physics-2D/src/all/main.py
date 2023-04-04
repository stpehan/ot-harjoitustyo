import pygame 
from gameloop import GameLoop
from renderer import Renderer
from clock import Clock
#from rectangle import Rectangle

def main():
    #init display
    WIDTH = 400
    HEIGHT = 400
    display = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Physics 2D")

    #init classes
    renderer = Renderer(display)
    clock = Clock()
    gameloop = GameLoop(renderer, clock, display)

    pygame.init()
    gameloop.start()


if __name__ == "__main__":
    main()