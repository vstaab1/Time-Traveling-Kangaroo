import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('image')
pygame.display.flip()
kangaroo1 = pygame.image.load('Kangaroo1.png').convert_alpha()
kangaroo1 = pygame.transform.scale(kangaroo1,(300,300))
kangaroo2 = pygame.image.load('Kangaroo2.png').convert_alpha()
kangaroo2 = pygame.transform.scale(kangaroo2, (300,300))
kangaroo3 = pygame.image.load('Kangaroo3.png').convert_alpha()
kangaroo3 = pygame.transform.scale(kangaroo3,(300,300))
kangaroo4 = pygame.image.load('Kangaroo4.png').convert_alpha()
kangaroo4 = pygame.transform.scale(kangaroo4, (300,300))
kangaroo5 = pygame.image.load('Kangaroo5.png').convert_alpha()
kangaroo5 = pygame.transform.scale(kangaroo5, (300,300))
def hopping(q):
    x = 40
    while x <= q:
        screen.fill([250, 204, 125])
        screen.blit(kangaroo1,(x,40))
        x += 30
        pygame.time.wait(1000)
        pygame.display.flip()
        pygame.display.update()
        screen.fill([250, 204, 125])
        screen.blit(kangaroo2,(x,40))
        x += 30
        pygame.time.wait(1000)
        pygame.display.flip()
        pygame.display.update()
        if x >= q:
            screen.fill([250, 204, 125])
            screen.blit(kangaroo1,(x,40))
            x += 30
            pygame.time.wait(1000)
            pygame.display.flip()
            pygame.display.update()
def flopping(q):
    x = 260
    screen.fill([250, 204, 125])
    screen.blit(kangaroo1,(x,40))
    x -= 15
    pygame.time.wait(500)
    pygame.display.flip()
    pygame.display.update()
    screen.fill([250, 204, 125])
    screen.blit(kangaroo3,(x,40))
    x -= 15
    pygame.time.wait(500)
    pygame.display.flip()
    pygame.display.update()
    screen.fill([250, 204, 125])
    screen.blit(kangaroo4,(x,40))
    x -= 15
    pygame.time.wait(500)
    pygame.display.flip()
    pygame.display.update()
    screen.fill([250, 204, 125])
    screen.blit(kangaroo5,(x,40))
    x -= 15
    pygame.time.wait(500)
    pygame.display.flip()
    pygame.display.update()
    while x >= q:
        screen.fill([250, 204, 125])
        screen.blit(kangaroo4,(x,40))
        x -= 30
        pygame.time.wait(500)
        pygame.display.flip()
        pygame.display.update()
        screen.fill([250, 204, 125])
        screen.blit(kangaroo5,(x,40))
        x -= 30
        pygame.time.wait(500)
        pygame.display.flip()
        pygame.display.update()
    if x <= q:
        screen.fill([250, 204, 125])
        screen.blit(kangaroo1,(x,40))
        x += 15
        pygame.time.wait(1000)
        pygame.display.flip()
        pygame.display.update()
flopping(70)
#flops 4
status = True
while (status):
    for i in pygame.event.get(): 
        if i.type == pygame.QUIT:
            status = False

