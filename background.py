import pygame

class bg:
    def __init__(self, screen):
        self.screen = screen
        
        self.background1 = pygame.image.load("image/game_bg/background1.jpg").convert_alpha()
        self.background2 = pygame.image.load("image/game_bg/background2.png").convert_alpha()
        self.cloud1 = pygame.image.load("image/game_bg/cloud1.png").convert_alpha()
        self.cloud2 = pygame.image.load("image/game_bg/cloud2.png").convert_alpha()
        self.cloud3 = pygame.image.load("image/game_bg/cloud3.png").convert_alpha()

        self.pos1 = 400
        self.pos2 = 200
        self.pos3 = 10

        self.speed1 = 1
        self.speed2 = 0.75
        self.speed3 = 0.5

    def drawbackground(self):
        self.screen.blit(self.background1,(0, 0))
        self.screen.blit(self.cloud1,(self.pos1, 0))
        self.screen.blit(self.cloud2,(self.pos2, 0))
        self.screen.blit(self.cloud3,(self.pos3, 0))
        self.screen.blit(self.background2,(0, 0))
        self.pos1 += self.speed1
        self.pos2 += self.speed2
        self.pos3 += self.speed3
        if self.pos1 > 600:
            self.pos1 = -700
        if self.pos2 > 700:
            self.pos2 = -600
        if self.pos3 > 800:
            self.pos3 = -600