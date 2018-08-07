import pygame
from pygame.locals import *
from sys import exit
from random import randint
def main():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    points=[]
    clock=pygame.time.Clock()
    while 1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEMOTION:
                points.append(event.pos)
                if len(points)>=2:
                    screen.fill((255,255,255))
                    pygame.draw.lines(screen,(randint(0,255),randint(0,255),randint(0,255)),False,points,10)
                if len(points)>10:
                    del points[0]
        pygame.display.flip()

if __name__=='__main__':
    main()
        
