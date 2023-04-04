import pygame
from rectangle import Rectangle

class Renderer:
    def __init__(self, display):
        self._display = display
        self.rectangle = None
        self.rectangles = pygame.sprite.Group()


    def add_rect(self, size):
        pos = pygame.mouse.get_pos()
        self.rectangle = Rectangle(pos[0], pos[1], size)
        self.rectangles.add(self.rectangle)

    def render(self):
        self._display.fill((0,0,0))
        self.rectangles.update()
        self.rectangles.draw(self._display)
        pygame.display.update()
        