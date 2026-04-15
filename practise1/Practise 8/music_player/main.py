import pygame
import sys
from player import MusicPlayer


pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()

title_font = pygame.font.Font(None, 50)
text_font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 28)

playlist = [
    "music/track1.mp3.mp3",
    "music/track2.mp3.mp3"
]

player = MusicPlayer(playlist)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.previous_track()
            elif event.key == pygame.K_q:
                running = False

    screen.fill((240, 240, 240))

    title_text = title_font.render("Music Player", True, (0, 0, 0))
    track_text = text_font.render(
        f"Current track: {player.get_current_track_name()}",
        True,
        (0, 0, 0)
    )
    position_text = text_font.render(
        f"Playback position: {player.get_position_seconds()} sec",
        True,
        (0, 0, 0)
    )
    controls_text = small_font.render(
        "P = Play | S = Stop | N = Next | B = Previous | Q = Quit",
        True,
        (0, 0, 0)
    )

    screen.blit(title_text, (280, 50))
    screen.blit(track_text, (180, 150))
    screen.blit(position_text, (180, 210))
    screen.blit(controls_text, (90, 320))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()