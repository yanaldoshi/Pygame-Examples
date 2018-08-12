import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Yo")
screen.fill((255,255,255))
clock=pygame.time.Clock()
while 1:
    clock.tick(30)
    event=pygame.event.wait()
    if event.type==QUIT:
        pygame.quit()
        break
    elif event.type==MOUSEBUTTONDOWN:
        linestart=pygame.mouse.get_pos()
    elif event.type==MOUSEBUTTONUP:
        lineend=pygame.mouse.get_pos()
        pygame.draw.line(screen,(0,0,0),linestart,lineend,1)
    pygame.display.update()

