#3
import pygame

pygame.init()

x, y = 500, 500
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("moving ball")

white = (255, 255, 255)
red = (255, 0, 0)

ball_radius = 25
ball_x = x // 2
ball_y = y // 2
step = 20

running = True
while running:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - ball_radius - step >= 0:
        ball_x -= step
    if keys[pygame.K_RIGHT] and ball_x + ball_radius + step <= x:
        ball_x += step
    if keys[pygame.K_UP] and ball_y - ball_radius - step >= 0:
        ball_y -= step
    if keys[pygame.K_DOWN] and ball_y + ball_radius + step <= y:
        ball_y += step

    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    pygame.time.delay(50)

pygame.quit()