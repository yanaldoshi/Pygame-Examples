import pygame
from sys import exit
from random import randint
def main():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    screen.fill((255,255,255))
    clock=pygame.time.Clock()
    while 1:
        #clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        if screen.mustlock():
            screen.lock()
        for x in range(100):
            rand_pos=(randint(0,640),randint(0,480))
            rand_col=(randint(0,255),randint(0,255),randint(0,255))
            screen.set_clip(270,190,100,100)
            screen.set_at(rand_pos,rand_col)
        try:
            screen.unlock()
        except AttributeError:
            pass
        pygame.display.update()

if __name__=='__main__':
    main()
