# **Bubble Sort Visualization**

A simple visualization of the **Bubble Sort** algorithm using **Pygame**. This project helps you understand how Bubble Sort works by animating the sorting process step by step.

---

## **What is Bubble Sort?**

Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly swapping adjacent elements if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the list (beginning of the array) with each pass.

### **How It Works**
1. Start at the beginning of the array.
2. Compare two adjacent elements.
3. If the first element is greater than the second, swap them.
4. Move to the next pair of elements and repeat.
5. After each pass, the largest unsorted element "bubbles up" to its correct position.
6. Repeat until the array is fully sorted.

---

## **Features**
- Visualize comparisons, swaps, and the final sorted state.
- Interactive controls:
  - Press **R** to regenerate the array.
  - Use **Left/Right Arrow Keys** to step through the sorting process manually.
  - Press **Spacebar** to toggle automatic sorting.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bubble-sort-visualization.git
   cd bubble-sort-visualization
   ```

2. Install Pygame:
   ```bash
   pip install pygame
   ```

3. Run the program:
   ```bash
   python bubble_sort_visualization_pygame.py
   ```

---

## **How to Use**
- Watch as the algorithm compares and swaps elements step by step.
- Use the interactive controls to explore the sorting process manually or automatically.

---

### **Phase 1: Bubble Sort Visualization Setup & Planning**

**Goal**: Set up the project structure, define visualization requirements, and initialize basic functionality.

- [x]  **Main Todo 1.1: Project Initialization**
    - [x]  **Sub-todo 1.1.1**: Create a new Python file for the project.
    - [x]  **Sub-todo 1.1.2**: Import necessary libraries (`pygame`, `random`, `sys`).
    - [x]  **Sub-todo 1.1.3**: Initialize Pygame with `pygame.init()`.
    - [x]  **Sub-todo 1.1.4**: Define constants like screen dimensions (`WIDTH`, `HEIGHT`), colors (`WHITE`, `BLACK`, etc.), and bar-related values (`ARRAY_SIZE`, `BAR_WIDTH`, `MAX_HEIGHT`, `SPEED`).
- [x]  **Main Todo 1.2: Generate and Test Random Array**
    - [x]  **Sub-todo 1.2.1**: Write a function `generate_random_array(size)` to generate a random array of integers between `10` and `MAX_HEIGHT`.
    - [x]  **Sub-todo 1.2.2**: Test the function by printing the generated array.
- [x]  **Main Todo 1.3: Initial Bar Chart Visualization**
    - [x]  **Sub-todo 1.3.1**: Write a function `draw_bars(array)`:
        - Clear the screen with `SCREEN.fill(BLACK)`.
        - Draw bars using `pygame.draw.rect()` based on the array values.
        - Add numbers above each bar using `FONT.render()` and `SCREEN.blit()`.
    - [x]  **Sub-todo 1.3.2**: Test the function by passing a random array and displaying the visualization.

---

### **Phase 2: Implement Bubble Sort Logic**

**Goal**: Build and test the bubble sort algorithm before integrating it with the visualization.

- [x]  **Main Todo 2.1: Basic Bubble Sort Algorithm**
    - [x]  **Sub-todo 2.1.1**: Implement a simple bubble sort function `bubble_sort(array)`:
        - Use nested loops to iterate through the array.
        - Compare adjacent elements and swap them if they are in the wrong order.
        - Stop early if no swaps are made in a pass.
    - [x]  **Sub-todo 2.1.2**: Test the function with a few examples to ensure correctness.
- [x]  **Main Todo 2.2: Step-by-Step Bubble Sort**
    - [x]  **Sub-todo 2.2.1**: Extend the bubble sort function into `bubble_sort_step_by_step(array)`:
        - Track comparisons and swaps in a `steps` list.
        - Append actions like `("compare", i, j)` and `("swap", i, j)` to the `steps` list.
        - Return the `steps`, total comparisons, and total swaps.
    - [x]  **Sub-todo 2.2.2**: Test the function by printing the steps and verifying their correctness.

---

### **Phase 3: Integrate Bubble Sort with Visualization**

**Goal**: Combine the bubble sort logic with the bar chart visualization.

- [x]  **Main Todo 3.1: Visualize Sorting Steps**
    - [x]  **Sub-todo 3.1.1**: Modify `draw_bars()` to accept additional parameters like `comparisons`, `swaps`, `sorted_indices`, `comparisons_count`, and `swaps_count`.
    - [x]  **Sub-todo 3.1.2**: Color bars differently based on their state (`comparisons`, `swaps`, `sorted_indices`).
    - [x]  **Sub-todo 3.1.3**: Display metrics (comparisons and swaps count) at the top-left corner of the screen.
- [x]  **Main Todo 3.2: Apply Sorting Steps**
    - [x]  **Sub-todo 3.2.1**: In the `main()` function, precompute all sorting steps using `bubble_sort_step_by_step(array[:])`.
    - [x]  **Sub-todo 3.2.2**: Maintain a `current_step` variable to track progress.
    - [x]  **Sub-todo 3.2.3**: Apply steps up to `current_step` to create a temporary array and pass it to `draw_bars()`.
- [x]  **Main Todo 3.3: Add Animation Timing**
    - [x]  **Sub-todo 3.3.1**: Use `pygame.time.delay(SPEED)` to control the speed of automatic sorting.
    - [x]  **Sub-todo 3.3.2**: Ensure the delay only happens when `auto_sort` is enabled.

---

### **Phase 4: Handle User Input**

**Goal**: Allow the user to interact with the visualization.

- [ ]  **Main Todo 4.1: Regenerate Array**
    - [ ]  **Sub-todo 4.1.1**: Detect when the user presses the 'R' key (`pygame.K_r`).
    - [ ]  **Sub-todo 4.1.2**: Regenerate the array and reset all sorting-related variables.
- [x]  **Main Todo 4.2: Step Forward/Backward**
    - [x]  **Sub-todo 4.2.1**: Detect when the user presses the right arrow key (`pygame.K_RIGHT`) to step forward.
    - [x]  **Sub-todo 4.2.2**: Detect when the user presses the left arrow key (`pygame.K_LEFT`) to step backward.
    - [x]  **Sub-todo 4.2.3**: Update `current_step` and adjust the visualization accordingly.
- [x]  **Main Todo 4.3: Toggle Auto-Sort**
    - [x]  **Sub-todo 4.3.1**: Detect when the user presses the spacebar (`pygame.K_SPACE`).
    - [x]  **Sub-todo 4.3.2**: Toggle the `auto_sort` mode and update the visualization dynamically.

---

### **Phase 5: Final Integration & Testing**

**Goal**: Combine all components into the main program and test edge cases.

- [ ]  **Main Todo 5.1: Combine Everything in Main Program**
    - [ ]  **Sub-todo 5.1.1**: Generate a random array.
    - [ ]  **Sub-todo 5.1.2**: Precompute sorting steps using `bubble_sort_step_by_step(array[:])`.
    - [ ]  **Sub-todo 5.1.3**: Run the visualization loop, handling user input and updating the display.
- [ ]  **Main Todo 5.2: Refactor and Clean Up**
    - [ ]  **Sub-todo 5.2.1**: Review the code for readability and maintainability.
    - [ ]  **Sub-todo 5.2.2**: Add comments to explain each part of the program.
    - [ ]  **Sub-todo 5.2.3**: Ensure consistent variable naming and formatting.
- [ ]  **Main Todo 5.3: Test Edge Cases**
    - [ ]  **Sub-todo 5.3.1**: Test the program with edge cases such as:
        - Smallest array size (`ARRAY_SIZE = 1`).
        - Already sorted array.
        - Reverse-sorted array.
        - Array with duplicate values.

---

### **Phase 6: Optional Enhancements**

**Goal**: Improve the visualization and user experience.

- [ ]  **Main Todo 6.1: Enhance Visualization**
    - [ ]  **Sub-todo 6.1.1**: Experiment with different colors for comparisons, swaps, and sorted indices.
    - [ ]  **Sub-todo 6.1.2**: Add grid lines or other visual enhancements to the screen.
    - [ ]  **Sub-todo 6.1.3**: Adjust the `SPEED` parameter to make the visualization smoother or faster.
- [ ]  **Main Todo 6.2: Add Additional Metrics**
    - [x]  **Sub-todo 6.2.1**: Display additional metrics like time elapsed or percentage completion.
    - [ ]  **Sub-todo 6.2.2**: Highlight the final sorted state with a unique animation or effect.
- [ ]  **Main Todo 6.3: Export Visualization**
    - [ ]  **Sub-todo 6.3.1**: Save the visualization as a GIF or video file for sharing.