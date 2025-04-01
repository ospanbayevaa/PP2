import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

background = pygame.image.load('road.png')
player_image = pygame.image.load('player.png')
enemy_image = pygame.image.load('enemy.png')
coin_image = pygame.image.load('coin.png') # coin image
bitcoin_image = pygame.transform.scale(coin_image, (50, 50)) #scaling

background_music = pygame.mixer.music.load('background.mp3')
crash_sound = pygame.mixer.Sound('crash.mp3')
coin_sound = pygame.mixer.Sound('coin.sound.mp3') # coin sound

total_coins = 0 # number of collected coins

font = pygame.font.SysFont("Verdana", 60)
coin_font = pygame.font.SysFont("Verdana", 30)
game_over = font.render("Game Over", True, "white")

PLAYER_SPEED = 5
ENEMY_SPEED = 10  # increase enemy speed
COIN_SPEED = 15   # increase coin speed

pygame.mixer.music.play(-1)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.w // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.h

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-PLAYER_SPEED, 0) 
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(PLAYER_SPEED, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.generate_random_rect()

    def generate_random_rect(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.w)
        self.rect.bottom = 0

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.generate_random_rect()

class Coin(pygame.sprite.Sprite): # class coin
    def __init__(self):
        super().__init__()
        self.image = bitcoin_image
        self.rect = self.image.get_rect()
        self.generate_position()

    def generate_position(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.w)
        self.rect.bottom = 0
        self.value = random.choice([1, 2, 3])  

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.generate_position()

def distance(sprite1, sprite2):
    return ((sprite1.rect.centerx - sprite2.rect.centerx) ** 2 + 
            (sprite1.rect.centery - sprite2.rect.centery) ** 2) ** 0.5

player = Player()
enemy = Enemy()
coin = Coin() # coin object

all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy, coin)

enemy_sprites = pygame.sprite.Group()
enemy_sprites.add(enemy)

coins_sprites = pygame.sprite.Group()
coins_sprites.add(coin)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    player.move()
    enemy.move()
    coin.move()

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Collecting coins    
    if coin.rect.colliderect(player.rect):
        coin_sound.play()
        total_coins += coin.value  
        coin.generate_position()
        
        if total_coins % 5 == 0:
            ENEMY_SPEED += 3
    
    # Showing collected coins
    coin_text = coin_font.render(str(total_coins), True, "darkgoldenrod3")
    screen.blit(coin_text, (355, 0))

    # Game over check with distance calculation
    for enemy in enemy_sprites:
        if distance(player, enemy) < 35:  

            crash_sound.play()
            time.sleep(1)
            screen.fill("red")
            screen.blit(game_over, game_over.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            pygame.display.flip()
            time.sleep(2)
            running = False
            break
    
    pygame.display.flip()
    clock.tick(60)
