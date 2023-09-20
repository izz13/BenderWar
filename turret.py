import pygame
import math
from pygame.math import Vector2

class Turret:
    def __init__(self, x, y, hp, image, elmt, attackRange=450, pimage="airslash.png"):
        self.x = x
        self.y = y
        self.hp = hp
        self.image = pygame.image.load(image)
        self.elmt = elmt
        self.attackRange = attackRange
        self.rect = self.image.get_bounding_rect()
        self.projectiles = []
        self.cooldown = 0
        self.cooldownl = 10
        self.projectileimage = pygame.image.load(pimage)
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)

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
                self.projectiles.append(Projectile(self.x, self.y, 5, pdirection, self.projectileimage))
                self.cooldown = 0
    def update(self, screen, px, py):
        self.render(screen)
        self.attack(px, py)
        if len(self.projectiles) > 0:
            for p in self.projectiles:
                p.update(screen)
class Projectile:
    def __init__(self, x, y, speed, direction, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.image = image
        self.destroyed = False
    def render(self, screen):
        self.rect.center = [self.x, self.y]
        screen.blit(self.image,self.rect)
        #pygame.draw.rect(screen, [99, 66, 00], self.rect)
    def move(self):
        if self.direction.length() != 0:
            vel = self.direction.normalize()
            self.x += vel[0] * self.speed
            self.y += vel[1] * self.speed
    def destroy(self):

    def update(self, screen):
        self.move()
        self.render(screen)
