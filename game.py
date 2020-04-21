import pygame
import random

WIDTH = 1280
HEIGHT = 720
FPS = 60

# Создаем игру и окно
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project_TDS")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.speedy = -8
        if keys[pygame.K_DOWN]:
            self.speedy = 8
        if keys[pygame.K_LEFT]:
            self.speedx = -8
        if keys[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        self.rect.y += self.speedy


class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH)
        self.rect.y = 0 - self.rect.height
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        Player.__init__(self)
        self.image = pygame.Surface((10,10))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.speedy = 0
        self.rect.x = - 1000000
        self.rect.y = - 1110000
    def update(self):
        self.speedy = 30
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y
        self.rect.y -= self.speedy


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
bullet = Bullet()
all_sprites.add(player)
all_sprites.add(bullet)
for i in range(5):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)


running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #update
    all_sprites.update()

    #Render
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    #Flip
    pygame.display.flip()

pygame.quit()