import pygame
import player

pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

green = (0, 255, 0)


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
