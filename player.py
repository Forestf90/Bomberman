import pygame

class Player:
    posX = 0
    posY = 0
    direction = 0
    frame = 0
    animation = []

    # frontAnimation = []
    # backAnimation = []
    # leftAnimation = []
    # rightAnimation = []
    # deathAnimation = []

    def __init__(self):
        self.load_animations()

    def load_animations(self):
        front = []
        back = []
        left = []
        right = []

        front.append(pygame.image.load('images/hero/pf0.png'))
        front.append(pygame.image.load('images/hero/pf1.png'))
        front.append(pygame.image.load('images/hero/pf2.png'))

        right.append(pygame.image.load('images/hero/pr0.png'))
        right.append(pygame.image.load('images/hero/pr1.png'))
        right.append(pygame.image.load('images/hero/pr2.png'))

        back.append(pygame.image.load('images/hero/pd0.png'))
        back.append(pygame.image.load('images/hero/pd1.png'))
        back.append(pygame.image.load('images/hero/pd2.png'))

        left.append(pygame.image.load('images/hero/pl0.png'))
        left.append(pygame.image.load('images/hero/pl1.png'))
        left.append(pygame.image.load('images/hero/pl2.png'))

        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)