import pygame
"""
def gameloop():
    pygame.init()
    size = [800, 640]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    patchNotes = pygame.image.load("patch notes.png")



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
        screen.blit(patchNotes, bkrdpos)



        pygame.display.flip()
        clock.tick(fps)






"""




class PatchNotes:

    def __init__(self, screen, fps, clock):
        self.screen = screen
        self.bckgroundImage = pygame.image.load("patch_notes.png")
        self.fps = fps
        self.clock =clock

    def gameloop(self):


        tick=self.clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()

        self.screen.fill([0, 0, 0])
        self.screen.blit(self.bckgroundImage, [0, 0])
        pygame.display.flip()
        self.clock.tick(self.fps)








































