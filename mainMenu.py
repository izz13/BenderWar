import pygame
import ui_objects

pygame.init()
"""
def gameloop():
    pygame.init()
    size = [800, 640]
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 60

    mainScreen = pygame.image.load("1.0_Halloween_TitleScreen.png")



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
        screen.blit(mainScreen, bkrdpos)



        pygame.display.flip()
        clock.tick(fps)


"""

class MainMenu:

    def __init__(self, screen, fps, clock):
        self.screen = screen
        self.bckgroundImage = pygame.image.load("1.0_Halloween_TitleScreen.png")
        self.fps = fps
        self.clock =clock
        self.change_scene_to = ""

        self.scene_change = False
        self.buttons()

    def buttons(self):
        self.patch_note_button = ui_objects.Button(300, 300, 50, 50, sending = "patch_notes")

    def gameloop(self):


        tick=self.clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if self.patch_note_button.rect.collidepoint(event.pos):
                    self.scene_change = True
                    self.change_scene_to = self.patch_note_button.sending

        self.screen.fill([0, 0, 0])
        self.screen.blit(self.bckgroundImage, [0, 0])
        pygame.draw.rect(self.screen, (0, 0, 0), self.patch_note_button.rect)
        pygame.display.flip()
        self.clock.tick(self.fps)























