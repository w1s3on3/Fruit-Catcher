# Fruit Catcher

Fruit Catcher is a simple Python game developed by Paul Wyers.

## Updates

- 24/04/2023 : Sound effects added.

## Description

Fruit Catcher is a game where the player controls a basket at the bottom of the screen to catch falling fruits. 
The game is implemented in Python and uses Pygame library for the graphics and input handling.

## Features

- Catch falling fruits with the basket to score points
- Game ends when player misses a fruit 
- Configurable options in config.py file

## Configuration

The game's behavior can be customized by modifying the options in the `config.py` file. 
The `config.py` file includes the following options:

- `LEFT_KEY` : pygame.K_LEFT
- `RIGHT_KEY` : pygame.K_RIGHT
- `PAUSE_KEY` : pygame.K_SPACE

- `MAX_FRUITS`: Maximum number of fruits on screen at once
- `MAX_MISSED`: Maximum number of fruits that can be missed before game ends
- `MAX_LEVEL`: Maximum level before game ends
- `NEW_LEVEL`: New level after catching this many fruits
- `LEVEL_DIFFICULTY`: Increase in speed per level
- `INITIAL_FRUIT_SPEED`: Initial speed of fruits
- `PLAYER_SPEED`: Player speed

- `SCREEN_WIDTH`: Width of the game window in pixels
- `SCREEN_HEIGHT`: Height of the game window in pixels
- `FPS`: Frames per second for the game

- `WHITE`: RGB color value for white
- `BLACK`: RGB color value for black
- `RED`: RGB color value for red
- `GREEN`: RGB color value for green
- `BLUE`: RGB color value for blue
- `YELLOW`: RGB color value for yellow
- `ORANGE`: RGB color value for orange
- `PURPLE`: RGB color value for purple
- `PINK`: RGB color value for pink
- `BROWN`: RGB color value for brown

- `FONT_SIZE`: Font size for text in the game
- `BACKGROUND_IMAGE`: File path for the background image
- `PLAYER_IMAGE`: File path for the player image
- `PLAYER_IMAGE_SIZE`: Size of the player image
- `FRUIT_IMAGES`: List of dictionaries containing file paths and sizes for fruit images

- `PLAYER_Y_OFFSET`: Vertical offset for player position
- `FRUIT_FALL_DELAY`: Delay between fruit falling in milliseconds

- `CATCH_SOUND` : Sound for when you catch the fruit
- `MISS_SOUND` : Sound for when you miss a fruit

- `DEBUG`: Boolean value to enable or disable debug mode

## Credits

- Game developed by: [Paul Wyers](https://github.com/w1s3on3/) 
- Pygame library: [https://www.pygame.org/](https://www.pygame.org/)
- Game sounds from: [https://opengameart.org/](https://opengameart.org/content/interface-sounds-starter-pack)

## License

This game is released under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.en.html)

Enjoy playing Fruit Catcher!

