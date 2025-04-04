import pygame
import os
pygame.init()

music_folder = "musics"

playlist = [os.path.join(music_folder, song) for song in os.listdir(music_folder) if song.endswith(".mp3")]

screen = pygame.display.set_mode((590, 413))
clock = pygame.time.Clock()
pygame.display.set_caption("Music Player")

background = pygame.image.load(os.path.join("images", "background.jpg"))

controller = pygame.Surface((500,110))
controller.fill((255, 255, 255))
controller_pos = ((590 - 500) // 2, 413 - 110 - 10)

font = pygame.font.SysFont("lEMON MILK", 18)

play_button = pygame.image.load(os.path.join("images", "play.png"))
pause_button = pygame.image.load(os.path.join("images", "pause.png"))
next_button = pygame.image.load(os.path.join("images", "next.png"))
previous_button = pygame.image.load(os.path.join("images", "previous.png"))

play_button = pygame.transform.scale(play_button, (40, 40))
pause_button = pygame.transform.scale(pause_button, (40, 40))
next_button = pygame.transform.scale(next_button, (35, 35))
previous_button = pygame.transform.scale(previous_button, (35, 35))

index = 0
playing = False

pygame.mixer.music.load(playlist[index])
pygame.mixer.music.play(1)
playing = True

running = True

while running :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                if playing :
                    playing = False
                    pygame.mixer.music.pause()
                else :
                    playing = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT :
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT :
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

    screen.blit(background, (0, 0))
    screen.blit(controller, controller_pos)

    text = font.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    screen.blit(text, (590 // 2 - text.get_width() // 2, controller_pos[1] + 10))

    if playing:
        screen.blit(pause_button, (590 // 2 - 20, controller_pos[1] + 50))
    else:
        screen.blit(play_button, (590// 2 - 20, controller_pos[1] + 50))

    screen.blit(previous_button, (590 // 2 - 80, controller_pos[1] + 52))
    screen.blit(next_button, (590 // 2 + 50, controller_pos[1] + 54))

    clock.tick(30)
    pygame.display.update()