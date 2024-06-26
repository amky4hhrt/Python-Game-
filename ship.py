import pygame

class Ship():

    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting postion"""
        self.screen = screen
        self.ai_settings = ai_settings

        #Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #store a decimal value for the ship center
        self.center = float(self.rect.centerx)

        #Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship position based on the movement flag"""
        #update the ship center value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >0:
            # self.rect.centerx -=1
            self.center -= self.ai_settings.ship_speed_factor

        #update the rect object from the self center
        self.rect.centerx = self.center



    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

        