import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.font_big = pygame.font.SysFont(None, 70)
        self.font_btn = pygame.font.SysFont(None, 45)  # меньше для кнопок
        self.font = pygame.font.SysFont(None, 40)

        self.WIDTH = screen.get_width()
        self.HEIGHT = screen.get_height()

    def input_name(self):
        name = ""
        active = True
        clock = pygame.time.Clock()

        while active:
            self.screen.fill((0, 0, 0))

            title = self.font_big.render("ENTER NAME", True, (255, 255, 255))
            self.screen.blit(title, (self.WIDTH//2 - title.get_width()//2, 120))

            box = pygame.Rect(self.WIDTH//2 - 130, 200, 260, 60)
            pygame.draw.rect(self.screen, (60, 60, 60), box)

            text = self.font.render(name, True, (255, 255, 255))
            self.screen.blit(text, (box.x + 10, box.y + 15))

            hint = self.font.render("Press ENTER to continue", True, (150,150,150))
            self.screen.blit(hint, (self.WIDTH//2 - hint.get_width()//2, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "PLAYER"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 10:
                            name += event.unicode

            pygame.display.update()
            clock.tick(60)

        return name if name != "" else "PLAYER"

    def button(self, text, y):
        rect = pygame.Rect(self.WIDTH//2 - 150, y, 300, 70)
        pygame.draw.rect(self.screen, (60, 60, 60), rect)

        label = self.font_btn.render(text, True, (255, 255, 255))
        self.screen.blit(label, (
            rect.centerx - label.get_width()//2,
            rect.centery - label.get_height()//2
        ))

        return rect

    def run(self):
        while True:
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if play.collidepoint(mx, my):
                        return "game"
                    if quitb.collidepoint(mx, my):
                        return "quit"

            play = self.button("PLAY", 170)
            self.button("LEADERBOARD", 270)
            quitb = self.button("QUIT", 370)

            pygame.display.update()