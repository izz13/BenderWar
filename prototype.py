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
playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttack.png")
player = playerfireboonder
airtrt = turret.Turret(400, 580, 100, "airtrt.png", "air")
wtrtrt = turret.Turret(64, 320, 100, "wtrtrt.png", "water", pimage="wtrwp.png")
earthtrt = turret.Turret(800, 620, 100, "earthTurret.png", "earth", pimage="EarthturretAttack.png")
firetrt = turret.Turret(900, 790, 100, "fireTurret.png", "fire", pimage="fireturretAttack.png")
commonGuard = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard1 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard2 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard3 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
threeshooter = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
threeshooter1 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
threeshooter2 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard4 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard5 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard6 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard7 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard8 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard9 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard10 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard11 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard12 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard13 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard14 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")
commonGuard15 = turret.Turret(100, 859, 100, "commonTurret.png", "common", pimage="commonAttack.png")

hitObjects = {"turrets": [airtrt, wtrtrt, firetrt, earthtrt, commonGuard, commonGuard1, commonGuard2, commonGuard3, threeshooter, threeshooter1, threeshooter2, commonGuard4, commonGuard5, commonGuard6, commonGuard7, commonGuard8, commonGuard9, commonGuard10, commonGuard11, commonGuard12, commonGuard13]}

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
        if turret.destroyed:
            hitObjects["turrets"].remove(turret)
    player.update(screen, tick, hitObjects)
    if player.hp<=0:
        isRunning = False
    pygame.display.flip()
    clock.tick(fps)




























pygame.quit()
