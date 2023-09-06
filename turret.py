import pygame
import math

class Turret:
    def __init__(self, x, y, hp, image, elmt, attackRange=150):
        self.x = x
        self.y = y
        self.hp = hp
        self.image = pygame.image.load(image)
        self.elmt = elmt
        self.attackRange = attackRange
        self.rect = self.image.get_bounding_rect()
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image,self.rect)

    def distance(self, Px, Py):
        dx = Px-self.x
        dy = Py-self.y
        distance = math.sqrt(dx*dx+dy*dy)
        return distance

    def attack(self, px, py):
        if self.distance(px, py)<=self.attackRange:
            print("attacking")
    def update(self, screen, px, py):
        self.render(screen)
        self.attack(px, py)
