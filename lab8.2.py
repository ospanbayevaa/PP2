import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((255, 255, 255))

colorRED, colorBLUE, colorWHITE, colorBLACK = (255, 0, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)
clock = pygame.time.Clock()

LMBpressed = False
THICKNESS = 5
THICKNESS_MIN, THICKNESS_MAX = 1, 20

prevX = prevY = currX = currY = 0
mode = "rect"
color = colorRED

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    center = ((x1 + x2) // 2, (y1 + y2) // 2)
    radius = max(abs(x2 - x1), abs(y2 - y1)) // 2
    return center, radius

def draw_by_mode():
    screen.blit(base_layer, (0, 0))
    if mode == "rect":
        pygame.draw.rect(screen, color, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
    elif mode == "circle":
        center, radius = calculate_circle(prevX, prevY, currX, currY)
        pygame.draw.circle(screen, color, center, radius, THICKNESS)

def erase(x, y):
    pygame.draw.circle(base_layer, (255, 255, 255), (x, y), THICKNESS)
    screen.blit(base_layer, (0, 0))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prevX, prevY = event.pos
        
        if event.type == pygame.MOUSEMOTION and LMBpressed:
            currX, currY = event.pos
            if mode in ["rect", "circle"]:
                draw_by_mode()
            elif mode == "eraser":
                erase(currX, currY)
        
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            currX, currY = event.pos
            if mode in ["rect", "circle"]:
                draw_by_mode()
                base_layer.blit(screen, (0, 0))
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "rect"
            if event.key == pygame.K_2:
                mode = "circle"
            if event.key == pygame.K_3:
                mode = "eraser"
            if event.key == pygame.K_r:
                color = colorRED
            if event.key == pygame.K_b:
                color = colorBLUE
            if event.key == pygame.K_w:
                color = colorWHITE
            if event.key == pygame.K_k:  # 'K' for black
                color = colorBLACK

            if event.key == pygame.K_EQUALS:
                THICKNESS = min(THICKNESS + 1, THICKNESS_MAX)
            if event.key == pygame.K_MINUS:
                THICKNESS = max(THICKNESS - 1, THICKNESS_MIN)
    
    pygame.display.flip()
    clock.tick(60)
