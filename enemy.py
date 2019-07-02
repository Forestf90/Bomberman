import pygame


class Enemy:
    posX = 4*11
    posY = 4*11
    direction = 0
    frame = 0
    animation = []
    range = 3
    bomb_limit = 1

    def __init__(self):
        self.life = True
        self.load_animations()

    def check_death(self, exp):

        for e in exp:
            for s in e.sectors:
                if int(self.posX/4) == s[0] and int(self.posY/4) == s[1]:
                    self.life = False

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
