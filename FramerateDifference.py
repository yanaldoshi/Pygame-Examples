import pygame
from sys import exit
pygame.init()
screen=pygame.display.set_mode((640,480))
x1,x2=(0,0)
speed=250
frame_no=0
clock=pygame.time.Clock()
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),(x1,100,50,50))
    pygame.draw.rect(screen,(0,255,0),(x2,300,50,50))
    time_passed=clock.tick(30)
    time_seconds=time_passed/1000.0
    distance=speed*time_seconds
    x1+=distance
    if (frame_no%5)==0:
        x2+=distance*5
    if x1>640:
        x1-=640
    if x2>640:
        x2-=640
    frame_no+=1
    pygame.display.update()
    
