import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

road = pygame.image.load("images/background1.png")
player_img = pygame.image.load("images/car.png")
enemy_img = pygame.image.load("images/enemy.png")
coin_img = pygame.image.load("images/coin.png")

road = pygame.transform.scale(road, (WIDTH, HEIGHT))
player_img = pygame.transform.scale(player_img, (150, 80))
enemy_img = pygame.transform.scale(enemy_img, (50, 80))
coin_img = pygame.transform.scale(coin_img, (30, 30))

player = player_img.get_rect(center=(250, 500))
enemy = enemy_img.get_rect(center=(random.randint(50, WIDTH-50), -100))
coin = coin_img.get_rect(center=(random.randint(50, WIDTH-50), -50))

enemy_speed = 3
coin_weight = random.choice([1, 2, 3])

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.blit(road, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 6
    if keys[pygame.K_RIGHT]:
        player.x += 6

    if player.left < 0:
        player.left = 0
    if player.right > WIDTH:
        player.right = WIDTH

    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = -100

        while True:
            new_x = random.randint(50, WIDTH-50)
            if abs(new_x - coin.centerx) > 60:
                break
        enemy.centerx = new_x

    coin.y += 4
    if coin.y > HEIGHT:
        coin.y = -50
        coin_weight = random.choice([1, 2, 3])

        while True:
            new_x = random.randint(50, WIDTH-50)
            if abs(new_x - enemy.centerx) > 60:
                break
        coin.centerx = new_x

    if player.colliderect(coin):
        score += coin_weight
        coin.y = -50

    if player.colliderect(enemy):
        print("GAME OVER")
        running = False

    if score % 3 == 0 and score != 0:
        enemy_speed = 3 + score // 3

    screen.blit(player_img, player)
    screen.blit(enemy_img, enemy)
    screen.blit(coin_img, coin)

    score_text = font.render(f"Score: {score}", True, (255,255,255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()