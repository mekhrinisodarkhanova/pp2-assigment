import pygame
import datetime

right_hand = pygame.image.load("images/right_hand.png")
left_hand = pygame.image.load("images/left_hand.png")

right_hand = pygame.transform.scale(right_hand, (300, 300))
left_hand = pygame.transform.scale(left_hand, (300, 300))

def draw_clock(screen):
    screen.fill((255, 255, 255))

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