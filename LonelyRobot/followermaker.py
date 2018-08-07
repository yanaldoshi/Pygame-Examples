import pygame
pygame.init()
def main():
    back=pygame.Surface((50,50),pygame.SRCALPHA,32)
    pygame.draw.circle(back,(255,0,0),(25,25),25)
    pygame.image.save(back,'follower.png')
if __name__=='__main__':
    main()
