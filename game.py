import pygame
import time
import math
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

pygame.display.set_caption("Mickey Mouse Clock")

pygame.display.set_icon(pygame.image.load('images/icon.gif'))
leftarm = pygame.image.load('images/leftarm.png')
rightarm = pygame.image.load('images/rightarm.png')
mickeyclock = pygame.transform.scale(pygame.image.load('images/clock.png'), (800, 600))

running = True

while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec

    minute_angle = minute * 6 + (second / 60) * 6
    second_angle = second * 6

    screen.blit(mickeyclock, (0, 0))

    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (800, 600)), -minute_angle)
    rightarm_rect = rotated_rightarm.get_rect(center = (800 // 2, 600 // 2 + 12))
    screen.blit(rotated_rightarm, rightarm_rect)

    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarm_rect = rotated_leftarm.get_rect(center = (800 // 2, 600 // 2 + 10))
    screen.blit(rotated_leftarm, leftarm_rect)

    pygame.display.flip()
    clock.tick(60)

