import pygame
from pygame.math import Vector2


pygame.mixer.init()

class Player:
    def __init__(self, hp, image, dmg, elmt, basic_attack_image, basicattacksound, prjctleatksnd, sprint=8, speed=4, basicattackcooldown=500, basicattackl=500):
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.sprint = sprint
        self.dmg = dmg
        self.elmt = elmt
        self.basic_attack_image = pygame.image.load(basic_attack_image)
        self.image = pygame.image.load(image)
        self.basicattacksound = pygame.mixer.Sound(basicattacksound)
        self.prjctleatksnd = pygame.mixer.Sound(prjctleatksnd)
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
        self.projattackcooldown = 750
        self.projattackl = 0
        self.projattacktimer = 0
        self.projattack = False
        self.healthRect = pygame.Rect(self.x-32, self.y-70, self.hp, 25)
        self.damageRect = pygame.Rect(self.x-32, self.y-70, self.max_hp, 25)
        self.projectiles = []
        self.proDamage = 3
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
        if self.x > 800-self.w:
           self.x = 800-self.w
        if self.y < 0:
            self.y = 0
        if self.y > 640-self.h:
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
        keys = objects.keys()
        for k in keys:
            hit = False
            for o in objects[k]:
                if attack_rect.colliderect(o.rect):
                    o.hp-=self.dmg
                    self.basicattack = False
                    self.basicattacktimer = 0
                    self.attacktimer = 0
                    hit = True
                    break
            if hit:
                break


        #pygame.draw.rect(screen, (255, 0, 0), attack_rect)

    def attack(self, screen, dt, objects):
        mouse_pos = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed()[0] and self.attack_timer >= self.basicattackcooldown:
            pygame.mixer.Sound.play(self.basicattacksound)
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
        if keys[pygame.K_q] and self.projattacktimer >= self.projattackcooldown:
            d = Vector2([mouse_pos[0]-self.x, mouse_pos[1]-self.y])
            self.projectiles.append(Projectile(self.x, self.y, 3, d, self.basic_attack_image, self.proDamage))
            self.projattacktimer = 0
        if self.projattacktimer < self.projattackcooldown:
            self.projattacktimer += dt

    def gothit(self, dmg):
        self.hp -= dmg


    def update(self, screen, dt, objects, vlx, vly):
        self.render(screen)
        self.attack(screen, dt, objects)
        for p in self.projectiles:
            if p.destroyed==True:
                self.projectiles.remove(p)
            p.update(screen, dt, vlx, vly, objects)

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

    def hit(self, objects):
        keys = objects.keys()
        for k in keys:
            hit = False
            for o in objects[k]:
                if self.rect.colliderect(o.rect):
                    o.hp-=self.dmg
                    self.destroyed = True
                    hit = True
                    break
            if hit:
                break


    def update(self, screen, dt, vlx, vly, objects):
        self.move()
        self.render(screen, vlx, vly)
        self.hit(objects)
        self.destroy(dt)




































































