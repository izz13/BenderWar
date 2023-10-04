import pygame
import player

def move(playervlx, playervly):
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
    return vlx, vly