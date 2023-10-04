import pygame
import player
import turret
from move import move
from random import randint

"""
Jayden's to-do list: 
1. make a for loop that make 20 turret objects with random pos
2. make a counter for remaining turrets
"""


pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

wtrbkrd = pygame.image.load("wtrbkgd.png")

playerEarthbender = player.Player(150, "EARTH.png", 40, "earth", "EarthAttack.png")
playerairbndr = player.Player(100, "airbender.png", 40, "air", "airslash.png")
playerwtrbndr = player.Player(100,"waterbender.png", 40, "water", "wtrwp.png")
playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttack.png")
player = playerfireboonder

bkrdpos = [0,0]

hitObjects = {
    "turrets": []
}

for i in range(20):
    hitObjects["turrets"].append(turret.Turret(randint(0,3200), randint(0,2560), randint(1,200), "wtrtrt.png", "water", pimage="wtrwp.png"))

isRunning = True
while isRunning==True:
    tick=clock.get_time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
    vlx, vly = move(player.speed, player.speed)
    if bkrdpos[0] > 0:
        bkrdpos[0] = 0
        vlx = 0
    if bkrdpos[1] > 0:
        bkrdpos[1] = 0
        vly = 0
    if bkrdpos[0] < -2400:
        bkrdpos[0] = -2400
        vlx = 0
    if bkrdpos[1] < -1920:
        bkrdpos[1] = -1920
        vly = 0
    bkrdpos[0] += vlx
    bkrdpos[1] += vly
    screen.blit(wtrbkrd, bkrdpos)
    for turret in hitObjects["turrets"]:
        turret.update(screen, player.x, player.y, tick, player, vlx, vly)
        if turret.destroyed:
            hitObjects["turrets"].remove(turret)
    player.update(screen, tick, hitObjects)

    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
