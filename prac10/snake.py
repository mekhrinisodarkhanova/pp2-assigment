import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

background = pygame.image.load("images/background2.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

apple_img = pygame.image.load("images/apple.png")
apple_img = pygame.transform.scale(apple_img, (20, 20))

WALL_COLOR = (0, 0, 0)

BLOCK_SIZE = 20

snake = [(300, 300)]
direction = (BLOCK_SIZE, 0)

def spawn_food():
    while True:
        x = random.randrange(BLOCK_SIZE, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        y = random.randrange(BLOCK_SIZE, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

        if (x, y) not in snake:
            return (x, y)

food = spawn_food()

score = 0
level = 1
speed = 3

font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(speed)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, BLOCK_SIZE):
                direction = (0, -BLOCK_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -BLOCK_SIZE):
                direction = (0, BLOCK_SIZE)
            elif event.key == pygame.K_LEFT and direction != (BLOCK_SIZE, 0):
                direction = (-BLOCK_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-BLOCK_SIZE, 0):
                direction = (BLOCK_SIZE, 0)

    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (
        head[0] < BLOCK_SIZE or
        head[0] >= WIDTH - BLOCK_SIZE or
        head[1] < BLOCK_SIZE or
        head[1] >= HEIGHT - BLOCK_SIZE
    ):
        print("Game Over (Wall)")
        running = False

    if head in snake:
        print("Game Over (Self)")
        running = False

    snake.insert(0, head)

    if head == food:
        score += 1
        food = spawn_food()

        if score % 5 == 0:
            level += 1
            speed += 2

    else:
        snake.pop()

    screen.blit(background, (0, 0))

    pygame.draw.rect(screen, WALL_COLOR, (0, 0, WIDTH, BLOCK_SIZE)) 
    pygame.draw.rect(screen, WALL_COLOR, (0, HEIGHT - BLOCK_SIZE, WIDTH, BLOCK_SIZE))  
    pygame.draw.rect(screen, WALL_COLOR, (0, 0, BLOCK_SIZE, HEIGHT))  
    pygame.draw.rect(screen, WALL_COLOR, (WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, HEIGHT))  

    for segment in snake:
        pygame.draw.rect(screen, (0, 0, 255), (*segment, BLOCK_SIZE, BLOCK_SIZE))

    screen.blit(apple_img, food)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()

pygame.quit()