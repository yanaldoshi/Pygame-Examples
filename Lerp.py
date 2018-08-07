import pygame
from sys import exit
def lerp(color1,color2,factor):
    """Linear interpolation of colors
        color1=original color
        color2=color needed
        factor=changing factor"""
    red1,green1,blue1=color1
    red2,green2,blue2=color2
    red=red1+(red2-red1)*factor
    green=green1+(green2-green1)*factor
    blue=blue1+(blue2-blue1)*factor
    return int(red),int(green),int(blue)
def main():
    screen=pygame.display.set_mode((640,480))
    points=[(0,120),(639,100),(639,140)]
    color1=(0,0,255)
    color2=(96,130,51)
    factor=0
    while 1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((255,255,255))
        pygame.draw.polygon(screen,(0,255,0),points,0)
        pygame.draw.circle(screen,(0,0,0),(int(factor*639.),120),10)
        if pygame.mouse.get_pressed()[0]:
            x,y=pygame.mouse.get_pos()
            factor=x/639.
            pygame.display.set_caption("%.4f"%factor)
        color=lerp(color1,color2,factor)
        pygame.draw.rect(screen,color,(0,240,640,240))
        pygame.display.update()

if __name__=='__main__':
    main()
