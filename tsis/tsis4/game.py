import pygame, random, time
from config import *

class Game:
    def __init__(self, settings):
        self.settings = settings

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load("assets/background.png")
        self.apple = pygame.image.load("assets/apple.png")
        self.poison = pygame.image.load("assets/poison.png")

        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.apple = pygame.transform.scale(self.apple, (GRID, GRID))
        self.poison = pygame.transform.scale(self.poison, (GRID, GRID))

        self.snake = [(300, 300)]
        self.dx, self.dy = GRID, 0

        self.food = self.spawn()
        self.poison_pos = self.spawn()

        self.timer_start = time.time()

        self.score = 0
        self.level = 1
        self.speed = 5

    def spawn(self):
        return (
            random.randint(1, WIDTH // GRID - 2) * GRID,
            random.randint(1, HEIGHT // GRID - 2) * GRID
        )

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return self.score, self.level

            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and self.dy == 0:
                self.dx, self.dy = 0, -GRID
            elif keys[pygame.K_DOWN] and self.dy == 0:
                self.dx, self.dy = 0, GRID
            elif keys[pygame.K_LEFT] and self.dx == 0:
                self.dx, self.dy = -GRID, 0
            elif keys[pygame.K_RIGHT] and self.dx == 0:
                self.dx, self.dy = GRID, 0

            head = (self.snake[0][0] + self.dx,
                    self.snake[0][1] + self.dy)

            if head[0] < 0 or head[1] < 0 or head[0] >= WIDTH or head[1] >= HEIGHT:
                break

            if head in self.snake:
                break

            if head == self.poison_pos:
                break

            self.snake.insert(0, head)

            if head == self.food:
                self.score += 1
                self.timer_start = time.time()
                self.food = self.spawn()
                self.poison_pos = self.spawn()

                if self.score % 5 == 0:
                    self.level += 1
                    self.speed += 1
            else:
                self.snake.pop()

            current_time = int(time.time() - self.timer_start)
            if current_time >= 7:
                self.food = self.spawn()
                self.poison_pos = self.spawn()
                self.timer_start = time.time()

            self.screen.blit(self.bg, (0, 0))

            for s in self.snake:
                pygame.draw.rect(self.screen, self.settings["snake_color"], (*s, GRID, GRID))

            self.screen.blit(self.apple, self.food)
            self.screen.blit(self.poison, self.poison_pos)

            font = pygame.font.SysFont(None, 30)
            self.screen.blit(font.render(f"Score: {self.score}", True, (255,255,255)), (10,10))
            self.screen.blit(font.render(f"Level: {self.level}", True, (255,255,255)), (10,40))
            self.screen.blit(font.render(f"Time: {current_time}/7", True, (255,255,255)), (10,70))

            pygame.display.update()
            self.clock.tick(self.speed)

        return self.score, self.level