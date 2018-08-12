import pygame
from sys import exit

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((25,25))
        self.image.fill((255,0,0))
        self.rect=self.image.get_rect()
        self.rect.centerx=0
        self.rect.centery=200
        self.x=1

    def update(self,screen):
        self.rect.centerx+=self.x
        if self.rect.left>screen.get_width():
            self.rect.right=0

def main():
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    background=pygame.Surface((screen.get_size()))
    background.fill((255,255,255))
    background=background.convert()
    screen.blit(background,(0,0))
    clock=pygame.time.Clock()
    box=Box()
    allsprites=pygame.sprite.Group(box)
    while 1:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
        allsprites.clear(screen,background)
        allsprites.update(screen)
        #pygame.time.wait(30)
        allsprites.draw(screen)
        pygame.display.update()
if __name__=='__main__':
    main()
