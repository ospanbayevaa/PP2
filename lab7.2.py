import pygame
import os

pygame.init()


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Music Player")


player_image = pygame.image.load("music/image.png")
player_image = pygame.transform.scale(player_image, (800, 800))  


_songs = ['music/Diamonds.mp3', 'music/SM.mp3', 'music/Love The Way You Lie.mp3']
playing = False
currentSong = 0

def playMusic(n):
    pygame.mixer.music.load(_songs[n])
    pygame.mixer.music.play(0)

playMusic(currentSong)
pygame.mixer.music.pause()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True

            if event.key == pygame.K_RIGHT and currentSong < len(_songs) - 1:
                currentSong += 1
                playMusic(currentSong)
                playing = True
            if event.key == pygame.K_LEFT and currentSong > 0:
                currentSong -= 1
                playMusic(currentSong)
                playing = True

    screen.blit(player_image, (0, 0))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
