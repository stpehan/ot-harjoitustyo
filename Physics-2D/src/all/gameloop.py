import pygame

class GameLoop:
    def __init__(self, renderer, clock, display):
        self._clock = clock
        self._renderer = renderer
        self._display = display

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            self._render()
            self._clock.tick(60)
            
    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.MOUSEBUTTONDOWN:
                   pass 
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._renderer.add_rect(100)
                self._renderer.rectangles.draw(self._display)
            elif event.type == pygame.QUIT:
                return False
            
    def _render(self):
        self._renderer.render()