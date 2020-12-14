import pygame

pygame.init()

win = pygame.display.set_mode((640, 640))

bg = pygame.image.load('imgs/Chess_Board.png')

class redrawGameWindow():
    win.blit(bg, (0, 0))
    pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()

pygame.quit()
