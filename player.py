import pygame

class Player:
    def __init__(self, hp, image, dmg, elmt, speed = 3):
        self.hp = hp
        self.speed = speed
        self.dmg = dmg
        self.elmt = elmt
        self.image = pygame.image.load(image)
        self.x = 368
        self.y = 288
        self.w = 64
        self.h = 64
        self.rect = self.image.get_bounding_rect()
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x-=self.speed
        if keys[pygame.K_d]:
            self.x+=self.speed
        if keys[pygame.K_w]:
            self.y-=self.speed
        if keys[pygame.K_s]:
            self.y+=self.speed
        if self.x<0:
           self.x=0
        if self.x>800-self.w:
           self.x=800-self.w
        if self.y<0:
            self.y = 0
        if self.y>640-self.h:
            self.y = 640-self.h
    def update(self, screen):
        self.render(screen)
    #   self.move()
