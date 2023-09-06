import pygame

class Turret:
    def __init__(self, x, y, hp, image, elmt):
        self.x = x
        self.y = y
        self.hp = hp
        self.image = pygame.image.load(image)
        self.elmt = elmt
        self.rect = self.image.get_bounding_rect()
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image,self.rect)
    def update(self, screen):
        self.render(screen)