import pygame
import random
from settings import ENEMY_SPEED, SCREEN_WIDTH

class Enemy:
    def __init__(self):
        self.width = 40
        self.height = 30
        self.color = (255, 0, 0)
        self.x = random.randint(0, SCREEN_WIDTH - self.width)
        self.y = random.randint(50, 150)
        self.speed = ENEMY_SPEED
        self.direction = 1

    def update(self):
        self.x += self.speed * self.direction

        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.width:
            self.direction *= -1
            self.y += 40

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
