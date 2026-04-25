import pygame
from racer import RacerGame
from ui import Menu

pygame.init()

screen = pygame.display.set_mode((500,600))

menu = Menu(screen)

state = "menu"
player_name = "PLAYER"

running = True
while running:

    if state == "menu":
        player_name = menu.input_name()  
        state = menu.run()

    elif state == "game":
        game = RacerGame(screen, {"name": player_name})
        state = game.run()

    elif state == "quit":
        running = False

pygame.quit()