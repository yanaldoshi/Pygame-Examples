import pygame

class Robot(pygame.sprite.Sprite):
    """A simple robot that responds to when a mouse hovers on it."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("Bob.png")
        self.image=self.image.convert_alpha()
        self.rect=self.image.get_rect()
        self.font=pygame.font.SysFont(None,30)
        self.message1=self.font.render("Hello!! Human",1,(0,0,0))
        self.message2=self.font.render("Hey! Come Back, I Am Lonely :(",1,(0,0,0))
        self.touched=False

    def update(self):
        self.rect.centerx=600
        self.rect.centery=400

    def checkstate(self,pos):
        if self.rect.collidepoint(pos):
            self.touched=True
            return 1  #touched 1st
        else:
            if self.touched:
                #self.touched=False
                return 2 #left
            else:
                return 3 #idle

class FollowerCircle(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("follower.png")
        self.image=self.image.convert_alpha()
        self.rect=self.image.get_rect()

    def update(self):
        self.rect.centerx,self.rect.centery=pygame.mouse.get_pos()

        
        
