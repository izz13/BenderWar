import pygame

class Player:
    def __init__(self, hp, image, dmg, elmt):
        self.hp = hp
        self.dmg = dmg
        self.elmt = elmt
        self.image = pygame.image.load(image)
        self.x = 0
        self.y = 0
        self.rect = self.image.get_bounding_rect()
    def render(self, screen):
        self.rect.center.x = self.x
        self.rect.center.y = self.y
        screen.blit(self.image, self.rect)

    def update(self, screen):
        self.render(screen)
