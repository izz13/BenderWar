import pygame
from mainMenu import *
from patch_notes_1_0 import *
from fireWorld import *
from WaterWorld import *
from airlevel import *
from EarthWorld import *
from scry import *
from death import *


pygame.init()

screen = pygame.display.set_mode([800, 640])
clock = pygame.time.Clock()
fps = 60

mainmenu = MainMenu(screen, fps, clock)
patch_notes = PatchNotes(screen, fps, clock)

fireworld = FireWorld(screen, fps, clock)
waterworld = WaterWorld(screen, fps, clock)
airworld = AirWorld(screen, fps, clock)
earthworld = EarthWorld(screen, fps, clock)
scryworld = ScaryWorld(screen, fps, clock)
deathscreen = DeathScreen(screen, fps, clock, "")
respawnscene = ""

scene = "scaryworld"

while True:

    if scene=="mainmenu":
        mainmenu.gameloop()
        if mainmenu.scene_change:
            scene = mainmenu.change_scene_to
            mainmenu.scene_change = False
            mainmenu.change_scene_to = ""
    if scene=="patch_notes":
        patch_notes.gameloop()
    if scene == "fireworld":
        if respawnscene == fireworld.respawn:
            fireworld.setuplvl()
            respawnscene = ""
        fireworld.gameloop()
        if fireworld.scene_change:
            scene = fireworld.change_scene_to
            respawnscene = fireworld.respawn
            fireworld.scene_change = False
            fireworld.change_scene_to = ""
    if scene == "waterworld":
        if respawnscene == waterworld.respawn:
            waterworld.setuplvl()
            respawnscene = ""
        waterworld.gameloop()
        if waterworld.scene_change:
            scene = waterworld.change_scene_to
            respawnscene = waterworld.respawn
            waterworld.scene_change = False
            waterworld.change_scene_to = ""
    if scene == "airworld":
        if respawnscene == airworld.respawn:
            airworld.setuplvl()
            respawnscene = ""
        airworld.gameloop()
        if airworld.scene_change:
            scene = airworld.change_scene_to
            respawnscene = airworld.respawn
            airworld.scene_change = False
            airworld.change_scene_to = ""
    if scene == "earthworld":
        if respawnscene == earthworld.respawn:
            earthworld.setuplvl()
            respawnscene = ""
        earthworld.gameloop()
        if earthworld.scene_change:
            scene = earthworld.change_scene_to
            respawnscene = earthworld.respawn
            earthworld.scene_change = False
            earthworld.change_scene_to = ""
    if scene == "scaryworld":
        if respawnscene == scryworld.respawn:
            scryworld.setuplvl()
            respawnscene = ""
        scryworld.gameloop()
        if scryworld.scene_change:
            scene = scryworld.change_scene_to
            respawnscene = scryworld.respawn
            scryworld.scene_change = False
            scryworld.change_scene_to = ""
    if scene == "deathscreen":
        deathscreen.gameloop(respawnscene)
        if deathscreen.scene_change:
            scene = deathscreen.change_scene_to
            deathscreen.scene_change = False
            deathscreen.change_scene_to = ""

