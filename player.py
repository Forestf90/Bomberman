import pygame

class Player:
    posX=0
    posY=0
    direction=0
    frontAnimation =[]
    backAnimation =[]
    leftAnimation=[]
    rightAnimation=[]
    deathAnimation=[]

    def __init__(self):
        self.load_animations()

    def load_animations(self):
        self.frontAnimation.append(pygame.image.load('images/hero/pf0.png'))
        self.frontAnimation.append(pygame.image.load('images/hero/pf1.png'))
        self.frontAnimation.append(pygame.image.load('images/hero/pf2.png'))