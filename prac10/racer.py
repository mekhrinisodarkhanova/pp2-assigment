import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

background = pygame.image.load("images/background1.png")
car_img = pygame.image.load("images/car.png")
coin_img = pygame.image.load("images/coin.png")

car_img = pygame.transform.scale(car_img, (150, 80))
coin_img = pygame.transform.scale(coin_img, (30, 30))
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

car_rect = car_img.get_rect(center=(WIDTH//2, HEIGHT - 80))

coin_rect = coin_img.get_rect()
coin_rect.x = random.randint(50, WIDTH - 50)
coin_rect.y = -50

speed = 5
coin_speed = 5

score = 0
font = pygame.font.SysFont("Verdana", 25)

def spawn_coin():
    coin_rect.x = random.randint(50, WIDTH - 50)
    coin_rect.y = -50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        car_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        car_rect.x += speed

    if car_rect.left < 0:
        car_rect.left = 0
    if car_rect.right > WIDTH:
        car_rect.right = WIDTH

    coin_rect.y += coin_speed

    if coin_rect.y > HEIGHT:
        spawn_coin()

    if car_rect.colliderect(coin_rect):
        score += 1
        spawn_coin()

    screen.blit(background, (0, 0))  
    screen.blit(car_img, car_rect)   
    screen.blit(coin_img, coin_rect) 

    text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(text, (250, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()