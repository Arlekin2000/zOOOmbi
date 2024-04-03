import pygame


class Player:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("soldier.png"), (130, 180))
        self.rect = self.image.get_rect(center=(100, 400))