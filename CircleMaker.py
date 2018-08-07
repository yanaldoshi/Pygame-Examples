import pygame
pygame.init()
def main():
    back=pygame.Surface((640,480))
    back.fill((0,0,0))
    for i in range(1,320,3):
        pygame.draw.circle(back,(255,0,0),(i,i),i,1)
        pygame.draw.circle(back,(0,0,255),((640-i),i),i,1)
        pygame.draw.circle(back,(0,255,0),(640-i,480-i),i,1)
        pygame.draw.circle(back,(255,255,255),(320,240),i,1)
    pygame.image.save(back,'circless.jpg')
if __name__=='__main__':
    main()
