import pygame
from settings import PLAYER_SPEED, SCREEN_WIDTH

class Player:
    def __init__(self, x, y):
        self.width = 50
        self.height = 30
        self.color = (0, 255, 0)
        self.x = x
        self.y = y
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
