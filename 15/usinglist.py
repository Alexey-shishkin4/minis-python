import copy
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
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 1:
            count += 1

    return count


def update_grid(grid):
    new_grid = copy.deepcopy(grid)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)

            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1

    return new_grid


def main(generations, delay):
    with open("grid.txt", "r", encoding="utf-8") as grid_file:
        grid = eval(grid_file.read())

    start_time = time.time()
    for _ in range(generations):
        show_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

    end_time = time.time()
    elapsed_time = end_time - start_time - generations * delay

    survivors = sum(sum(row) for row in grid)
    print(f"Количество выживших: {survivors}")
    print(f"Время выполнения: {elapsed_time:.2f} секунд")


if __name__ == "__main__":
    steps = 20
    delay = 1.5

    main(steps, delay)
