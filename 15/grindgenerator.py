import random


def create_grid(rows, cols):
    return [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]


grid = create_grid(512, 512)

with open("grid.txt", "w", encoding="utf-8") as file:
    file.write(str(grid))
