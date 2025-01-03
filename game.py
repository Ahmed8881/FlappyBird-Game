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
# Bird class
class Bird:
    def __init__(self):
        self.image = BIRD_IMAGE
        self.rect = self.image.get_rect()
        self.rect.center = (100, SCREEN_HEIGHT // 2)
        self.velocity = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.rect)
