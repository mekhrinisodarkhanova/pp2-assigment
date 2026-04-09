import pygame

class Ball:
    def __init__(self, width, height):
        self.image = pygame.image.load("images/ball.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.x = width // 2
        self.y = height // 2

        self.speed = 20
        self.width = width
        self.height = height

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.speed >= 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + 50 + self.speed <= self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y - self.speed >= 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y + 50 + self.speed <= self.height:
            self.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))