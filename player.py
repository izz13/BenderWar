import pygame
from pygame.math import Vector2

class Player:
    def __init__(self, hp, image, dmg, elmt, basic_attack_image, sprint=8, speed=4, basicattackcooldown=500, basicattackl=500):
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.sprint = sprint
        self.dmg = dmg
        self.elmt = elmt
        self.basic_attack_image = pygame.image.load(basic_attack_image)
        self.image = pygame.image.load(image)
        self.x = 380
        self.y = 320
        self.w = 64
        self.h = 64
        self.rect = self.image.get_bounding_rect()
        self.attack_timer = 0
        self.basicattackcooldown = basicattackcooldown
        self.basicattackl = basicattackl
        self.basicattacktimer = 0
        self.basicattack = False
        self.healthRect = pygame.Rect(self.x-32, self.y-70, self.hp, 25)
        self.damageRect = pygame.Rect(self.x-32, self.y-70, self.max_hp, 25)
    def render(self, screen):
        self.rect.centerx = self.x
        self.rect.centery = self.y
        screen.blit(self.image, self.rect)
        self.healthRect.width = self.hp
        pygame.draw.rect(screen, (255, 0, 0), self.damageRect)
        pygame.draw.rect(screen, (0, 255, 0), self.healthRect)

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
    def basic_attack(self, pos, screen, objects):
        attack_rect = pygame.Rect(0, 0, 32, 32)
        x = pos[0]-self.x
        y = pos[1]-self.y
        direction = Vector2(x, y)
        direction = direction.normalize()
        direction.scale_to_length(50)
        attack_pos = (400+direction[0], 320+direction[1])
        attack_rect.center = attack_pos
        screen.blit(self.basic_attack_image, attack_rect)
        for object in objects:
            hit = False
            for i in object:
                if attack_rect.colliderect(i.rect):
                    i.hp-=self.dmg
                    hit = True
                    break
            if hit==True:
                break
        #pygame.draw.rect(screen, (255, 0, 0), attack_rect)

    def attack(self, screen, dt, objects):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.attack_timer >= self.basicattackcooldown:
            self.basicattack = True
            self.attack_timer = 0
        if self.basicattack == True:
            if self.basicattacktimer <= self.basicattackl:
                self.basicattacktimer += dt
                self.basic_attack(mouse_pos, screen, objects)
            else:
                self.basicattacktimer = 0
                self.basicattack = False
        if self.basicattack == False and self.attack_timer <= self.basicattackcooldown:
            self.attack_timer += dt
    def gothit(self, dmg):
        self.hp -= dmg


    def update(self, screen, dt, objects):
        self.render(screen)
        self.attack(screen, dt, objects)
