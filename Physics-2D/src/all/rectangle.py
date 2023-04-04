import pygame
import random
import math



class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()

        col = random.randint(0,255)
        col2 = random.randint(0,255)
        col3 = random.randint(0,255)

        self.image = pygame.Surface([size, size])
        self.image.fill((col, col2, col3))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.size = size
        self.velocity = 0

    def update(self):
        self.gravity()

    def calculate_gravity(self):
        #TODO: calculate drag coefficient (currently 0.0005!)
        #TODO: rects have no mass! (currently 1)
        terminal_vel = math.sqrt((2*0.1*9.81)/(0.0005*1.225*(self.size//100)))
        if self.velocity < terminal_vel:
            self.velocity += 0.1 * 9.81 #m/s
        return self.velocity
    
    def gravity(self):
        #TODO: get width and height of display (currently 400)
        if self.rect.bottom < 400:
            self.fall(self.calculate_gravity())
        else:
            self.stop(400)

    def fall(self, speed):
        self.rect.y += speed

    def stop(self, y):
        self.velocity = 0
        self.rect.bottom = y

    def get_pos(self):
        return (self.rect.x, self.rect.y)
    
    