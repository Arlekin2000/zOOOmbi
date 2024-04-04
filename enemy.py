import pygame
from random import uniform, randint, choice

class Enemy(pygame.sprite.Sprite):
    images = ["zomby1.png", "zomby2.png", "zomby3.png", "zomby4.png", "zomby5.png"]
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(choice(Enemy.images)).convert_alpha(), (120, 150))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = round(uniform(0.35, 0.90), 2)
        self.health = randint(100, 300)
        self.add(group)

    def update(self):
        if self.rect.x > 0 - 120:
            self.rect.x -= self.speed
        else:
            self.kill()
