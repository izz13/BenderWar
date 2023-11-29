import pygame
from mainMenu import *
from patch_notes_1_0 import *

pygame.init()

screen = pygame.display.set_mode([800, 640])
clock = pygame.time.Clock()
fps = 60

mainmenu = MainMenu(screen, fps, clock)
patch_notes = PatchNotes(screen, fps, clock)

scene = "mainmenu"

while True:

    if scene=="mainmenu":
        mainmenu.gameloop()
        if mainmenu.scene_change:
            scene = mainmenu.change_scene_to
            mainmenu.scene_change = False
            mainmenu.change_scene_to = ""
    if scene=="patch_notes":
        patch_notes.gameloop()

