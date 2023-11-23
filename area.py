import pygame

class Area:
    def __init__(self, top, left, side, name, own = 0, size = 0):
        self.top = top
        self.left = left
        self.side = side
        self.name = name
        self.own = own
        self.size = size
        self.area = pygame.Rect(self.top, self.left, self.side, self.side)
    
    def change(self, size, own):
        self.size = size
        self.own = own