import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, hp, image, dmg, elmt, basic_attack_image, sprint = 8, speed = 4):
        self.hp = hp
        self.speed = speed
        self.sprint = sprint
        self.dmg = dmg
        self.elmt = elmt
        self.basic_attack_image = pygame.image.load(basic_attack_image)
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
    def basic_attack(self, pos, screen):
        attack_rect = pygame.Rect(0, 0, 32, 32)
        x = pos[0]-self.x
        y = pos[1]-self.y
        direction = Vector2(x, y)
        direction = direction.normalize()
        direction.scale_to_length(50)
        attack_pos = (400+direction[0], 320+direction[1])
        attack_rect.center = attack_pos
        pygame.draw.rect(screen, (255, 0, 0), attack_rect)

    def attack(self, screen):
        mouse_pos = (0, 0)
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            self.basic_attack(mouse_pos, screen)

    def update(self, screen):
        self.render(screen)
        self.attack(screen)
