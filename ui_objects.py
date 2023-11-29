import pygame
pygame.init()

class Button:
    def __init__(self, x, y, w, h, sending = ""):
        self.rect = pygame.Rect(x, y, w, h)
        self.sending = sending
