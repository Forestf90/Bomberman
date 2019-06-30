
class Explosion:
    sectors = []

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 300
        self.frame = 0

    def explode(self , map):

        self.sectors.append([self.sourceX, self.sourceY])