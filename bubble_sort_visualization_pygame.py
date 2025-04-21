import pygame
import random
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Create Pygame screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bubble Sort Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORANGE = (255, 165, 0)

# Bar-related constants
ARRAY_SIZE = 20
BAR_WIDTH = WIDTH // ARRAY_SIZE
MAX_HEIGHT = HEIGHT - 50
SPEED = 250  # Initial sorting speed in milliseconds

FONT = pygame.font.SysFont("Arial", 16)

def generate_random_array(size):
    """Generate a random array of integers."""
    return [random.randint(10, MAX_HEIGHT) for _ in range(size)]

def draw_bars(array, comparisons=None, swaps=None, sorted_indices=None, comparisons_count=0, swaps_count=0):
    """Draws the bars on the screen."""
    SCREEN.fill(BLACK)

    for index, value in enumerate(array):
        # Determine the color of the bar based on its state
        color = WHITE
        if sorted_indices and index in sorted_indices:
            color = GREEN
        elif swaps and index in swaps:
            color = ORANGE
        elif comparisons and index in comparisons:
            color = RED

        # Position and size of the bar
        bar_rect = pygame.Rect(index * BAR_WIDTH, HEIGHT - value, BAR_WIDTH - 1, value)
        # Draw the bar
        pygame.draw.rect(SCREEN, color, bar_rect)

        # Display number above the bar
        number_text = FONT.render(str(value), True, WHITE)
        text_rect = number_text.get_rect(center=(index * BAR_WIDTH + BAR_WIDTH // 2, HEIGHT - value - 15))
        SCREEN.blit(number_text, text_rect)

    # Display metrics at the top-left corner
    comparisons_text = FONT.render(f"Comparisons: {comparisons_count}", True, WHITE)
    swaps_text = FONT.render(f"Swaps: {swaps_count}", True, WHITE)
    SCREEN.blit(comparisons_text, (10, 10))
    SCREEN.blit(swaps_text, (10, 30))

    pygame.display.flip()

def bubble_sort_step_by_step(array):
    """Sorts an array using the Bubble Sort algorithm and tracks each step."""
    n = len(array)
    steps = []
    comparison_count = 0
    swaps_count = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            steps.append(("compare", j, j + 1))
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

def main():
    global current_step, auto_sort

    # Generate a random array
    array = generate_random_array(ARRAY_SIZE)

    # Precompute all sorting steps
    steps, total_comparisons, total_swaps = bubble_sort_step_by_step(array[:])

    # Initialize variables for step-by-step visualization
    current_step = 0
    auto_sort = False  # Tracks whether automatic sorting is enabled
    clock = pygame.time.Clock()

    # Visualization loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Step forward with 'Right Arrow'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                if current_step < len(steps):
                    current_step += 1

            # Step backward with 'Left Arrow'
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                if current_step > 0:
                    current_step -= 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                auto_sort = not auto_sort # if on turn off, if off turn on

        # automatically advance to next steps if auto_sort is enabled
        if auto_sort and current_step < len(steps):
            current_step += 1
            pygame.time.delay(SPEED)


        # Apply steps up to current_step
        temp_array = array[:]  # Create a copy of the original array
        comparisons = None
        swaps = None
        sorted_indices = set()

        for step in steps[:current_step]:
            action, *indices = step
            if action == "compare":
                comparisons = tuple(indices)
            elif action == "swap":
                i, j = indices
                temp_array[i], temp_array[j] = temp_array[j], temp_array[i]
                swaps = tuple(indices)
            elif action == "sorted":
                sorted_indices.add(indices[0])

        # Draw the bars based on the current step
        draw_bars(temp_array, comparisons=comparisons, swaps=swaps, sorted_indices=sorted_indices,
                  comparisons_count=total_comparisons, swaps_count=total_swaps)
        
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()