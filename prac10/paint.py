import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

background = pygame.image.load("images/background3.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rect_btn   = pygame.Rect(29, 51, 70, 70)
circle_btn = pygame.Rect(29, 139, 70, 70)
eraser_btn = pygame.Rect(29, 226, 70, 70)
red_btn    = pygame.Rect(27, 328, 30, 30)
yellow_btn = pygame.Rect(71, 328, 30, 30)
blue_btn   = pygame.Rect(27, 372, 30, 30)
green_btn  = pygame.Rect(72, 372, 30, 30)

canvas_rect = pygame.Rect(161, 100, 500, 320)
canvas = pygame.Surface((canvas_rect.width, canvas_rect.height))
canvas.fill((255, 255, 255))

tool = "rect"
drawing = False
start_pos = None

color = (255, 0, 0)

clock = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))
    screen.blit(canvas, canvas_rect.topleft)

    preview = canvas.copy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            if rect_btn.collidepoint(x, y):
                tool = "rect"

            elif circle_btn.collidepoint(x, y):
                tool = "circle"

            elif eraser_btn.collidepoint(x, y):
                tool = "eraser"

            elif red_btn.collidepoint(x, y):
                color = (255, 0, 0)

            elif yellow_btn.collidepoint(x, y):
                color = (255, 255, 0)

            elif blue_btn.collidepoint(x, y):
                color = (0, 0, 255)

            elif green_btn.collidepoint(x, y):
                color = (0, 255, 0)

            elif canvas_rect.collidepoint(x, y):
                drawing = True
                start_pos = (x - canvas_rect.x, y - canvas_rect.y)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                x, y = pygame.mouse.get_pos()
                end_pos = (x - canvas_rect.x, y - canvas_rect.y)

                if tool == "rect":
                    rect = pygame.Rect(start_pos,
                        (end_pos[0] - start_pos[0],
                         end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, rect, 2)

                elif tool == "circle":
                    radius = int(((end_pos[0] - start_pos[0])**2 +
                                  (end_pos[1] - start_pos[1])**2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius, 2)

                drawing = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos

            if drawing and tool == "eraser":
                if canvas_rect.collidepoint(x, y):
                    pygame.draw.circle(
                        canvas,
                        (255, 255, 255),
                        (x - canvas_rect.x, y - canvas_rect.y),
                        12
                    )

    if drawing and tool in ["rect", "circle"]:
        x, y = pygame.mouse.get_pos()
        end_pos = (x - canvas_rect.x, y - canvas_rect.y)

        if tool == "rect":
            rect = pygame.Rect(start_pos,
                (end_pos[0] - start_pos[0],
                 end_pos[1] - start_pos[1]))
            pygame.draw.rect(preview, color, rect, 2)

        elif tool == "circle":
            radius = int(((end_pos[0] - start_pos[0])**2 +
                          (end_pos[1] - start_pos[1])**2) ** 0.5)
            pygame.draw.circle(preview, color, start_pos, radius, 2)

        screen.blit(preview, canvas_rect.topleft)

    if tool == "rect":
        pygame.draw.rect(screen, (0,0,0), rect_btn, 2)
    if tool == "circle":
        pygame.draw.rect(screen, (0,0,0), circle_btn, 2)
    if tool == "eraser":
        pygame.draw.rect(screen, (0,0,0), eraser_btn, 2)

    if color == (255, 0, 0):
        pygame.draw.rect(screen, (0,0,0), red_btn, 2)
    if color == (255, 255, 0):
        pygame.draw.rect(screen, (0,0,0), yellow_btn, 2)
    if color == (0, 0, 255):
        pygame.draw.rect(screen, (0,0,0), blue_btn, 2)
    if color == (0, 255, 0):
        pygame.draw.rect(screen, (0,0,0), green_btn, 2)

    pygame.display.flip()
    clock.tick(60)