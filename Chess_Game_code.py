import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 900
clock = pygame.time.Clock()
#font = pygame.font.Font('freesansbold.ttf', 20)
#medium_font = pygame.font.Font('freesansbold.ttf', 40)
#big_font = pygame.font.Font('freesansbold.ttf', 50)


screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess Game')

clock.tick(60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()