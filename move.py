import pygame
import player

def move(playervlx, playervly, b_size, b_pos):
    keys = pygame.key.get_pressed()
    vlx = 0
    vly = 0
    if keys[pygame.K_d]:
        vlx=-playervlx
    if keys[pygame.K_a]:
        vlx=playervlx
    if keys[pygame.K_w]:
        vly=playervly
    if keys[pygame.K_s]:
        vly=-playervly
    if keys[pygame.K_LSHIFT]:
        if vlx!=0:
            vlx = vlx*2
        if vly!=0:
            vly = vly*2
    if b_pos[0]>0:

        vlx = -vlx
    if b_pos[1]>0:

        vly = -vly
    if b_pos[0]<-b_size[0]:

        vlx = -vlx
    if b_pos[1]<-b_size[1]:

        vly = -vly
    return vlx, vly
