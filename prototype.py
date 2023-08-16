import pygame
import player

pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

green = (0, 255, 0)

playerEarthbender = player.Player(150, "EARTH.png", 40, "earth")
playerairbndr = player.Player(100, "airbender.png", 40, "air")

isRunning = True
while isRunning==True:
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            isRunning = False
    screen.fill(green)
    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
