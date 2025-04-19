import pygame
import random
import sys

pygame.init()


# screen dimensions
WIDTH, HEIGHT = 800, 600

# create pygame screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

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

FONT = pygame.font.SysFont("Arial", 16)

def generate_random_array(size):
    """Generate a random array of integers."""
    return [random.randint(10, MAX_HEIGHT) for _ in range(size)]

def draw_bars(array):
    """Draws the bars on the screen."""
    SCREEN.fill(BLACK)

    for index, value in enumerate(array):
        # position and size of the bar
        bar_rect = pygame.Rect(index * BAR_WIDTH, HEIGHT - value, BAR_WIDTH - 1, value)

        # draw the bar
        pygame.draw.rect(SCREEN, WHITE, bar_rect)

        # display number above the bar
        number_text = FONT.render(str(value), True, WHITE)
        text_rect = number_text.get_rect(center=(index * BAR_WIDTH + BAR_WIDTH // 2, HEIGHT - value - 15))
        SCREEN.blit(number_text, text_rect)

    pygame.display.flip()

if __name__ == "__main__":
    random_array = generate_random_array(ARRAY_SIZE)
    print("generated array: ", random_array)

    # draw random bars
    draw_bars(random_array)

    # keep running until we quit
    running = True
    while running: 
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False

    pygame.quit()