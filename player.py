import pygame

class Player:
    def __init__(self, hp, image, dmg, elmt):
        self.hp = hp
        self.dmg = dmg
        self.elmt = elmt
        self.image = pygame.image.load(image)
        self.x = 250
        self.y = 250
        self.rect = self.image.get_bounding_rect()
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)

    def update(self, screen):
        self.render(screen)
