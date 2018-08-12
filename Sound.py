import pygame
from pygame.locals import *
from sys import exit
def main():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    screen.fill((255,255,255))
    sound=pygame.mixer.Sound("Sound1.ogg")
    font=pygame.font.SysFont("jokerman",40)
    fontsurf=font.render("Press Space Mortal!!",0,(0,0,0))
    clock=pygame.time.Clock()
    coord=((screen.get_width()-fontsurf.get_width())/2,(screen.get_height()-fontsurf.get_height())/2)
    while 1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==KEYDOWN:
                if event.key==K_SPACE:
                    sound.play(5)
        screen.blit(fontsurf, coord)
        pygame.display.update()
if __name__=="__main__":
    main()
