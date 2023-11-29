import pygame

def gameloop():
    pygame.init()
    size = [800, 640]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    helpScreen = pygame.image.load("help.png")



    bkrdpos = [0,0]
    b_size = [2400, 1920]



    isRunning = True
    while isRunning==True:
        tick=clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                isRunning = False

        screen.fill([0, 0, 0])
        screen.blit(helpScreen, bkrdpos)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__=="__main__":
    gameloop()
