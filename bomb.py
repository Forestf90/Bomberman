

class Bomb:
    frame = 0

    def __init__(self, r, x, y):
        self.range = r
        self.posX = x
        self.posY = y
        self.time = 3000

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 1000:
            self.frame = 2
        elif self.time < 2000:
            self.frame = 1
