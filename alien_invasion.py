import pygame
import game_function as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship

def run_game():
  #Initialize pygame,settings, and screen object
  pygame.display.init()
  
  ai_settings = Settings()
  print ai_settings.screen_height
  print ai_settings.screen_width
  screen = pygame.display.set_mode((ai_settings.screen_height,ai_settings.screen_width))
  pygame.display.set_caption("Alien Invasion")
  
  #Make a ship, a group of bullets and a group of aliens
  ship = Ship(ai_settings,screen)
  bullets = Group()
  aliens = Group()
  
  #Create the fleet of aliens
  gf.create_fleet(ai_settings, screen, aliens)
  #Start the main loop for the game
  while True:
      
    gf.check_events(ai_settings,screen,ship,bullets) 
    ship.update()
    gf.update_bullets(bullets)
    gf.update_screen(ai_settings,screen,ship,aliens,bullets)

    #Make the most recently drawn screen visible
    pygame.display.flip()


run_game()