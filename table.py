import pygame

def drawTable(screen, startpos, endpos, size , thick = 4, color = (66,66,66)):
    length = (endpos[0] - startpos[0]) / size
    for row in range(0,size+1):
        pygame.draw.line(screen, color, (startpos[0], startpos[1] + (row * length)),(endpos[0], startpos[1] + (row * length)),thick)
        pygame.draw.line(screen, color, (startpos[0] + (row * length), startpos[1]),(startpos[0] + (row * length), endpos[1]),thick)