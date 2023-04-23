# File: main.py
# Author: Paul Wyers
# License: GNU General Public License v3.0 (GPLv3)

import sys
import random
import pygame
from sprites import Player, Fruit
from resources import load_image
from config import *

pygame.init()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Catcher")
clock = pygame.time.Clock()

# Font
font = pygame.font.SysFont(None, FONT_SIZE)

# Load images
bg = load_image(BACKGROUND_IMAGE)
# Scale background image to screen size
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
# Player image
player_img = pygame.transform.scale(load_image(PLAYER_IMAGE), (50, 50))  
# Fruit images
fruit_images = []
for fruit in FRUIT_IMAGES:
    fruit_img = pygame.transform.scale(load_image(fruit["image"]), fruit["size"])
    fruit_images.append(fruit_img)

# Start Game variables
player = Player(player_img)
fruits = pygame.sprite.Group()
level = 1 # Start at level 1
fruits_caught = 0 
fruits_missed = 0  
game_over = False # Game starts not over
paused = False  # Game starts unpaused

# Reset game state.
def reset_game(player, fruits):
    player.reset()
    fruits.empty()
    global fruits_caught
    fruits_caught = 0
    global fruits_missed
    fruits_missed = 0

# Show game over screen and return the rect of the try again button.
def show_game_over(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT):
    if not isinstance(screen, pygame.Surface):
        raise ValueError("screen parameter must be a valid pygame.Surface object")
    if not isinstance(font, pygame.font.Font):
        raise ValueError("font parameter must be a valid pygame.font.Font object")

    game_over_text = font.render("Game Over", True, RED)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    screen.blit(game_over_text, game_over_rect)

    try_again_text = font.render("Try Again", True, BLACK)
    try_again_rect = try_again_text.get_rect()
    try_again_rect.center = (SCREEN_WIDTH // 2, game_over_rect.bottom + 50)
    screen.blit(try_again_text, try_again_rect)

    quit_text = font.render("QUIT", True, ORANGE)
    quit_rect = quit_text.get_rect()
    quit_rect.center = (SCREEN_WIDTH // 2, try_again_rect.bottom + 50)
    screen.blit(quit_text, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Close pygame window
                sys.exit()  # Exit the Python interpreter
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if try_again_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            return True  # Return True when Try Again button is clicked
        if quit_rect.collidepoint(mouse_pos) and mouse_click[0] == 1:
            pygame.quit()  # Close pygame window
            sys.exit()  # Exit the Python interpreter

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:  # Check for key presses
            if event.key == PAUSE_KEY:  # Pause game
                paused = not paused # Toggle pause state

    screen.blit(bg, (0, 0)) # Draw background image

    if not paused: # If game is not paused
        # using predefined LEFT_KEY and RIGHT_KEY variables from config.py file to move the player
        keys = pygame.key.get_pressed()
        if keys == LEFT_KEY:
            player.move_left()
        if keys == RIGHT_KEY:
            player.move_right()

        # Spawn fruits
        if len(fruits) < MAX_FRUITS:
            fruit_img = random.choice(fruit_images)
            fruit = Fruit(fruit_img, level, LEVEL_DIFFICULTY)
            fruits.add(fruit)

        # Update and draw player & fruit
        player.update()
        fruits.update()

        # Check for collision with fruits
        caught_fruits = pygame.sprite.spritecollide(player, fruits, True)
        for fruit in caught_fruits:
            if fruit.rect.colliderect(player.rect.left, player.rect.top, player.rect.width, player.rect.height / 2): 
                fruits_caught += 1
                if fruits_caught >= level * NEW_LEVEL:
                    level += 1
                    for fruit in fruits:
                        fruit.update()
            else:
                # Fruit is missed
                fruits_missed += 1
                if DEBUG:
                    print(f"Missed fruit")

            if DEBUG:
                print(f"Caught fruit {fruit.speed} ")

        # Check if fruits missed the basket
        for fruit in fruits:
            if fruit.rect.top > SCREEN_HEIGHT:
                fruits_missed += 1
                fruit.kill()
                if DEBUG:
                    print(f"Fruit missed")


        # Draw sprites
        player.draw(screen)
        fruits.draw(screen)

        # Draw game stats on screen
        caught_text = font.render("Score: {}".format(fruits_caught), True, BLACK)
        screen.blit(caught_text, (10, 10))

        missed_text = font.render("Missed: {}".format(fruits_missed), True, BLACK)
        screen.blit(missed_text, (10, 40))

        level_text = font.render("Level: {}".format(level), True, BLACK)
        screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

        if fruits_missed >= MAX_MISSED: # Check if game over condition is met
            game_over = True

        if game_over: # If game over, show game over screen
            reset_game(player, fruits) # Reset game state
            while True:
                retry = show_game_over(screen, font, SCREEN_WIDTH, SCREEN_HEIGHT)
                if retry:
                    game_over = False
                    level = 1
                    break
                else:
                    pygame.quit() # Close pygame window
                    sys.exit() # Exit the Python interpreter
    
    else:   # game is paused, display pause screen
            pause_text = font.render("PAUSED", True, YELLOW)
            screen.blit(pause_text, ((SCREEN_WIDTH - pause_text.get_width()) // 2, SCREEN_HEIGHT // 2))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit() # Close pygame window
sys.exit() # Exit the Python interpreter