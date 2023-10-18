import pygame
import player
import turret
from move import move
from random import randint

"""
Jayden's to-do list: 
get started on coding the Air level
"""


pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

textx = 0
texty = 0
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
wtrbkrd = pygame.image.load("wtrbkgd.png")

playerEarthbender = player.Player(150, "EARTH.png", 40, "earth", "EarthAttack.png")
playerairbndr = player.Player(100, "airbender.png", 40, "air", "airslash.png")
playerwtrbndr = player.Player(100, "waterbender.png", 40, "water", "wtrwp.png")
playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttack.png")
player = playerfireboonder

bkrdpos = [0, 0]

hitObjects = {
    "turrets": []
}


tn = 20
b_size = [2400, 1920]

for i in range(tn):
    hitObjects["turrets"].append(turret.Turret(randint(0, 2800), randint(0, 2240), randint(1, 120), "wtrtrt.png", "water", b_size, pimage="wtrwp.png"))
isRunning = True
while isRunning:
    tick = clock.get_time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
    vlx, vly = move(player.speed, player.speed, b_size, bkrdpos)
    bkrdpos[0] += vlx
    bkrdpos[1] += vly
    screen.blit(wtrbkrd, bkrdpos)
    for turret in hitObjects["turrets"]:
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
        turret.update(screen, player.x, player.y, tick, player, vlx, vly)
        if turret.destroyed:
            hitObjects["turrets"].remove(turret)
            tn -= 1
    text = font.render(str(tn), True, green)
    textRect = text.get_rect()
    textRect.center = (textx, texty)
    screen.blit(text, textRect.center)
    player.update(screen, tick, hitObjects, vlx, vly)

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
