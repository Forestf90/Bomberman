import pygame, sys
from player import Player

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

WINDOWWIDTH = 600
WINDOWHEIGHT = 600

TILEWIDTH = 20
TILEHEIGHT = 20

BACKGROUND = (107, 142, 35)

pygame.init()
s = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Bomberman')


clock = pygame.time.Clock()

player = Player()


def draw():
    s.fill(BACKGROUND)
    s.blit(player.animation[player.direction][player.frame],
           (player.posX*(TILEWIDTH/4), player.posY*(TILEHEIGHT/4), TILEWIDTH, TILEHEIGHT))

    pygame.display.update()


def main():
    while True:
        clock.tick(15)
        keys = pygame.key.get_pressed()

        temp = player.direction
        movement = False
        if keys[pygame.K_DOWN]:
            temp = 0
            player.posY += 1
            movement = True
        elif keys[pygame.K_RIGHT]:
            temp = 1
            player.posX += 1
            movement = True
        elif keys[pygame.K_UP]:
            temp = 2
            player.posY -= 1
            movement = True
        elif keys[pygame.K_LEFT]:
            temp = 3
            player.posX -= 1
            movement = True
        if temp != player.direction:
            player.frame = 0
            player.direction = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1
        draw()
        for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)


main()
