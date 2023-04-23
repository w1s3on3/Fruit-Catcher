# Configuration settings
import pygame

# Game keys
LEFT_KEY = pygame.K_LEFT
RIGHT_KEY = pygame.K_RIGHT
PAUSE_KEY = pygame.K_SPACE

# Game variables
MAX_FRUITS = 5 # Maximum number of fruits on screen at once
MAX_MISSED = 3 # Maximum number of fruits that can be missed before game ends
MAX_LEVEL = 100 # Maximum level before game ends
NEW_LEVEL = 5 # New level after catching this many fruits
LEVEL_DIFFICULTY = 2  # increase in speed per level
INITIAL_FRUIT_SPEED = 1 # Initial speed of fruits
PLAYER_SPEED = 3 # Player speed

# Screen dimensions
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

# Font
FONT_SIZE = 36

# Images
BACKGROUND_IMAGE = "images/background.jpg"
PLAYER_IMAGE = "images/basket.png"
PLAYER_IMAGE_SIZE = (50, 50)
FRUIT_IMAGES = [
    {"image": "images/apple.png", "size": (40, 40)},
    {"image": "images/banana.png", "size": (40, 40)},
    {"image": "images/orange.png", "size": (40, 40)}
]

# Constants for magic numbers
PLAYER_Y_OFFSET = 10
FRUIT_FALL_DELAY = 100

# Debug mode
DEBUG = True