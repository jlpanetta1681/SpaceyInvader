import pygame
import os
import random
import time

pygame.font.init()


WIDTH, HEIGHT= 650, 650

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders By Joe")

# pics and icons
# Ships

RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))

# Player  Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png")) 
BLUE_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))

# Player Laser
YELLOW_LASERS = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASERS
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.mask_health = health

# Main Game Loop

def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5
    ship = Ship(300, 300)

    clock = pygame.time.Clock()


    def redraw_window():
        WIN.blit(BG, (0, 0))
        # Draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255, 0, 0))
        level_label = main_font.render(f"Level: {level}", 1, (255, 0, 0))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        
        ship.draw(WIN)
        pygame.display.update()


    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]and ship.x - player_vel > 0: # left
            ship.x -= player_vel
        if keys[pygame.K_d]and ship.x + player_vel + 85 < WIDTH: # right
            ship.x += player_vel
        if keys[pygame.K_w]and ship.y - player_vel > 0: # up
            ship.y -= player_vel
        if keys[pygame.K_s] and ship.y + player_vel + 85 < HEIGHT: # down
            ship.y += player_vel

main()
