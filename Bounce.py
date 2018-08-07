import pygame
from sys import exit
draw_lines=True
line_col=(100,200,150)
pygame.init()
screen=pygame.display.set_mode((640,480))
clock=pygame.time.Clock()
x,y=(50,50)
points=[(x+25,y+25)]
speed_x,speed_y=133,170
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((255,255,255))
    pygame.draw.rect(screen,(255,0,0),(x,y,50,50))
    time_passed=clock.tick(100)
    x+=(time_passed/1000.0)*(speed_x)
    y+=(time_passed/1000.0)*(speed_y)
    if x>640-50:
        speed_x=-speed_x
        x=640-50
    elif x<0:
        speed_x=-speed_x
        x=0
    if y>480-50:
        speed_y=-speed_y
        y=480-50
    elif y<0:
        speed_y=-speed_y
        y=0
    if draw_lines==True:
        points.append((x+25,y+25))
        if len(points)>2:
            pygame.draw.lines(screen,line_col,False,points,5)
        if len(points)>1000:
            del points[0]
    pygame.display.update()
