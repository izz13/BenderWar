import pygame
import player
from move import move


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
    print(bkrdpos)
    screen.blit(wtrbkrd, bkrdpos)
    player.update(screen, tick, hitObjects)

    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
