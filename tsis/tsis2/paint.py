import pygame
import sys
import datetime
from tools import flood_fill

pygame.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

background = pygame.image.load("assets/background.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

canvas_rect = pygame.Rect(180, 50, 500, 380)
canvas = pygame.Surface((canvas_rect.width, canvas_rect.height))
canvas.fill((255, 255, 255))

btn_w, btn_h = 55, 45
gap = 8
x1, x2 = 20, 85
y = 40

tools_list = [
    "rect","circle","square","tri_r","tri_e",
    "rhomb","pencil","line","fill","eraser"
]

tools_btn = {}
for i, name in enumerate(tools_list):
    col = i % 2
    row = i // 2
    tools_btn[name] = pygame.Rect(
        x1 if col == 0 else x2,
        y + row * (btn_h + gap),
        btn_w,
        btn_h
    )

color_btn = {
    "red": pygame.Rect(20, 340, 30, 30),
    "yellow": pygame.Rect(55, 340, 30, 30),
    "blue": pygame.Rect(90, 340, 30, 30),
    "green": pygame.Rect(125, 340, 30, 30)
}

size_btn = {
    2: pygame.Rect(20, 390, 30, 30),
    5: pygame.Rect(55, 390, 30, 30),
    10: pygame.Rect(90, 390, 30, 30)
}

tool = "rect"
color = (255, 0, 0)
size = 2

drawing = False
start_pos = None

clock = pygame.time.Clock()

while True:
    screen.blit(background, (0, 0))

    preview = canvas.copy()

    if drawing:
        mx, my = pygame.mouse.get_pos()
        end_pos = (mx - canvas_rect.x, my - canvas_rect.y)

        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]

        if tool == "rect":
            pygame.draw.rect(preview, color, (*start_pos, dx, dy), size)

        elif tool == "square":
            s = min(abs(dx), abs(dy))
            pygame.draw.rect(preview, color, (*start_pos, s, s), size)

        elif tool == "circle":
            r = int((dx**2 + dy**2)**0.5)
            pygame.draw.circle(preview, color, start_pos, r, size)

        elif tool == "tri_r":
            pygame.draw.polygon(preview, color,
                [start_pos, (start_pos[0], end_pos[1]), end_pos], size)

        elif tool == "tri_e":
            s = abs(dx)
            pygame.draw.polygon(preview, color,
                [(start_pos[0], start_pos[1]),
                 (start_pos[0] + s, start_pos[1]),
                 (start_pos[0] + s//2, start_pos[1] - s)], size)

        elif tool == "rhomb":
            cx, cy = start_pos
            pygame.draw.polygon(preview, color,
                [(cx, cy - abs(dy)), (cx + abs(dx), cy),
                 (cx, cy + abs(dy)), (cx - abs(dx), cy)], size)

        elif tool == "line":
            pygame.draw.line(preview, color, start_pos, end_pos, size)

    screen.blit(preview, canvas_rect.topleft)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # СОХРАНЕНИЕ
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
                pygame.image.save(canvas, filename)
                print("Saved:", filename)

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

            # инструменты
            for name, rect in tools_btn.items():
                if rect.collidepoint(x, y):
                    tool = name

            # цвета
            if color_btn["red"].collidepoint(x,y): color=(255,0,0)
            if color_btn["yellow"].collidepoint(x,y): color=(255,255,0)
            if color_btn["blue"].collidepoint(x,y): color=(0,0,255)
            if color_btn["green"].collidepoint(x,y): color=(0,255,0)

            # толщина
            for s, rect in size_btn.items():
                if rect.collidepoint(x, y):
                    size = s

            if canvas_rect.collidepoint(x, y):
                cx, cy = x - canvas_rect.x, y - canvas_rect.y

                if tool == "fill":
                    flood_fill(canvas, cx, cy, color)
                else:
                    drawing = True
                    start_pos = (cx, cy)

        if event.type == pygame.MOUSEBUTTONUP:
            if drawing:
                mx, my = pygame.mouse.get_pos()
                end_pos = (mx - canvas_rect.x, my - canvas_rect.y)

                dx = end_pos[0] - start_pos[0]
                dy = end_pos[1] - start_pos[1]

                if tool == "rect":
                    pygame.draw.rect(canvas, color, (*start_pos, dx, dy), size)

                elif tool == "square":
                    s = min(abs(dx), abs(dy))
                    pygame.draw.rect(canvas, color, (*start_pos, s, s), size)

                elif tool == "circle":
                    r = int((dx**2 + dy**2)**0.5)
                    pygame.draw.circle(canvas, color, start_pos, r, size)

                elif tool == "tri_r":
                    pygame.draw.polygon(canvas, color,
                        [start_pos,(start_pos[0], end_pos[1]),end_pos], size)

                elif tool == "tri_e":
                    s = abs(dx)
                    pygame.draw.polygon(canvas, color,
                        [(start_pos[0],start_pos[1]),
                         (start_pos[0]+s,start_pos[1]),
                         (start_pos[0]+s//2,start_pos[1]-s)], size)

                elif tool == "rhomb":
                    cx, cy = start_pos
                    pygame.draw.polygon(canvas, color,
                        [(cx,cy-abs(dy)),(cx+abs(dx),cy),
                         (cx,cy+abs(dy)),(cx-abs(dx),cy)], size)

                elif tool == "line":
                    pygame.draw.line(canvas, color, start_pos, end_pos, size)

                drawing = False

        if event.type == pygame.MOUSEMOTION:
            if drawing:
                mx, my = event.pos
                cx, cy = mx - canvas_rect.x, my - canvas_rect.y

                if tool == "pencil":
                    pygame.draw.line(canvas, color, start_pos, (cx, cy), size)
                    start_pos = (cx, cy)

                elif tool == "eraser":
                    pygame.draw.circle(canvas, (255,255,255), (cx, cy), size*2)

    for name, rect in tools_btn.items():
        if tool == name:
            pygame.draw.rect(screen, (0,0,0), rect, 2)

    if color == (255,0,0): pygame.draw.rect(screen,(0,0,0),color_btn["red"],2)
    if color == (255,255,0): pygame.draw.rect(screen,(0,0,0),color_btn["yellow"],2)
    if color == (0,0,255): pygame.draw.rect(screen,(0,0,0),color_btn["blue"],2)
    if color == (0,255,0): pygame.draw.rect(screen,(0,0,0),color_btn["green"],2)

    for s, rect in size_btn.items():
        if size == s:
            pygame.draw.rect(screen, (0,0,0), rect, 2)

    pygame.display.flip()
    clock.tick(60)