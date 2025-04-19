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
MAX_HEIGHT = HEIGHT - 50
SPEED = 250 # initial sorting speed in millisecond

def generate_random_array(size):
    """Generate a random array of integers."""
    return [random.randint(10, MAX_HEIGHT) for _ in range(size)]

if __name__ == "__main__":
    random_array = generate_random_array(ARRAY_SIZE)
    print("generated array: ", random_array)