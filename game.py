import pygame

pygame.init()
win = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Project TDS')
run = True
fps = 60
#person
height = 25
width = 30
x = 640
y = 360
clock = pygame.time.Clock()

while run:
    clock.tick(fps)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    #controlers
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5
    if keys[pygame.K_UP]:
        y -= 5
    if keys[pygame.K_DOWN]:
        y += 5
    #drawing frames
    win.fill((0,0,0))
    pygame.draw.rect(win, (100,125,50), (x, y, width, height))
    pygame.display.update()