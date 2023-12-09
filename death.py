import pygame
import ui_objects

class DeathScreen:

    def __init__(self, screen, fps, clock, respawnsending):
        self.screen = screen
        self.bckgroundImage = pygame.image.load("DEATH.png")
        self.fps = fps
        self.clock = clock
        self.change_scene_to = ""

        self.scene_change = False
        self.buttons(respawnsending)

    def buttons(self, respawnsending):
        self.respawn_button = ui_objects.Button(270, 490, 290, 100, sending = respawnsending)

    def gameloop(self, respawnsending):
        self.respawn_button.sending = respawnsending


        tick=self.clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if self.respawn_button.rect.collidepoint(event.pos):
                    print("clickonrespawnbutton")

                    self.scene_change = True
                    self.change_scene_to = self.respawn_button.sending

        self.screen.fill([0, 0, 0])
        self.screen.blit(self.bckgroundImage, [0, 0])
        pygame.draw.rect(self.screen, (0, 0, 0), self.respawn_button.rect)
        pygame.display.flip()
        self.clock.tick(self.fps)




























    pygame.quit()
if __name__=="__main__":
    gameloop()

