import pygame

class Player:
    def __init__(self, hp, image, dmg, elmt):
        self.hp = hp
        self.dmg = dmg
        self.elmt = elmt
        self.image = pygame.image.load(image)