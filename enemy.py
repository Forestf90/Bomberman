import pygame, random
from bomb import Bomb
from node import Node
from explosion import Explosion
from algorithm import Algorithm


class Enemy:
    # posX = 4*11
    # posY = 4*11
    # direction = 0
    # frame = 0
    # animation = []
    # range = 3
    # bomb_limit = 1
    # plant = False
    dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]

    def __init__(self, x, y, alg):
        self.life = True
        self.path = []
        self.movement_path = []
        self.posX = x*4
        self.posY = y*4
        self.direction = 0
        self.frame = 0
        self.animation = []
        self.range = 3
        self.bomb_limit = 1
        self.plant = False
        self.algorithm =alg
        #self.load_animations(n)

    def move(self, map, bombs, explosions, enemy):

        if self.direction == 0:
            self.posY += 1
        elif self.direction == 1:
            self.posX += 1
        elif self.direction == 2:
            self.posY -= 1
        elif self.direction == 3:
            self.posX -= 1

        if self.posX % 4 == 0 and self.posY % 4 == 0:
            self.movement_path.pop(0)
            self.path.pop(0)
            if len(self.path) > 1:
                grid = self.create_grid(map, bombs, explosions, enemy)
                next = self.path[1]
                if grid[next[0]][next[1]] > 1:
                    self.movement_path.clear()
                    self.path.clear()

        if self.frame == 2:
            self.frame = 0
        else:
            self.frame += 1

    def make_move(self, map, bombs, explosions, enemy):

        if not self.life:
            return
        if len(self.movement_path) == 0:
            # self.movment_path.clear()
            # self.path.clear()
            if self.plant:
                bombs.append(self.plant_bomb(map))
                self.plant = False
                map[int(self.posX/4)][int(self.posY/4)] = 3
            if self.algorithm is Algorithm.DFS:
                self.dfs(self.create_grid(map, bombs, explosions, enemy))
            else:
                self.bfs(self.create_grid(map, bombs, explosions, enemy))

        else:
            self.direction = self.movement_path[0]
            self.move(map, bombs, explosions, enemy)

    def plant_bomb(self, map):
        b = Bomb(self.range, round(self.posX/4), round(self.posY/4), map, self)
        self.bomb_limit -= 1
        return b

    def check_death(self, exp):

        for e in exp:
            for s in e.sectors:
                if int(self.posX/4) == s[0] and int(self.posY/4) == s[1]:
                    self.life = False

    def dfs(self, grid):

        new_path = []
        new_path.append([int(self.posX/4), int(self.posY/4)])
        depth = 0
        if self.bomb_limit == 0:
            self.dfs_rec(grid, 0, new_path, depth)
        else:
            self.dfs_rec(grid, 2, new_path, depth)

        self.path = new_path

    def dfs_rec(self, grid, end, path, depth):

        last = path[-1]
        if depth > 200:
            return
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

        random.shuffle(self.dire)

        # safe
        if grid[last[0] + self.dire[0][0]][last[1] + self.dire[0][1]] == 0:
            path.append([last[0] + self.dire[0][0], last[1] + self.dire[0][1]])
            self.movement_path.append(self.dire[0][2])
        elif grid[last[0] + self.dire[1][0]][last[1] + self.dire[1][1]] == 0:
            path.append([last[0] + self.dire[1][0], last[1] + self.dire[1][1]])
            self.movement_path.append(self.dire[1][2])
        elif grid[last[0] + self.dire[2][0]][last[1] + self.dire[2][1]] == 0:
            path.append([last[0] + self.dire[2][0], last[1] + self.dire[2][1]])
            self.movement_path.append(self.dire[2][2])
        elif grid[last[0] + self.dire[3][0]][last[1] + self.dire[3][1]] == 0:
            path.append([last[0] + self.dire[3][0], last[1] + self.dire[3][1]])
            self.movement_path.append(self.dire[3][2])

          #unsafe
        elif grid[last[0] + self.dire[0][0]][last[1] + self.dire[0][1]] == 1:
            path.append([last[0] + self.dire[0][0], last[1] + self.dire[0][1]])
            self.movement_path.append(self.dire[0][2])
        elif grid[last[0] + self.dire[1][0]][last[1] + self.dire[1][1]] == 1:
            path.append([last[0] + self.dire[1][0], last[1] + self.dire[1][1]])
            self.movement_path.append(self.dire[1][2])
        elif grid[last[0] + self.dire[2][0]][last[1] + self.dire[2][1]] == 1:
            path.append([last[0] + self.dire[2][0], last[1] + self.dire[2][1]])
            self.movement_path.append(self.dire[2][2])
        elif grid[last[0] + self.dire[3][0]][last[1] + self.dire[3][1]] == 1:
            path.append([last[0] + self.dire[3][0], last[1] + self.dire[3][1]])
            self.movement_path.append(self.dire[3][2])
        else:
            if len(self.movement_path) > 0:
                path.pop(0)
                self.movement_path.pop(0)
        depth += 1
        self.dfs_rec(grid, end, path, depth)

    def bfs(self, grid):
        print('bfs')

        new_path = []
        new_path.append([int(self.posX/4), int(self.posY/4)])
        end = 2
        if self.bomb_limit == 0:
            end = 0

        self.path = new_path

    def create_grid(self, map, bombs, explosions, enemys):
        grid = [[0] * len(map) for r in range(len(map))]

        # 0 - safe
        # 1 - unsafe
        # 2 - destryable
        # 3 - unreachable

        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]] = 1
            grid[b.posX][b.posY] = 3

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]] = 3

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    grid[i][j] = 3
                elif map[i][j] == 2:
                    grid[i][j] = 2

        for x in enemys:
            if x == self:
                continue
            elif not x.life:
                continue
            else:
                grid[int(x.posX / 4)][int(x.posY / 4)] = 2

        return grid

    def load_animations(self, en, scale):
        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        image_path = 'images/enemy/e'
        if en == '':
            image_path = 'images/hero/p'

        f1 = pygame.image.load(image_path+en+'f0.png')
        f2 = pygame.image.load(image_path+en+'f1.png')
        f3 = pygame.image.load(image_path+en+'f2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load(image_path+en+'r0.png')
        r2 = pygame.image.load(image_path+en+'r1.png')
        r3 = pygame.image.load(image_path+en+'r2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load(image_path+en+'b0.png')
        b2 = pygame.image.load(image_path+en+'b1.png')
        b3 = pygame.image.load(image_path+en+'b2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load(image_path+en+'l0.png')
        l2 = pygame.image.load(image_path+en+'l1.png')
        l3 = pygame.image.load(image_path+en+'l2.png')

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
