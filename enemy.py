import pygame
from bomb import Bomb
from node import Node
from explosion import Explosion

class Enemy:
    posX = 4*11
    posY = 4*11
    direction = 0
    frame = 0
    animation = []
    range = 3
    bomb_limit = 1
    plant = False

    def __init__(self):
        self.life = True
        self.load_animations()
        self.path = []
        self.movment_path = []

    def move(self):

        if self.direction == 0:
            self.posY += 1
        elif self.direction == 1:
            self.posX += 1
        elif self.direction == 2:
            self.posY -= 1
        elif self.direction == 3:
            self.posX -= 1

        if self.posX % 4 == 0 and self.posY % 4 == 0:
            self.movment_path.pop(0)
            self.path.pop(0)
            # self.movment_path.clear()
            # self.path.clear()

        if self.frame == 2:
            self.frame = 0
        else:
            self.frame += 1

    def make_move(self, map, bombs, explosions, enemy):

        if not self.life:
            return
        if len(self.movment_path) == 0:
            # self.movment_path.clear()
            # self.path.clear()
            if self.plant:
                bombs.append(self.plant_bomb())
                self.plant = False
                map[int(self.posX/4)][int(self.posY/4)] = 3
            self.dfs(map, bombs, explosions, enemy)
        else:
            self.direction = self.movment_path[0]
            self.move()


    def plant_bomb(self):
        b = Bomb(self.range, round(self.posX/4), round(self.posY/4), self)
        self.bomb_limit -= 1
        return b

    def check_death(self, exp):

        for e in exp:
            for s in e.sectors:
                if int(self.posX/4) == s[0] and int(self.posY/4) == s[1]:
                    self.life = False

    def dfs(self, map, bombs, explosions, enemy):

        grid = []

        #0 - safe
        #1 - unsafe
        #2 - destryable
        #3 - unreachable
        for i in range(len(map)):
            grid.append([])
            for j in range(len(map[i])):
                if map[i][j] == 0:
                    grid[i].append(0)
                elif map[i][j] == 1:
                    grid[i].append(3)
                elif map[i][j] == 2:
                    grid[i].append(2)
                elif map[i][j] == 3:
                    grid[i].append(1) #3

        for b in bombs:
            temp_ex = Explosion(b.posX, b.posY, b.range)
            temp_ex.explode(map, bombs)

            for x in temp_ex.sectors:
                grid[x[0]][x[1]] = 1

        new_path = []
        new_path.append([int(self.posX/4), int(self.posY/4)])
        if self.bomb_limit == 0:
            self.dfs_rec(grid, 0, new_path)
        else:
            self.dfs_rec(grid, 2, new_path)

        self.path = new_path

    def dfs_rec(self, grid, end, path):

        last = path[-1]
        if grid[last[0]][last[1]] == 0 and end == 0:
            return
        elif end == 2:
            if grid[last[0] + 1][last[1]] == end or grid[last[0] - 1][last[1]] == end \
                    or grid[last[0]][last[1] + 1] == end \
                    or grid[last[0]][last[1] - 1] == end:
                if len(path) == 1 and end == 2:
                    self.plant = True
                return

        grid[last[0]][last[1]] = 9

        if grid[last[0] + 1][last[1]] == 0 or grid[last[0] + 1][last[1]] == 1:
            path.append([last[0] + 1, last[1]])
            self.movment_path.append(1)
        elif grid[last[0] - 1][last[1]] == 0 or grid[last[0] - 1][last[1]] == 1:
            path.append([last[0] - 1, last[1]])
            self.movment_path.append(3)
        elif grid[last[0]][last[1] + 1] == 0 or grid[last[0]][last[1] + 1] == 1:
            path.append([last[0], last[1] + 1])
            self.movment_path.append(0)
        elif grid[last[0]][last[1] - 1] == 0 or grid[last[0]][last[1] - 1] == 1:
            path.append([last[0], last[1] - 1])
            self.movment_path.append(2)

        self.dfs_rec(grid, end, path)

    def load_animations(self):
        front = []
        back = []
        left = []
        right = []
        resize_width = 40
        resize_height = 40
        en = '1'

        f1 = pygame.image.load('images/enemy/e'+en+'f0.png')
        f2 = pygame.image.load('images/enemy/e'+en+'f1.png')
        f3 = pygame.image.load('images/enemy/e'+en+'f2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load('images/enemy/e'+en+'r0.png')
        r2 = pygame.image.load('images/enemy/e'+en+'r1.png')
        r3 = pygame.image.load('images/enemy/e'+en+'r2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load('images/enemy/e'+en+'b0.png')
        b2 = pygame.image.load('images/enemy/e'+en+'b1.png')
        b3 = pygame.image.load('images/enemy/e'+en+'b2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load('images/enemy/e'+en+'l0.png')
        l2 = pygame.image.load('images/enemy/e'+en+'l1.png')
        l3 = pygame.image.load('images/enemy/e'+en+'l2.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))

        left.append(l1)
        left.append(l2)
        left.append(l3)

        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)
