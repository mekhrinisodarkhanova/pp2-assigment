import pygame
import datetime

background = pygame.image.load("images/clock.png")
right_hand = pygame.image.load("images/right_hand1.png")   
left_hand = pygame.image.load("images/left_hand1.png")     

background = pygame.transform.scale(background, (600, 600))
# right_hand = pygame.transform.scale(right_hand, (100, 100))
# left_hand = pygame.transform.scale(left_hand, (100, 100))


def draw_clock(screen):
    screen.blit(background, (0, 0))

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = minutes * 6
    second_angle = seconds * 6

    center = (300, 300)

    rotated_min = pygame.transform.rotate(right_hand, -minute_angle)
    rotated_sec = pygame.transform.rotate(left_hand, -second_angle)

    rect_min = rotated_min.get_rect(center=center)
    rect_sec = rotated_sec.get_rect(center=center)

    screen.blit(rotated_min, rect_min)
    screen.blit(rotated_sec, rect_sec)