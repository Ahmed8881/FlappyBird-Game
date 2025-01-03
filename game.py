import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game settings
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_HEIGHT = 400
PIPE_GAP = 150
PIPE_SPEED = 3

# Load images
BIRD_IMAGE = pygame.image.load('image.png')
BIRD_IMAGE = pygame.transform.scale(BIRD_IMAGE, (50, 35))

# Load fonts
FONT = pygame.font.SysFont('Arial', 30)
