import pygame, json
from game import Game
from db import *

pygame.init()
init_db()

def load_settings():
    with open("settings.json", "r") as f:
        return json.load(f)

def main():
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont(None, 40)

    username = ""
    typing = True

    settings = load_settings()

    # ввод имени
    while typing:
        screen.fill((0,0,0))
        txt = font.render("Enter name: " + username, True, (255,255,255))
        screen.blit(txt, (200, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += event.unicode

        pygame.display.update()

    player_id = get_or_create_player(username)
    best = get_best_score(player_id)

    game = Game(settings)
    score, level = game.run()

    save_game(player_id, score, level)

    # game over
    running = True
    while running:
        screen.fill((0,0,0))

        lines = [
            "GAME OVER",
            f"Score: {score}",
            f"Level: {level}",
            f"Best: {best}",
            "Press Q to quit"
        ]

        for i, l in enumerate(lines):
            screen.blit(font.render(l, True, (255,255,255)), (250, 200 + i*40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return

        pygame.display.update()

main()