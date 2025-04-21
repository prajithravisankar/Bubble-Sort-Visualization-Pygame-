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

def draw_bars(array, comparisons=None, swaps=None, sorted_indices=None, comparisons_count=0, swaps_count=0):
    """Draws the bars on the screen."""
    SCREEN.fill(BLACK)

    for index, value in enumerate(array):
        # determine the color of the bar based on its state
        color = WHITE
        if sorted_indices and index in sorted_indices:
            color = GREEN
        elif swaps and index in swaps: 
            color = ORANGE
        elif comparisons and index in comparisons:
            color = RED

        # position and size of the bar
        bar_rect = pygame.Rect(index * BAR_WIDTH, HEIGHT - value, BAR_WIDTH - 1, value)
        # draw the bar
        pygame.draw.rect(SCREEN, color, bar_rect)

        # display number above the bar
        number_text = FONT.render(str(value), True, WHITE)
        text_rect = number_text.get_rect(center=(index * BAR_WIDTH + BAR_WIDTH // 2, HEIGHT - value - 15))
        SCREEN.blit(number_text, text_rect)

    # display metrics at the top left corner
    comparisons_text = FONT.render(f"Comparisons: {comparisons_count}", True, WHITE)
    swaps_text = FONT.render(f"Swaps: {swaps_count}", True, WHITE)
    SCREEN.blit(comparisons_text, (10, 10))
    SCREEN.blit(swaps_text, (10, 30))

    pygame.display.flip()

def bubble_sort_step_by_step(array):
    """Sorts an array using the bubble sort algorithm."""
    n = len(array)
    steps = []
    comparison_count = 0
    swaps_count = 0
    for i in range(n):
        """outer loop, worst case we have to go through all the elements"""
        swapped = False
        for j in range(0, n - i - 1):
            """inner loop, we compare adjacent elements and put the larger one at the end"""
            steps.append(("comparison", j, j + 1))
            comparison_count += 1

            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

                steps.append(("swap", j, j + 1))
                swaps_count += 1

        if not swapped:
            break

    for i in range(n):
        steps.append(("sorted", n - i - 1))

    return steps, comparison_count, swaps_count


if __name__ == "__main__":
    random_array = generate_random_array(ARRAY_SIZE)
    print("generated array: ", random_array)

    
    steps, total_comparison, total_swaps = bubble_sort_step_by_step(random_array)
    print("steps: ", steps)
    print('\n')
    print("total comparisons: ", total_comparison)
    print('\n')
    print("total swaps: ", total_swaps)

    # testing with single step
    comparisons = {0, 1}
    swaps = None
    sorted_indices = set() # no sorted indices yet

    # draw random bars
    draw_bars(random_array, comparisons=comparisons, swaps=swaps, sorted_indices=sorted_indices, comparisons_count=total_comparison, swaps_count=total_swaps)

    # keep running until we quit
    running = True
    while running: 
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                running = False

    pygame.quit()