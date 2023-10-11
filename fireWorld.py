#Eric's To Do List:
#1.draw art:(
#2.make pygame file for fire world:(
#3.make a for loop that adds 20 turrets to the turrets list at a random position:(
import pygame
import player
import turret
from random import randint
from move import move


pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

firbkrd = pygame.image.load("fireBackground.png")

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
    hitObjects["turrets"].append(turret.Turret(randint(0,3200), randint(0,2560), randint(1,200), "fireTurret.png", "fire", pimage="fireturretAttack.png"))




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
    #print(bkrdpos)
    screen.blit(firbkrd, bkrdpos)
    for turret in hitObjects["turrets"]:
        turret.update(screen, player.x, player.y, tick, player, vlx, vly)
        if turret.destroyed==True:
            hitObjects["turrets"].remove(turret)
    player.update(screen, tick, hitObjectsw1    )


    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
