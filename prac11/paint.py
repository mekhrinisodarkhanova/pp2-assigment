import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

background = pygame.image.load("images/background3.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

rect_btn   = pygame.Rect(20, 40, 60, 60)
circle_btn = pygame.Rect(90, 40, 60, 60)
square_btn = pygame.Rect(20, 110, 60, 60)
tri_r_btn  = pygame.Rect(90, 110, 60, 60)
tri_e_btn  = pygame.Rect(20, 180, 60, 60)
rhomb_btn  = pygame.Rect(90, 180, 60, 60)
eraser_btn = pygame.Rect(20, 250, 130, 50)
red_btn    = pygame.Rect(20, 320, 30, 30)
yellow_btn = pygame.Rect(60, 320, 30, 30)
blue_btn   = pygame.Rect(100, 320, 30, 30)
green_btn  = pygame.Rect(140, 320, 30, 30)

canvas_rect = pygame.Rect(180, 50, 500, 380)
canvas = pygame.Surface((canvas_rect.width, canvas_rect.height))
canvas.fill((255, 255, 255))

tool = "rect"        
color = (255, 0, 0)      

drawing = False
start_pos = None

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

            if rect_btn.collidepoint(x, y): tool = "rect"
            elif circle_btn.collidepoint(x, y): tool = "circle"
            elif square_btn.collidepoint(x, y): tool = "square"
            elif tri_r_btn.collidepoint(x, y): tool = "tri_r"
            elif tri_e_btn.collidepoint(x, y): tool = "tri_e"
            elif rhomb_btn.collidepoint(x, y): tool = "rhomb"
            elif eraser_btn.collidepoint(x, y): tool = "eraser"

            elif red_btn.collidepoint(x, y): color = (255, 0, 0)
            elif yellow_btn.collidepoint(x, y): color = (255, 255, 0)
            elif blue_btn.collidepoint(x, y): color = (0, 0, 255)
            elif green_btn.collidepoint(x, y): color = (0, 255, 0)

            elif canvas_rect.collidepoint(x, y):
                drawing = True
                start_pos = (x - canvas_rect.x, y - canvas_rect.y)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                x, y = pygame.mouse.get_pos()
                end_pos = (x - canvas_rect.x, y - canvas_rect.y)

                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]

                if tool == "rect":
                    pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], dx, dy), 2)

                elif tool == "square":
                    size = min(abs(dx), abs(dy))
                    pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], size, size), 2)

                elif tool == "circle":
                    radius = int((dx**2 + dy**2) ** 0.5)
                    pygame.draw.circle(canvas, color, start_pos, radius, 2)

                elif tool == "tri_r":
                    pygame.draw.polygon(canvas, color, [
                        start_pos,
                        (start_pos[0], end_pos[1]),
                        end_pos
                    ], 2)

                elif tool == "tri_e":
                    size = abs(dx)
                    pygame.draw.polygon(canvas, color, [
                        (start_pos[0], start_pos[1]),
                        (start_pos[0] + size, start_pos[1]),
                        (start_pos[0] + size//2, start_pos[1] - size)
                    ], 2)

                elif tool == "rhomb":
                    cx, cy = start_pos
                    pygame.draw.polygon(canvas, color, [
                        (cx, cy - abs(dy)),
                        (cx + abs(dx), cy),
                        (cx, cy + abs(dy)),
                        (cx - abs(dx), cy)
                    ], 2)

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

    if drawing and tool != "eraser":
        x, y = pygame.mouse.get_pos()
        end_pos = (x - canvas_rect.x, y - canvas_rect.y)
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]

        if tool == "rect":
            pygame.draw.rect(preview, color, (start_pos[0], start_pos[1], dx, dy), 2)

        elif tool == "square":
            size = min(abs(dx), abs(dy))
            pygame.draw.rect(preview, color, (start_pos[0], start_pos[1], size, size), 2)

        elif tool == "circle":
            radius = int((dx**2 + dy**2) ** 0.5)
            pygame.draw.circle(preview, color, start_pos, radius, 2)

        elif tool == "tri_r":
            pygame.draw.polygon(preview, color, [
                start_pos,
                (start_pos[0], end_pos[1]),
                end_pos
            ], 2)

        elif tool == "tri_e":
            size = abs(dx)
            pygame.draw.polygon(preview, color, [
                (start_pos[0], start_pos[1]),
                (start_pos[0] + size, start_pos[1]),
                (start_pos[0] + size//2, start_pos[1] - size)
            ], 2)

        elif tool == "rhomb":
            cx, cy = start_pos
            pygame.draw.polygon(preview, color, [
                (cx, cy - abs(dy)),
                (cx + abs(dx), cy),
                (cx, cy + abs(dy)),
                (cx - abs(dx), cy)
            ], 2)

        screen.blit(preview, canvas_rect.topleft)

    if tool == "rect": pygame.draw.rect(screen, (0,0,0), rect_btn, 2)
    if tool == "circle": pygame.draw.rect(screen, (0,0,0), circle_btn, 2)
    if tool == "square": pygame.draw.rect(screen, (0,0,0), square_btn, 2)
    if tool == "tri_r": pygame.draw.rect(screen, (0,0,0), tri_r_btn, 2)
    if tool == "tri_e": pygame.draw.rect(screen, (0,0,0), tri_e_btn, 2)
    if tool == "rhomb": pygame.draw.rect(screen, (0,0,0), rhomb_btn, 2)
    if tool == "eraser": pygame.draw.rect(screen, (0,0,0), eraser_btn, 2)

    if color == (255, 0, 0): pygame.draw.rect(screen, (0,0,0), red_btn, 2)
    if color == (255, 255, 0): pygame.draw.rect(screen, (0,0,0), yellow_btn, 2)
    if color == (0, 0, 255): pygame.draw.rect(screen, (0,0,0), blue_btn, 2)
    if color == (0, 255, 0): pygame.draw.rect(screen, (0,0,0), green_btn, 2)

    pygame.display.flip()
    clock.tick(60)