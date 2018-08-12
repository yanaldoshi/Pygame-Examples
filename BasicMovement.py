import pygame
from pygame.locals import *
from sys import exit
from vector2 import Vector2
pygame.init()
screen=pygame.display.set_mode((640,480))
screen.fill((255,255,255))
clock=pygame.time.Clock()
pos=Vector2((screen.get_width()-50)/2,(screen.get_height()-50)/2)
surface=pygame.Surface((50,50))
surface.fill((255,0,0))
speed=100.
pygame.key.set_repeat(10,30)
while 1:
    screen.fill((255,255,255))
    screen.blit(surface,pos)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    direction=Vector2(0.,0.)
    pressed_keys=pygame.key.get_pressed()
    if pressed_keys[K_LEFT]:
        direction.x=-1.
    elif pressed_keys[K_RIGHT]:
        direction.x=1.
    if pressed_keys[K_UP]:
        direction.y=-1.
    elif pressed_keys[K_DOWN]:
        direction.y=1.
    direction.normalize()
    time_passed=clock.tick()/1000.0
    pos+=direction*speed*time_passed
    if(pos[0]>=590):
		pos[0]=590
    elif(pos[0]<=0):
		pos[0]=0
    if(pos[1]>=430):
		pos[1]=430
    elif(pos[1]<=0):
		pos[1]=0
    pygame.display.update()
