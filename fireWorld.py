#Eric's To Do List:
#1.draw art:(
#2.make pygame file for fire world:(
#3.make a for loop that adds 20 turrets to the turrets list at a random position:(
import pygame
import player
import turret
from random import randint
from move import move

"""
pygame.init()
size = [800, 640]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
"""
class FireWorld:
    def __init__(self, screen, fps, clock):
        self.screen = screen
        self.fps = fps
        self.clock = clock
        self.firbkrd = pygame.image.load("fireBackground.png")

        self.playerEarthbender = player.Player(150, "EARTH.png", 40, "earth", "EarthAttack.png", "rockatksnd.mp3", "rockatksnd.mp3")
        self.playerairbndr = player.Player(100, "airbender.png", 40, "air", "airslash.png", "airslash.mp3", "airslash.mp3")
        #self.playerwtrbndr = player.Player(100, "waterbender.png", 40, "water", "wtrwp.png", "wateratk.mp3", "wateratk.mp3")
        self.playerfireboonder = player.Player(90, "FireBender.png", 35, "fire", "FireAttack.png", "fireatksnd.mp3", "fireatksnd.mp3")
        self.player = self.playerfireboonder


        self.bkrdpos = [0,0]
        self.b_size = [2400, 1920]

        self.hitObjects = {
                "turrets": []
            }

        for i in range(20):
            self.hitObjects["turrets"].append(turret.Turret(randint(0,3200), randint(0,2560), randint(1,200), "fireTurret.png", "fire", self.b_size, pimage="fireturretAttack.png"))

    def gameloop(self):

        tick = self.clock.get_time()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        vlx, vly = move(self.player.speed, self.player.speed, self.b_size, self.bkrdpos)

        self.bkrdpos[0] += vlx
        self.bkrdpos[1] += vly
        #print(bkrdpos)
        self.screen.fill([0, 0, 0])
        self.screen.blit(self.firbkrd, self.bkrdpos)
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
            if turret.destroyed==True:
                self.hitObjects["turrets"].remove(turret)
        self.player.update(self.screen, tick, self.hitObjects, vlx, vly)


        pygame.display.flip()
        self.clock.tick(self.fps)




























pygame.quit()
