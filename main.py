import pygame
from constants import *
from player import Player
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    print("Starting asteroids!")
    
    
    
    while True:
     for event in pygame.event.get():
       if event.type == pygame.QUIT:
          return

     # limit the framerate to 60fps
     dt = clock.tick(60) / 1000
     screen.fill("black")
     player.draw(screen)
     pygame.display.flip()
     player.update(dt)

if __name__ == "__main__":
    main()
