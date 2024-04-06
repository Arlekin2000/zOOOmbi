import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, level, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 5))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 3
        if level == 1:
            self.damage = 100
        elif level == 2:
            self.damage = 80
        elif level == 3:
            self.damage = 60
        elif level >= 4:
            self.damage = 40
        elif level >= 5:
            self.damage = 20
        self.add(group)

    def update(self):
        if self.rect.x < 800:
            self.rect.x += self.speed
        else:
            self.kill()