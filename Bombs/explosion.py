class Explosion:

    bomber = None

    def __init__(self, x_pos, y_pos, range):
        self.sourceX = x_pos
        self.sourceY = y_pos
        self.range = range
        self.time = 400
        self.frame = 0
        self.sectors = []

    def explode(self, map, bombs, bomb):

        self.bomber = bomb.bomber
        self.sectors.extend(bomb.sectors)
        bombs.remove(bomb)
        self.bomb_chain(bombs, map)

    def bomb_chain(self, bombs, map):

        for s in self.sectors:
            for bomb in bombs:
                if bomb.posX == s[0] and bomb.posY == s[1]:

                    map[bomb.posX][bomb.posY] = 0
                    bomb.bomber.bomb_limit += 1
                    self.explode(map, bombs, bomb)

    def clear_sectors(self, map):

        for s in self.sectors:
            map[s[0]][s[1]] = 0

    def update(self, dt):
        self.time = self.time - dt

        if 200 < self.time <= 300:
            self.frame = 1
        elif 100 < self.time <= 200:
            self.frame = 2
        elif 50 < self.time <= 100:
            self.frame = 1
        else:
            self.frame = 0

