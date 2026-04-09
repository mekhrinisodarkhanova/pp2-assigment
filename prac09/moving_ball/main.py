import pygame
import sys
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("images/bg.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

ball = Ball(WIDTH, HEIGHT)
clock = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys)
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)