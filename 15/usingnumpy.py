import numpy as np
import time
import matplotlib.pyplot as plt


def show_grid(grid):
    plt.imshow(grid, cmap='binary', interpolation='nearest')
    plt.show()


def count_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1] and grid[nx, ny] == 1:
            count += 1

    return count


def update_grid(grid):
    new_grid = grid.copy()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            neighbors = count_neighbors(grid, i, j)

            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid


def count_survivors(grid):
    return np.sum(grid)


def main(generations, delay):
    with open("grid.txt", "r", encoding="utf-8") as grid_file:
        grid = np.array(eval(grid_file.read()))

    start_time = time.time()
    for _ in range(generations):
        show_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

    end_time = time.time()
    elapsed_time = end_time - start_time - generations * delay

    survivors = count_survivors(grid)
    print(f"Количество выживших: {survivors}")
    print(f"Время выполнения: {elapsed_time:.2f} секунд")


if __name__ == "__main__":
    steps = 20
    delay = 1.5

    main(steps, delay)
