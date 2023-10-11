import pygame
import player
import turret
from move import move
from random import randint

"""
Jayden's to-do list: 
2. make a counter for remaining turrets
"""


pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
textx = 0
texty = 0

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((textx, texty))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text surface object,
# on which text is drawn on it.

# create a rectangular object for the
# text surface object

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

for i in range(tn):
    hitObjects["turrets"].append(turret.Turret(randint(0, 2800), randint(0, 2240), randint(1, 120), "wtrtrt.png", "water", pimage="wtrwp.png"))
isRunning = True
while isRunning:
    tick = clock.get_time()
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
            tn -= 1
    text = font.render(str(tn), True, green)
    textRect = text.get_rect()
    textRect.center = (textx, texty)
    display_surface.blit(text, textRect.center)
    player.update(screen, tick, hitObjects)

    pygame.display.flip()
    clock.tick(fps)
pygame.quit()
