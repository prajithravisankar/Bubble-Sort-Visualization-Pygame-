import pygame
import random
import sys

pygame.init()


# screen dimensions
WIDTH, HEIGHT = 800, 600

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# bar-related constants
ARRAY_SIZE = 20
BAR_WIDTH = WIDTH // ARRAY_SIZE
BAR_HEIGHT = HEIGHT - 50
SPEED = 250 # initial sorting speed in millisecond