import pygame

def load_image(image_path):
    try:
        image = pygame.image.load(image_path).convert_alpha()
        return image
    except pygame.error as e:
        print(f"Error loading image: {image_path}")
        raise SystemExit(e)

