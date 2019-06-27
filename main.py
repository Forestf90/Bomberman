import pygame, sys
from player import Player

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

WINDOWWIDTH = 600
WINDOWHEIGHT = 600

BACKGROUND = (107, 142, 35)

pygame.init()
s = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Bomberman')


clock = pygame.time.Clock()

player = Player()


def draw():
    s.fill(BACKGROUND)
    s.blit(player.frontAnimation[0], player.frontAnimation[0].get_rect())

    pygame.display.update()


def main():
    while True:
        clock.tick(20)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
           # if e.type == pygame.KEYDOWN:
                # if e.key == pygame.K_UP and pyton.kierunek != 1:
                #     pyton.kierunek = 3
                # elif e.key == pygame.K_DOWN and pyton.kierunek != 3:
                #     pyton.kierunek = 1
                # elif e.key == pygame.K_LEFT and pyton.kierunek != 2:
                #     pyton.kierunek = 0
                # elif e.key == pygame.K_RIGHT and pyton.kierunek != 0:
                #     pyton.kierunek = 2
        draw()


main()
