import pygame
import copy
import random
import save
from table import drawTable
from load_all_image import loading
from player import player
from area import Area
from winner import checkwin
from button import button
from background import bg

pygame.init()

WIDTH, HEIGHT = 800,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("yummy eddy")
clock = pygame.time.Clock()

pygame.mixer.music.load("sound/bg.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
pickup = pygame.mixer.Sound("sound/pickup.mp3")
pygame.mixer.Sound.set_volume(pickup, 1)
drop = pygame.mixer.Sound("sound/drop.mp3")
pygame.mixer.Sound.set_volume(drop, 0.1)
victory = pygame.mixer.Sound("sound/victory.mp3")
pygame.mixer.Sound.set_volume(victory, 0.05)

BOARD_SIZE = 5
STARTPOS = (151, 121)
ENDPOS = (650, 620)
LENGTH = (ENDPOS[0] - STARTPOS[0]) / BOARD_SIZE
BUTTONPOS = 0

scene = "mainmenu"
FPS = 60

font = pygame.font.Font("font/Pixeltype.ttf", 72)
fontcount = pygame.font.Font(None, 24)

background = bg(screen)
main_img = pygame.image.load("image/game_bg/home.png").convert_alpha()
pinkwin = pygame.image.load("image/game_bg/pink win.png").convert_alpha()
yellowwin = pygame.image.load("image/game_bg/yellow win.png").convert_alpha()
pink = pygame.image.load("image/game_bg/pink.png").convert_alpha()
yellow = pygame.image.load("image/game_bg/yellow.png").convert_alpha()
draw_img = pygame.image.load("image/game_bg/draw.png").convert_alpha()
draw_bg = pygame.image.load("image/game_bg/drawbg.png").convert_alpha()

arrow = pygame.image.load("image/arrow.png").convert_alpha()
arrowLeft = pygame.transform.scale(arrow, (150, 70))
arrowRight = pygame.transform.flip(arrowLeft, True, False)
play_img = pygame.image.load("image/button/play.png").convert_alpha()
load_img = pygame.image.load("image/button/load.png").convert_alpha()
exit_img = pygame.image.load("image/button/exit.png").convert_alpha()
home_img = pygame.image.load("image/button/home.png").convert_alpha()
resume_img = pygame.image.load("image/button/resume.png").convert_alpha()
save_img = pygame.image.load("image/button/save.png").convert_alpha()
mainmenu_img = pygame.image.load("image/button/mainmenu.png").convert_alpha()
playagain_img = pygame.image.load("image/button/playagain.png").convert_alpha()

play_button = button(screen, 400, 260, play_img, 0.9)
loadgame_button = button(screen, 400, 360, load_img, 0.9)
exit_button = button(screen, 400, 460, exit_img, 0.9)
resume_button = button(screen, 400, 260, resume_img, 0.9)
savegame_button = button(screen, 400, 360, save_img, 0.9)
mainmenu_button = button(screen, 400, 460, mainmenu_img, 0.9)
home_button = button(screen, 760, 35, home_img)
playagain_button = button(screen, 400, 550, playagain_img, 0.9)

def setup():
    global area, area_name, table, Char, win, draw, winsound
    area = []
    area_name = 1
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            area.append(Area(STARTPOS[0] + x * LENGTH, STARTPOS[1] + y * LENGTH, LENGTH, area_name))
            area_name += 1

    table = {}
    Char = [[],[]]
    for x in loading("image/p1"):
        Char[0].append(player(screen, fontcount, x, 50 - len(Char[0]) * 4, 595 - len(Char[0]) * 100, 1))
    for x in loading("image/p2"):
        Char[1].append(player(screen, fontcount, x, 700 - len(Char[1]) * 4, 595 - len(Char[1]) * 100, 2))

    win = 0
    draw = 0
    winsound = True

win = 0
play = random.randint(0, 1)
clicked = False
drag = False
run = True
while run:
    pos = pygame.mouse.get_pos()

    if scene == "mainmenu":
        screen.blit(main_img,(0, 0))
        if play_button.draw():
            setup()
            scene = "game"

        if loadgame_button.draw():
            data = save.load_game()
            if data != None:
                area = []
                area_name = 1
                for y in range(BOARD_SIZE):
                    for x in range(BOARD_SIZE):
                        area.append(Area(STARTPOS[0] + x * LENGTH, STARTPOS[1] + y * LENGTH, LENGTH, area_name))
                        area_name += 1
                table = {}
                Char = [[],[]]
                for x, a in list(zip(loading("image/p1"),data[0])):
                    Char[0].append(player(screen, fontcount, x, 50 - len(Char[0]) * 4, 595 - len(Char[0]) * 100, 1, a))
                for x, a in list(zip(loading("image/p2"),data[1])):
                    Char[1].append(player(screen, fontcount, x, 700 - len(Char[1]) * 4, 595 - len(Char[1]) * 100, 2, a))

                for i in data[2]:
                    for j in i.keys():
                        for x in Char[i[j][0]-1]:
                            if x.size == i[j][1]:
                                used = copy.copy(x)
                                used.amount = 1
                                used.update(i[j][2],i[j][3])
                                used.stop(True)
                                table[j] = used
                draw = data[3]
                play = data[4]
                scene = "game"
            
        if exit_button.draw():
            run = False
    
    elif scene == "pause":
        background.drawbackground()
        if resume_button.draw():
            scene = "game"
        if savegame_button.draw():
            data = [[],[],[]]
            n = 0
            t = {}
            for i in Char:
                for j in i:
                    data[n].append(j.amount)
                n = 1
            for i in table:
                t[i] = (table[i].own,table[i].size,table[i].x,table[i].y)
            data[2].append(t)
            data.append(draw)
            data.append(play)
            save.save_game(data)
        if mainmenu_button.draw():
            scene = "mainmenu"

    elif scene == "game":
        background.drawbackground()
        drawTable(screen, STARTPOS, ENDPOS, BOARD_SIZE)
        
        if home_button.draw():
            scene = "pause"

        for x in table.values():
            if x != None:
                x.draw()
        if play == 0:
            for i in Char[1]:
                i.draw()
                i.text()
            for i in Char[0]:
                i.draw()
                i.text()
            screen.blit(arrowLeft, (350, 625))
        else:
            for i in Char[0]:
                i.draw()
                i.text()
            for i in Char[1]:
                i.draw()
                i.text()
            screen.blit(arrowRight, (300, 625))

        if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
            clicked = True
        elif pygame.mouse.get_pressed()[0] == 0:
            clicked = False
            for a in area:
                if a.area.collidepoint(pos) and drag:
                    if select.size > a.size:
                        a.change(select.size, select.own)
                        select.update(a.area.topleft[0] + (LENGTH - select.area.width)/2, a.area.topleft[1] + (LENGTH - select.area.height)/2)
                        used = copy.copy(select)
                        used.stop(True)
                        if a.name in table:
                            table.pop(a.name)
                        table[a.name] = used
                        pygame.mixer.Sound.play(drop)
                        play = 0 if play == 1 else 1
                        select.use()
                        select.back()
                        draw += 1
                        win = checkwin(area, draw)
                if drag:
                    select.back()

            drag = False
        
        if clicked:
            for x in Char[play]:
                if x.area.collidepoint(pos) and drag != True and x.amount > 0:
                    pygame.mixer.Sound.play(pickup)
                    offset_x, offset_y = x.area.topleft[0] - pos[0], x.area.topleft[1] - pos[1]
                    drag = True
                    select = x
        if drag:
            select.update(pos[0] + offset_x ,pos[1] + offset_y)
        
        if win in [1,2,3]:
            
            pygame.time.delay(200)
            scene = "result"
            if win == 1:
                result = "yellow eddy win"
            elif win == 2:
                result = "pink eddy win"
            elif win == 3:
                result = "draw"

    elif scene == "result":
        pygame.mixer.music.stop()
        if winsound:
            pygame.mixer.Sound.play(victory)
            winsound = False
        if result == "yellow eddy win":
            screen.blit(yellowwin,(0, 0))
            screen.blit(yellow,(60, 100))
        elif result == "pink eddy win":
            screen.blit(pinkwin,(0, 0))
            screen.blit(pink,(60, 100))
        elif result == "draw":
            screen.blit(draw_bg,(0, 0))
            screen.blit(draw_img,(60, 100))
        if playagain_button.draw():
            pygame.mixer.Sound.stop(victory)
            pygame.mixer.music.play(-1)
            setup()
            scene = "game"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()