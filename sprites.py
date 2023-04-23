import pygame
import random
from config import PLAYER_SPEED, MAX_FRUITS, MAX_MISSED, INITIAL_FRUIT_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, FRUIT_FALL_DELAY, PLAYER_Y_OFFSET

class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGHT - self.rect.height
        self.rect.x = SCREEN_WIDTH // 2
        self.speed = PLAYER_SPEED
        self.max_fruits = MAX_FRUITS
        self.max_missed = MAX_MISSED
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, pygame.display.Info().current_h)) # Restrict player position within screen boundaries

    def reset(self):
        # Implement reset logic here
        # For example, reset the position of the player to the center of the screen
        self.rect.x = self.screen_width // 2 - self.rect.width // 2
        self.rect.y = self.screen_height - self.rect.height - PLAYER_Y_OFFSET

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Fruit(pygame.sprite.Sprite):
    def __init__(self, image, level, level_difficulty):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.level = level
        self.level_difficulty = level_difficulty

        if self.rect.width > SCREEN_WIDTH:
            self.rect.width = SCREEN_WIDTH
        elif self.rect.width < 0:
            self.rect.width = 0

        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -random.randint(0, FRUIT_FALL_DELAY)  # Add random delay for fruits to fall at different times
        if level == 1:
            self.speed = random.uniform(1, int(INITIAL_FRUIT_SPEED))
        else:
            self.speed = random.uniform(1, int(INITIAL_FRUIT_SPEED * self.level_difficulty))


    def update(self):
        self.rect.y += self.speed  # Update vertical position based on speed
        if self.rect.x < 0:  # Check if sprite goes off the left edge of the screen
            self.rect.x = 0  # Set x position to 0
        elif self.rect.x > SCREEN_WIDTH - self.rect.width:  # Check if sprite goes off the right edge of the screen
            self.rect.x = SCREEN_WIDTH - self.rect.width  # Set x position to the rightmost possible value


