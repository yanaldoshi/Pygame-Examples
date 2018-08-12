import pygame
from pygame.locals import *
from sys import exit
def check(data):
    (event, linecolor, linewidth, background)=data
    if event.key==K_l:
        background=pygame.image.load("paint.bmp")
    elif event.key==K_c:
        background.fill((255,255,255))
    elif event.key==K_s:
        pygame.image.save(background,"paint.bmp")
    elif event.key==K_r:
        linecolor=(255,0,0)
    elif event.key==K_w:
        linecolor=(255,255,255)
    elif event.key==K_g:
        linecolor=(0,255,0)
    elif event.key==K_b:
        linecolor=(0,0,255)
    elif event.key==K_k:
        linecolor=(0,0,0)
    elif event.key==K_1:
        linewidth=1
    elif event.key==K_2:
        linewidth=2
    elif event.key==K_3:
        linewidth=3
    elif event.key==K_4:
        linewidth=4
    elif event.key==K_5:
        linewidth=5
    elif event.key==K_6:
        linewidth=6
    elif event.key==K_7:
        linewidth=7
    elif event.key==K_8:
        linewidth=8
    elif event.key==K_9:
        linewidth=9
    data=(event,linecolor,linewidth,background)
    return data
def showstats(linecolor,linewidth):
    font=pygame.font.SysFont('arial',20)
    stats=font.render("color:%s width:%d"%(linecolor,linewidth),1,(255,255,255),(0,0,0))
    return stats
def main():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    background=pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    clock=pygame.time.Clock()
    linewidth=1
    linecolor=(0,0,0)
    linestart=(0,0)
    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==MOUSEMOTION:
                lineend=pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()==(1,0,0):
                    pygame.draw.line(background, linecolor, linestart,lineend, linewidth)
                linestart=lineend
            elif event.type==KEYDOWN:
                data=(event,linecolor, linewidth, background)
                data=check(data)
                (event,linecolor,linewidth,background)=data
        screen.blit(background,(0,0))
        label=showstats(linecolor,linewidth)
        screen.blit(label,(0,screen.get_height()-30))
        pygame.display.update()
if __name__=="__main__":
    main()
    
