import pygame
from settings import BULLET_SPEED

class Bullet:
    def __init__(self):
        self.width = 5
        self.height = 15
        self.color = (255, 255, 255)
        self.x = 0
        self.y = 0
        self.speed = BULLET_SPEED
        self.state = "ready"

    def fire(self, x, y):
        if self.state == "ready":
            self.x = x
            self.y = y
            self.state = "fire"

    def update(self):
        if self.state == "fire":
            self.y -= self.speed
            if self.y < 0:
                self.state = "ready"

    def draw(self, screen):
        if self.state == "fire":
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
