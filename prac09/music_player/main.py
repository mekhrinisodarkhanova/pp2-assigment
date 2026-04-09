import pygame
import sys
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

# фон
background = pygame.image.load("images/bg.png")
background = pygame.transform.scale(background, (600, 400))

player = MusicPlayer()
font = pygame.font.Font(None, 36)

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()
            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    text = font.render("Track: " + player.get_current_track(), True, (255, 255, 255))
    screen.blit(text, (20, 350))

    pygame.display.flip()