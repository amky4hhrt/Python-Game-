import sys
import pygame

def check_events():
    """Responds to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    """Update images to the screen and flip to the new screen"""
    #Redraw the screen with each pass through loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    #make the most recently screen visible
    pygame.display.flip()
