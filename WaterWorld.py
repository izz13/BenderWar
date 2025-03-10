import pygame
import player
import turret
from move import move
from random import randint

"""
Jayden's to-do list: 
get started on coding the Air level
"""

"""
pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
"""
green = (0, 255, 0)
class WaterWorld:
    def __init__(self, screen, fps, clock):
        self.screen = screen
        self.fps = fps
        self.clock = clock
        self.textx = 0
        self.texty = 0
        pygame.display.set_caption('Show Text')
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.wtrbkrd = pygame.image.load("wtrbkgd.png")

        self.playerEarthbender = player.Player(150, "EARTH.png", 40, "earth", "EarthAttack.png", "rockatksnd.mp3", "rockatksnd.mp3")
        self.playerairbndr = player.Player(100, "airbender.png", 40, "air", "airslash.png", "airslash.mp3", "airslash.mp3")
        #playerwtrbndr = player.Player(100, "waterbender.png", 40, "water", "wtrwp.png", "wateratk.mp3", "wateratk.mp3")
        self.playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttack.png", "fireatksnd.mp3", "fireatksnd.mp3")
        self.player = self.playerfireboonder
        self.respawn = "waterworld"
        self.scene_change = False
        self.change_scene_to = ""

        self.bkrdpos = [0, 0]
        self.tn = 20
        self.b_size = [2400, 1920]
        self.setuplvl()

    def setuplvl(self):
        self.player.hp = self.player.max_hp
        self.hitObjects = {
            "turrets": []
        }

        for i in range(self.tn):
            self.hitObjects["turrets"].append(
                turret.Turret(randint(0, 3200), randint(0, 2560), randint(1, 200), "wtrtrt.png", "water",
            self.b_size, pimage="wtrwp.png"))
    def gameloop(self):
        tick = self.clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        vlx, vly = move(self.player.speed, self.player.speed, self.b_size, self.bkrdpos)
        self.bkrdpos[0] += vlx
        self.bkrdpos[1] += vly
        self.screen.blit(self.wtrbkrd, self.bkrdpos)
        if self.player.hp <= 0:
            self.scene_change = True
            self.change_scene_to = "deathscreen"
        for turret in self.hitObjects["turrets"]:
            if self.bkrdpos[0] > 0:
                self.bkrdpos[0] = 0
                vlx = 0
            if self.bkrdpos[1] > 0:
                self.bkrdpos[1] = 0
                vly = 0
            if self.bkrdpos[0] < -2400:
                self.bkrdpos[0] = -2400
                vlx = 0
            if self.bkrdpos[1] < -1920:
                self.bkrdpos[1] = -1920
                vly = 0
            turret.update(self.screen, self.player.x, self.player.y, tick, self.player, vlx, vly)
            if turret.destroyed:
                self.hitObjects["turrets"].remove(turret)
                self.tn -= 1
        text = self.font.render(str(self.tn), True, green)
        textRect = text.get_rect()
        textRect.center = (self.textx, self.texty)
        self.screen.blit(text, textRect.center)
        self.player.update(self.screen, tick, self.hitObjects, vlx, vly)

        pygame.display.flip()
        self.clock.tick(self.fps)
pygame.quit()
