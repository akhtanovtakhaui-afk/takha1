import pygame
import sys
from clock import MickeyClock


pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

fps_clock = pygame.time.Clock()

mickey_clock = MickeyClock(
    400,
    300,
    "images/mickeyclock.jpeg"
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw(screen)

    pygame.display.flip()
    fps_clock.tick(1)

pygame.quit()
sys.exit()