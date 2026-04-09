import pygame
import sys
from clock import draw_clock

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_clock(screen)

    pygame.display.flip()
    clock.tick(60)