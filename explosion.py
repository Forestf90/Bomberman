
class Explosion:

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 300
        self.frame = 0
        self.sectors = []

    def explode(self, map, bombs):

        self.sectors.append([self.sourceX, self.sourceY])

        for x in range(1, self.range):
            if map[self.sourceX + x][self.sourceY] == 1:
                break
            elif map[self.sourceX+x][self.sourceY] == 0 or map[self.sourceX-x][self.sourceY] == 3:
                self.sectors.append([self.sourceX+x, self.sourceY])
            elif map[self.sourceX+x][self.sourceY] == 2:
                self.sectors.append([self.sourceX+x, self.sourceY])
                # map[self.sourceX+x][self.sourceY] = 0
                break
        for x in range(1, self.range):
            if map[self.sourceX - x][self.sourceY] == 1:
                break
            elif map[self.sourceX-x][self.sourceY] == 0 or map[self.sourceX-x][self.sourceY] == 3:
                self.sectors.append([self.sourceX-x, self.sourceY])
            elif map[self.sourceX-x][self.sourceY] == 2:
                self.sectors.append([self.sourceX-x, self.sourceY])
                # map[self.sourceX-x][self.sourceY] = 0
                break
        for x in range(1, self.range):
            if map[self.sourceX][self.sourceY + x] == 1:
                break
            elif map[self.sourceX][self.sourceY+x] == 0 or map[self.sourceX][self.sourceY+x] == 3:
                self.sectors.append([self.sourceX, self.sourceY+x])
            elif map[self.sourceX][self.sourceY+x] == 2:
                self.sectors.append([self.sourceX, self.sourceY+x])
                # map[self.sourceX][self.sourceY+x] = 0
                break
        for x in range(1, self.range):
            if map[self.sourceX][self.sourceY - x] == 1:
                break
            elif map[self.sourceX][self.sourceY-x] == 0 or map[self.sourceX][self.sourceY-x] == 3:
                self.sectors.append([self.sourceX, self.sourceY-x])
            elif map[self.sourceX][self.sourceY - x] == 2:
                self.sectors.append([self.sourceX, self.sourceY - x])
                # map[self.sourceX][self.sourceY - x] = 0
                break
        self.bomb_chain(bombs, map)

    def bomb_chain(self, bombs, map):

        for s in self.sectors:
            for x in bombs:
                if x.posX == s[0] and x.posY == s[1]:
                    self.sourceX = x.posX
                    self.sourceY = x.posY
                    self.range = x.range
                    map[x.posX][x.posY] = 0
                    bombs.remove(x)
                    self.explode(map, bombs)

    def clear_sectors(self, map):

        for i in self.sectors:
            map[i[0]][i[1]] = 0

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 100:
            self.frame = 2
        elif self.time < 200:
            self.frame = 1
