
class Explosion:
    sectors = []

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 300
        self.frame = 0

    def explode(self, map):

        self.sectors.append([self.sourceX, self.sourceY])

        for x in range(1, self.range):
            if map[self.sourceX + x][self.sourceY] == 1:
                break
            elif map[self.sourceX+x][self.sourceY] == 0:
                self.sectors.append([self.sourceX+x, self.sourceY])
        for x in range(1, self.range):
            if map[self.sourceX - x][self.sourceY] == 1:
                break
            elif map[self.sourceX-x][self.sourceY] == 0:
                self.sectors.append([self.sourceX-x, self.sourceY])
        for x in range(1, self.range):
            if map[self.sourceX][self.sourceY + x] == 1:
                break
            elif map[self.sourceX][self.sourceY+x] == 0:
                self.sectors.append([self.sourceX, self.sourceY+x])
        for x in range(1, self.range):
            if map[self.sourceX][self.sourceY - x] == 1:
                break
            elif map[self.sourceX][self.sourceY-x] == 0:
                self.sectors.append([self.sourceX, self.sourceY-x])

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 100:
            self.frame = 2
        elif self.time < 200:
            self.frame = 1
