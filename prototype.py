import pygame
import player
import turret

pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

screenFill = (255, 255, 255)
blue = (0, 0, 255)
tlc = pygame.Rect(10, 10, 50, 50)
trc = pygame.Rect(740, 10, 50, 50)
blc = pygame.Rect(10, 580, 50, 50)
brc = pygame.Rect(740, 580, 50, 50)
objects = [tlc, trc, blc, brc]

playerEarthbender = player.Player(150, "EARTH.png", 40, "earth", "EarthAttack.png")
playerairbndr = player.Player(100, "airbender.png", 40, "air", "airslash.png")
playerwtrbndr = player.Player(100,"waterbender.png", 40, "water", "wtrwp.png")
playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttackA.png")
player = playerfireboonder
airtrt = turret.Turret(400, 580, 100, "airtrt.png", "air")
wtrtrt = turret.Turret(64, 320, 100, "wtrtrt.png", "water", pimage="wtrwp.png")
earthtrt = turret.Turret(800, 620, 100, "earthTurret.png", "earth", pimage="EarthturretAttack.png")
firetrt = turret.Turret(900, 790, 100, "fireTurret.png", "fire", pimage="fireturretAttack.png")

hitObjects = {
    "turrets": [airtrt, wtrtrt, firetrt, earthtrt]
}

def move(playervlx, playervly):
    keys = pygame.key.get_pressed()
    vlx = 0
    vly = 0
    if keys[pygame.K_d]:
        vlx=-playervlx
    if keys[pygame.K_a]:
        vlx=playervlx
    if keys[pygame.K_w]:
        vly=playervly
    if keys[pygame.K_s]:
        vly=-playervly
    if keys[pygame.K_LSHIFT]:
        if vlx!=0:
            vlx = vlx*2
        if vly!=0:
            vly = vly*2
    return vlx, vly

isRunning = True
while isRunning==True:
    tick=clock.get_time()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            isRunning = False
    screen.fill(screenFill)
    #move(objects, player.speed, player.speed, turrets)
    vlx, vly = move(player.speed, player.speed)
    for object in objects:
        object.x += vlx
        object.y += vly
        if object.x > 800-object.width:
            object.x=0
        if object.x < 0:
            object.x=800-object.width
        if object.y > 640-object.height:
            object.y=0
        if object.y < 0:
            object.y=640-object.height
    for object in objects:
        pygame.draw.rect(screen, blue, object)
    for turret in hitObjects["turrets"]:
        turret.update(screen, player.x, player.y, tick, player, vlx, vly)
    player.update(screen, tick, objects)
    if player.hp<=0:
        isRunning = False
    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
