import pygame, sys, random
from player import Player
from explosion import Explosion

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

TILEWIDTH = 40
TILEHEIGHT = 40

WINDOWWIDTH = 13*TILEWIDTH
WINDOWHEIGHT = 13*TILEHEIGHT

BACKGROUND = (107, 142, 35)

pygame.init()
s = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Bomberman')


clock = pygame.time.Clock()

player = Player()
bombs = []
explosions =[]

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

grass_img = pygame.image.load('images/terrain/grass.png')
grass_img = pygame.transform.scale(grass_img, (TILEWIDTH, TILEHEIGHT))

block_img = pygame.image.load('images/terrain/block.png')
block_img = pygame.transform.scale(block_img, (TILEWIDTH, TILEHEIGHT))

box_img = pygame.image.load('images/terrain/box.png')
box_img = pygame.transform.scale(box_img, (TILEWIDTH, TILEHEIGHT))

bomb1_img = pygame.image.load('images/bomb/1.png')
bomb1_img = pygame.transform.scale(bomb1_img, (TILEWIDTH, TILEHEIGHT))

bomb2_img = pygame.image.load('images/bomb/2.png')
bomb2_img = pygame.transform.scale(bomb2_img, (TILEWIDTH, TILEHEIGHT))

bomb3_img = pygame.image.load('images/bomb/3.png')
bomb3_img = pygame.transform.scale(bomb3_img, (TILEWIDTH, TILEHEIGHT))

explosion1_img = pygame.image.load('images/explosion/1.png')
explosion1_img = pygame.transform.scale(explosion1_img, (TILEWIDTH, TILEHEIGHT))

explosion2_img = pygame.image.load('images/explosion/2.png')
explosion2_img = pygame.transform.scale(explosion2_img, (TILEWIDTH, TILEHEIGHT))

explosion3_img = pygame.image.load('images/explosion/3.png')
explosion3_img = pygame.transform.scale(explosion3_img, (TILEWIDTH, TILEHEIGHT))

terrain_images = [grass_img, block_img, box_img, grass_img]
bomb_images = [bomb1_img, bomb2_img, bomb3_img]
explosion_images = [explosion1_img, explosion2_img, explosion3_img]


def draw():
    s.fill(BACKGROUND)
    for i in range(len(map)):
        for j in range(len(map[i])):
            #if map[i][j] != 0:
            s.blit(terrain_images[map[i][j]], (i*TILEWIDTH, j*TILEHEIGHT, TILEHEIGHT, TILEWIDTH))

    for x in bombs:
        s.blit(bomb_images[x.frame], (x.posX*TILEWIDTH, x.posY*TILEHEIGHT, TILEHEIGHT, TILEWIDTH))

    for y in explosions:
        for x in y.sectors:
            s.blit(explosion_images[y.frame], (x[0]*TILEWIDTH, x[1]*TILEHEIGHT, TILEHEIGHT, TILEWIDTH))

    s.blit(player.animation[player.direction][player.frame],
           (player.posX*(TILEWIDTH/4), player.posY*(TILEHEIGHT/4), TILEWIDTH, TILEHEIGHT))

    pygame.display.update()


def generate_map():

    for i in range(1, len(map)-1):
        for j in range(1, len(map[i])-1):
            if map[i][j] != 0:
                continue
            elif (i < 3 or i > len(map)-4) and (j < 3 or j > len(map[i])-4):
                continue
            if random.randint(0, 9) < 7:
                map[i][j] = 2

    return


def main():
    generate_map()
    while True:
        dt = clock.tick(15)
        keys = pygame.key.get_pressed()

        temp = player.direction
        movement = False
        if keys[pygame.K_DOWN]:
            temp = 0
            # player.posY += 1
            player.move(0, 1, map)
            movement = True
        elif keys[pygame.K_RIGHT]:
            temp = 1
            # player.posX += 1
            player.move(1, 0, map)
            movement = True
        elif keys[pygame.K_UP]:
            temp = 2
            # player.posY -= 1
            player.move(0, -1, map)
            movement = True
        elif keys[pygame.K_LEFT]:
            temp = 3
            # player.posX -= 1
            player.move(-1, 0, map)
            movement = True
        if temp != player.direction:
            player.frame = 0
            player.direction = temp
        if movement:
            if player.frame == 2:
                player.frame = 0
            else:
                player.frame += 1
        # if keys[pygame.K_SPACE]:
        #     temp_bomb = player.plant_bomb()
        #     bombs.append(temp_bomb)
        #     map[temp_bomb.posX][temp_bomb.posY] = 3

        draw()
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit(0)
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    temp_bomb = player.plant_bomb()
                    bombs.append(temp_bomb)
                    map[temp_bomb.posX][temp_bomb.posY] = 3

        for b in bombs:
            b.update(dt)
            if b.time < 1:
                map[b.posX][b.posY] = 0
                exp_temp = Explosion(b.posX, b.posY, b.range)
                bombs.remove(b)
                exp_temp.explode(map, bombs)
                explosions.append(exp_temp)
                
        for e in explosions:
            e.update(dt)
            if e.time < 1:
                explosions.remove(e)

main()
