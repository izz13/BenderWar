import pygame

pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

isRunning = True
while isRunning==True:
    events = pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            isRunning = False
    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
