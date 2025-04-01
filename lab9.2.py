import pygame
import time
import random

pygame.init()


WIDTH, HEIGHT = 600, 600
CELL = 30
LEVEL_UP_SCORE = 5  


screen = pygame.display.set_mode((WIDTH, HEIGHT))
message_font = pygame.font.SysFont("Verdana", 50)
ingame_font = pygame.font.SysFont("Verdana", 25)


def load_best_score():
    try:
        with open("best_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_best_score(score):
    with open("best_score.txt", "w") as file:
        file.write(str(score))

best_score = load_best_score()


def game_over(score):
    global running, best_score
    screen.fill("black")
    
    game_over_text = message_font.render("Game Over", True, "white")
    score_text = ingame_font.render(f"Score: {score}", True, "red")
    best_text = ingame_font.render(f"Best Score: {best_score}", True, "yellow")
    
    screen.blit(game_over_text, (170, 200))
    screen.blit(score_text, (220, 270))
    screen.blit(best_text, (200, 320))
    
    pygame.display.flip()
    time.sleep(3)
    running = False


def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, 'gray30', (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
    
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, 'orange', (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, 'yellow', (segment.x * CELL, segment.y * CELL, CELL, CELL))
    
    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += food.value
            food.spawn(self.body)
            last_segment = self.body[-1]
            self.body.append(Point(last_segment.x, last_segment.y))
    
    def check_self_collision(self):
        head = self.body[0]
        for segment in self.body[1:]:
            if head.x == segment.x and head.y == segment.y:
                game_over(self.score)

class Food:
    def __init__(self):
        self.spawn([])
        self.value = random.choice([1, 3, 5])
        self.timer = pygame.time.get_ticks()
    
    def spawn(self, snake_body):
        while True:
            new_pos = Point(random.randint(0, 19), random.randint(0, 19))
            if new_pos not in snake_body:
                self.pos = new_pos
                self.value = random.choice([1, 3, 5])
                self.timer = pygame.time.get_ticks()
                break
    
    def draw(self):
        colors = {1: 'red', 3: 'green', 5: 'blue'}
        pygame.draw.rect(screen, colors[self.value], (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class Obstacle:
    def __init__(self):
        self.body = []
    
    def spawn(self, level):
        self.body = []
        for _ in range(level - 1):
            while True:
                new_pos = Point(random.randint(0, 19), random.randint(0, 19))
                if new_pos not in snake.body and new_pos != food.pos:
                    self.body.append(new_pos)
                    break
    
    def draw(self):
        for obs in self.body:
            pygame.draw.rect(screen, 'white', (obs.x * CELL, obs.y * CELL, CELL, CELL))


FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
obstacle = Obstacle()
level = 1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    screen.fill('black')
    draw_grid()
    snake.move()
    snake.check_collision(food)
    snake.draw()
    food.draw()
    obstacle.draw()
    
    if snake.score >= level * LEVEL_UP_SCORE:
        level += 1
        FPS += 1
        obstacle.spawn(level)
    
    score_text = ingame_font.render(f"Score: {snake.score}", True, "green")
    level_text = ingame_font.render(f"Level: {level}", True, "white")
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))
    
    if snake.body[0] in obstacle.body:
        game_over(snake.score)
    
    snake.check_self_collision()
    pygame.display.flip()
    clock.tick(FPS)
    
    if snake.body[0].x < 0 or snake.body[0].x >= 20 or snake.body[0].y < 0 or snake.body[0].y >= 20:
        if snake.score > best_score:
            best_score = snake.score
            save_best_score(best_score)
        game_over(snake.score)

pygame.quit()