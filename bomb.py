class Bomb:
    frame = 0

    def __init__(self, r, x, y, map, bomber):
        self.range = r
        self.posX = x
        self.posY = y
        self.time = 3000
        self.bomber = bomber
        self.sectors = []
        self.get_range(map)

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 1000:
            self.frame = 2
        elif self.time < 2000:
            self.frame = 1

    def get_range(self, map):

        self.sectors.append([self.posX, self.posY])

        for x in range(1, self.range):
            if map[self.posX + x][self.posY] == 1:
                break
            elif map[self.posX+x][self.posY] == 0 or map[self.posX-x][self.posY] == 3:
                self.sectors.append([self.posX+x, self.posY])
            elif map[self.posX+x][self.posY] == 2:
                self.sectors.append([self.posX+x, self.posY])
                break
        for x in range(1, self.range):
            if map[self.posX - x][self.posY] == 1:
                break
            elif map[self.posX-x][self.posY] == 0 or map[self.posX-x][self.posY] == 3:
                self.sectors.append([self.posX-x, self.posY])
            elif map[self.posX-x][self.posY] == 2:
                self.sectors.append([self.posX-x, self.posY])
                break
        for x in range(1, self.range):
            if map[self.posX][self.posY + x] == 1:
                break
            elif map[self.posX][self.posY+x] == 0 or map[self.posX][self.posY+x] == 3:
                self.sectors.append([self.posX, self.posY+x])
            elif map[self.posX][self.posY+x] == 2:
                self.sectors.append([self.posX, self.posY+x])
                break
        for x in range(1, self.range):
            if map[self.posX][self.posY - x] == 1:
                break
            elif map[self.posX][self.posY-x] == 0 or map[self.posX][self.posY-x] == 3:
                self.sectors.append([self.posX, self.posY-x])
            elif map[self.posX][self.posY - x] == 2:
                self.sectors.append([self.posX, self.posY - x])
                break
