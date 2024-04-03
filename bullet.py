import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        self.add(group)

    def update(self):
        if self.rect.x < 800:
            self.rect.x += self.speed
        else:
            self.kill()