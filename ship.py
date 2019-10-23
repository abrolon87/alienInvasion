import pygame

class Ship:

    def __init__(self, ai_game):
        # set starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # load ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start new ships at midbottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        # store decimal value for horizontal position
        self.x = float(self.rect.x)
        
        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update ship's position based on the movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            

        self.rect.x = self.x #something is up with this line

    def blitme(self):
        self.screen.blit(self.image, self.rect)
