import pygame
from robotsprite import *
import sys

def main():
    pygame.init()
    screen=pygame.display.set_mode((1290,720))
    pygame.display.set_caption("Lonely Robot")
    background=pygame.Surface(screen.get_size())
    background.fill((255,255,255))
    screen.blit(background,(0,0))
    robo=Robot()
    friend=FollowerCircle()
    friendslist=pygame.sprite.OrderedUpdates(robo,friend)
    clock=pygame.time.Clock()
    pygame.mouse.set_visible(False)

    while True:
        clock.tick(60)
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.mouse.set_visible(True)
                pygame.quit()
                sys.exit()
        state=robo.checkstate(pygame.mouse.get_pos())
        if state==1:
            friendslist.clear(screen,background)
            friendslist.update()
            friendslist.draw(screen)
            pygame.draw.line(screen,(0,0,0),(507,273),(370,170),5)
            screen.blit(robo.message1,(300,100))
            pygame.display.update()
            continue
        elif state==2:
            friendslist.clear(screen,background)
            friendslist.update()
            friendslist.draw(screen)
            pygame.draw.line(screen,(0,0,0),(507,273),(370,170),5)
            screen.blit(robo.message2,(300,100))
            pygame.display.update()
            continue
        elif state==3:
            pass
            
        friendslist.clear(screen,background)
        friendslist.update()
        friendslist.draw(screen)
        pygame.display.update()

if __name__=="__main__":
    main()
