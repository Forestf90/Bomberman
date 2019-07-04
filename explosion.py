
class Explosion:

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 300
        self.frame = 0
        self.sectors = []

    def explode(self, map, bombs, b):

        self.sectors.extend(b.sectors)
        bombs.remove(b)
        self.bomb_chain(bombs, map)

    def bomb_chain(self, bombs, map):

        for s in self.sectors:
            for x in bombs:
                if x.posX == s[0] and x.posY == s[1]:
                    # self.sourceX = x.posX
                    # self.sourceY = x.posY
                    # self.range = x.range
                    map[x.posX][x.posY] = 0
                    x.bomber.bomb_limit += 1
                    self.explode(map, bombs, x)

    def clear_sectors(self, map):

        for i in self.sectors:
            map[i[0]][i[1]] = 0

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 100:
            self.frame = 2
        elif self.time < 200:
            self.frame = 1
