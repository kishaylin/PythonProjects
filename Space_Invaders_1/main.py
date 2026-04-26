import pygame
import math
import random

from settings import *
from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invaders")

player = Player(370, 480)
enemies = [Enemy() for _ in range(NUM_ENEMIES)]
bullet = Bullet()

score = 0
font = pygame.font.Font(None, 36)

def is_collision(e, b):
    distance = math.sqrt((e.x - b.x)**2 + (e.y - b.y)**2)
    return distance < 30

running = True
while running:
    screen.fill((0, 0, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.fire(player.x + 22, player.y)

    keys = pygame.key.get_pressed()
    player.move(keys)

    for enemy in enemies:
        enemy.update()

        if bullet.state == "fire" and is_collision(enemy, bullet):
            score += 1
            bullet.state = "ready"
            enemies.remove(enemy)
            enemies.append(Enemy())

        enemy.draw(screen)

    bullet.update()

    player.draw(screen)
    bullet.draw(screen)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
