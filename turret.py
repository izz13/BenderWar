import pygame
import math
from random import randint
from pygame.math import Vector2

class Turret:
    def __init__(self, x, y, hp, image, elmt, b_size, attackRange=450, pimage="airslash.png"):
        self.x = x
        self.y = y
        self.startx = x
        self.starty = y
        self.hp = hp
        self.image = pygame.image.load(image)
        self.elmt = elmt
        self.attackRange = attackRange
        self.rect = self.image.get_bounding_rect()
        self.projectiles = []
        self.cooldown = 0
        self.cooldownl = 50
        self.projectileimage = pygame.image.load(pimage)
        self.max_hp = hp
        self.healthRect = pygame.Rect(self.x-32, self.y-70, self.hp, 25)
        self.damageRect = pygame.Rect(self.x-32, self.y-70, self.max_hp, 25)
        self.destroyed = False
        self.b_size = b_size
        self.edgepos = [b_size[0]-self.x, b_size[1]-self.y]


    def render(self, screen, vlx, vly):
        self.x += vlx
        self.y += vly
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.healthRect.width = self.hp
        self.damageRect.x += vlx
        self.damageRect.y += vly
        self.healthRect.x += vlx
        self.healthRect.y += vly
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (255, 0, 0), self.damageRect)
        pygame.draw.rect(screen, (0, 255, 0), self.healthRect)


    def distance(self, Px, Py):
        dx = Px-self.x
        dy = Py-self.y
        distance = math.sqrt(dx*dx+dy*dy)
        return distance, dx, dy

    def attack(self, px, py):
        d, dx, dy = self.distance(px, py)
        if d <= self.attackRange:
            if self.cooldown < self.cooldownl:
                self.cooldown += 1
            else:
                pdirection = Vector2(dx, dy)
                self.projectiles.append(Projectile(self.x, self.y,5, pdirection, self.projectileimage, 5))
                self.cooldown = 0

    def destroy(self):
        if self.hp <=0:
            self.destroyed = True
    def update(self, screen, px, py, dt, player, vlx, vly):
        self.render(screen, vlx, vly)
        self.attack(px, py)
        if len(self.projectiles) > 0:
            for p in self.projectiles:
                p.update(screen, dt, player, vlx, vly)
                if p.destroyed:
                    self.projectiles.remove(p)
        self.destroy()
class Projectile:
    def __init__(self, x, y, speed, direction, image, dmg):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.image = image
        self.destroyed = False
        self.timer = 0
        self.timerl = 10000
        self.dmg = dmg
    def render(self, screen, vlx, vly):
        self.x += vlx
        self.y += vly
        self.rect.center = [self.x, self.y]
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen, [99, 66, 00], self.rect)
    def move(self):
        if self.direction.length() != 0:
            vel = self.direction.normalize()
            self.x += vel[0] * self.speed
            self.y += vel[1] * self.speed
    def destroy(self, dt):

        if self.timer >= self.timerl:
            self.destroyed = True
        else:
            self.timer += dt
    def hitplayer(self, player):
        if self.rect.colliderect(player.rect):
            player.gothit(self.dmg)
            self.destroyed = True

    def gothit(self, dmg):
        self.hp -= dmg

    def update(self, screen, dt, player, vlx, vly):
        self.move()
        self.render(screen, vlx, vly)
        self.destroy(dt)
        self.hitplayer(player)

class Necromancer(Turret):
    def __init__(self, x, y, hp, image, elmt, b_size, attackRange=450, pimage="airslash.png"):
        super().__init__(x, y, hp, image, elmt, b_size, attackRange, pimage)
        self.spawn = False
        self.spawnrange = 100
        self.spawntimer = 0
        self.spawnl = 200
    def spawnskeleton(self):
        return Skeleton(self.x+randint(-self.spawnrange, self.spawnrange), self.y+randint(-self.spawnrange, self.spawnrange), 5, "skltn.png", "skltn", self.b_size)

    def spawner(self):
        if self.spawntimer >= self.spawnl:
            self.spawn = True
            self.spawntimer = 0
        elif self.spawn == False:
            self.spawntimer += 1
    def update(self, screen, px, py, dt, player, vlx, vly):
        self.render(screen, vlx, vly)
        self.spawner()
        self.destroy()




class Skeleton(Turret):
    def __init__(self, x, y, hp, image, elmt, b_size, attackRange=450, pimage="bnetrw.png"):
        super().__init__(x, y, hp, image, elmt, b_size, attackRange, pimage)
        self.fkedstryd = pygame.image.load("deadskltn.png")
        self.rsrctd = pygame.image.load("bknskltn.png")
        self.rsrcttimer = 0
        self.rsrctl = 1000
        self.rsrctusd = False
    def destroy(self, dt):
        if self.hp <=0:
            if self.rsrctusd != True:
                if self.rsrcttimer < self.rsrctl:
                    self.rsrcttimer += dt
                    self.image = self.fkedstryd
                else:
                    self.image = self.rsrctd
                    self.hp = self.max_hp
                    self.rsrcttimer = 0
                    self.rsrctusd = True
            else:
                self.destroyed = True

    def update(self, screen, px, py, dt, player, vlx, vly):
        self.render(screen, vlx, vly)
        self.attack(px, py)
        if len(self.projectiles) > 0:
            for p in self.projectiles:
                p.update(screen, dt, player, vlx, vly)
                if p.destroyed:
                    self.projectiles.remove(p)
        self.destroy(dt)