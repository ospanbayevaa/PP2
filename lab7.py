import pygame
import math
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey clock")


clock_face = pygame.image.load("mickeyclock.jpeg")
clock_face = pygame.transform.scale(clock_face, (400, 400))

minute_hand = pygame.image.load("righthand.png")
minute_hand = pygame.transform.scale(minute_hand, (30, 120))

second_hand = pygame.image.load("lefthand.png")
second_hand = pygame.transform.scale(second_hand, (20, 150))


center = (WIDTH // 2, HEIGHT // 2)

def draw_rotated_image(image, angle, pivot):
   
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_rect = rotated_image.get_rect(center=pivot)
    screen.blit(rotated_image, rotated_rect)

running = True
clock_tick = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    
    screen.blit(clock_face, (center[0] - 200, center[1] - 200))

    now = datetime.now()
    minute_angle = (360 / 60) * now.minute
    second_angle = (360 / 60) * now.second

    
    draw_rotated_image(minute_hand, minute_angle, center)
    draw_rotated_image(second_hand, second_angle, center)

    pygame.display.flip()
    clock_tick.tick(1)

pygame.quit()
