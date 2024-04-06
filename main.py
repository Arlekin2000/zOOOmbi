import pygame
from player import Player
from enemy import Enemy
from random import randint
from bullet import Bullet

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, randint(500, 1500))

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("zOOOmbi")
pygame.display.set_icon(pygame.image.load("titulimage.png"))
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

speed = 10
score = 0
level = 1

background = pygame.transform.scale(pygame.image.load("roud.jpg"), (800, 600))
player = Player()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def create_bullet(group):
    global level
    a, b = player.rect.center
    return Bullet(a + 50, b - 50, level, group)

def create_enemy(group):
    return Enemy(900, randint(400, 500), group)

def collide_enemy():
    global score
    for enemy in enemies:
        for bullet in bullets:
            if bullet.rect.colliderect(enemy.rect):
                enemy.health -= bullet.damage
                bullet.kill()
                print(bullet.damage)
                if enemy.health <= 0:
                    score += 1
                    enemy.kill()
        if player.rect.collidepoint(enemy.rect.center):
            score -= 10
            enemy.kill()

def level_up():
    global score, level
    if score >= 100:
        level = 2
    if score >= 200:
        level = 3
    if score >= 300:
        level = 4
    if score >= 400:
        level = 5


flDown = flLeft = flRight = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or score < 0:
            exit()
        elif event.type == pygame.USEREVENT:
            create_enemy(enemies)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                flLeft = True
            elif event.key == pygame.K_RIGHT:
                flRight = True
            elif event.key == pygame.K_UP:
                player.rect.top -= randint(100, 200)
            elif event.key == pygame.K_DOWN:
                flDown = True
            elif event.key == pygame.K_SPACE:
                create_bullet(bullets)
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                flDown = flLeft = flRight = False

    if flLeft:
        player.rect.left -= speed
    elif flRight:
        player.rect.right += speed
    elif flDown:
        player.rect.bottom += speed

    if player.rect.bottom < 500:
        player.rect.bottom += randint(5, 10)

    if player.rect.bottom >= 580:
        player.rect.bottom = 580
    if player.rect.top <= 100:
        player.rect.top = 100
    if player.rect.left <= 0:
        player.rect.left = 0
    if player.rect.right >= 800:
        player.rect.right = 800

    text = pygame.font.SysFont("Baby Kruffy", 48).render(f"Score {score}", True, (0, 0, 0))
    text_rect = text.get_rect(bottomright=(750, 580))
    text_level = pygame.font.SysFont("Baby Kruffy", 48).render(f"Level {level}", True, RED)
    text_level_rect = text_level.get_rect(center=(380, 30))

    level_up()
    collide_enemy()
    window.blit(background, (0, 0))
    window.blit(text_level, text_level_rect)
    window.blit(player.image, player.rect)
    enemies.draw(window)
    bullets.draw(window)
    window.blit(text, text_rect)
    pygame.display.update()
    enemies.update()
    bullets.update()

    clock.tick(60)