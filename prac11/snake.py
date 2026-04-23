import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("images/background2.png")
apple_img = pygame.image.load("images/apple.png")

bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
apple_img = pygame.transform.scale(apple_img, (20, 20))

snake = [(300, 300)]
dx, dy = 20, 0

def new_food():
    return (random.randint(1, 38)*20, random.randint(1, 28)*20)

food = new_food()
food_timer = time.time()

score = 0
level = 1
speed = 5  

clock = pygame.time.Clock()

running = True
while running:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and dy != 20:
        dx, dy = 0, -20
    elif keys[pygame.K_DOWN] and dy != -20:
        dx, dy = 0, 20
    elif keys[pygame.K_LEFT] and dx != 20:
        dx, dy = -20, 0
    elif keys[pygame.K_RIGHT] and dx != -20:
        dx, dy = 20, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if head == food:
        score += 1
        food = new_food()
        food_timer = time.time()

        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    if head in snake[1:]:
        print("GAME OVER")
        running = False

    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    if time.time() - food_timer >= 7:
        food = new_food()
        food_timer = time.time()

    for s in snake:
        pygame.draw.rect(screen, (0, 0, 255), (*s, 20, 20))

    screen.blit(apple_img, food)

    current_timer = int(time.time() - food_timer)

    font = pygame.font.SysFont(None, 36)

    timer_text = font.render(f"Time: {current_timer}/7", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 40))

    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 70))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()