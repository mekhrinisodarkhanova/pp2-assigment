import pygame
import random
from persistence import save_score

class RacerGame:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.WIDTH, self.HEIGHT = screen.get_size()

        self.road = pygame.transform.scale(pygame.image.load("assets/road.png"), (self.WIDTH, self.HEIGHT))
        self.player_img = pygame.transform.scale(pygame.image.load("assets/car.png"), (150, 80))
        self.enemy_img = pygame.transform.scale(pygame.image.load("assets/enemy.png"), (50, 80))
        self.coin_img = pygame.transform.scale(pygame.image.load("assets/coin.png"), (30, 30))
        self.nitro_img = pygame.transform.scale(pygame.image.load("assets/nitro.png"), (30, 30))
        self.shield_img = pygame.transform.scale(pygame.image.load("assets/shield.png"), (30, 30))
        self.repair_img = pygame.transform.scale(pygame.image.load("assets/repair.png"), (30, 30))

        self.player = self.player_img.get_rect(center=(250, 500))

        self.enemy = self.enemy_img.get_rect(center=(250, -100))
        self.coin = self.coin_img.get_rect(center=(200, -50))

        self.base_speed = 3
        self.enemy_speed = self.base_speed
        self.coin_speed = 4

        self.score = 0
        self.font = pygame.font.SysFont(None, 36)

        self.bonus = None
        self.bonus_type = None
        self.bonus_spawn_time = 0

        self.active_bonus = None
        self.bonus_start_time = 0
        self.bonus_duration = 5000 

        self.repair_charge = 0

        self.player_speed = 6

    def rand_x(self):
        return random.randint(50, self.WIDTH - 50)

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            now = pygame.time.get_ticks()
            self.screen.blit(self.road, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

            keys = pygame.key.get_pressed()
            speed = self.player_speed

            if self.active_bonus == "nitro":
                speed = self.player_speed + 4

            if keys[pygame.K_LEFT]:
                self.player.x -= speed
            if keys[pygame.K_RIGHT]:
                self.player.x += speed

            self.player.left = max(self.player.left, 0)
            self.player.right = min(self.player.right, self.WIDTH)

            if self.score > 0 and self.score % 5 == 0:
                self.enemy_speed = self.base_speed + self.score // 5
                self.coin_speed = 4 + self.score // 5

            self.enemy.y += self.enemy_speed
            if self.enemy.y > self.HEIGHT:
                self.enemy.y = -100
                self.enemy.centerx = self.rand_x()

            self.coin.y += self.coin_speed
            if self.coin.y > self.HEIGHT:
                self.coin.y = -50
                self.coin.centerx = self.rand_x()

            if self.bonus is None and now - self.bonus_spawn_time > 4000:
                self.bonus_type = random.choice(["nitro", "shield", "repair"])
                self.bonus = pygame.Rect(self.rand_x(), -50, 30, 30)
                self.bonus_spawn_time = now

            if self.bonus:
                self.bonus.y += self.enemy_speed
                if self.bonus.y > self.HEIGHT:
                    self.bonus = None

            p = self.player.inflate(-30, -30)
            e = self.enemy.inflate(-20, -20)

            if p.colliderect(e):
                if self.active_bonus == "shield":
                    pass  # игнор урона
                elif self.repair_charge > 0:
                    self.repair_charge = 0
                else:
                    save_score(self.settings["name"], self.score)
                    return "menu"

                self.enemy.y = -100
                self.enemy.centerx = self.rand_x()

            if p.colliderect(self.coin):
                self.score += 1
                self.coin.y = -50
                self.coin.centerx = self.rand_x()

            if self.bonus and p.colliderect(self.bonus):
                self.active_bonus = self.bonus_type
                self.bonus_start_time = now
                self.bonus = None

                if self.active_bonus == "repair":
                    self.repair_charge = 1

            if self.active_bonus and now - self.bonus_start_time > self.bonus_duration:
                self.active_bonus = None

            self.screen.blit(self.player_img, self.player)
            self.screen.blit(self.enemy_img, self.enemy)
            self.screen.blit(self.coin_img, self.coin)

            if self.bonus:
                if self.bonus_type == "nitro":
                    self.screen.blit(self.nitro_img, self.bonus)
                elif self.bonus_type == "shield":
                    self.screen.blit(self.shield_img, self.bonus)
                elif self.bonus_type == "repair":
                    self.screen.blit(self.repair_img, self.bonus)

            text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))

            if self.active_bonus:
                bonus_text = self.font.render(f"BONUS: {self.active_bonus}", True, (255, 255, 0))
                self.screen.blit(bonus_text, (10, 40))

            pygame.display.update()
            clock.tick(60)