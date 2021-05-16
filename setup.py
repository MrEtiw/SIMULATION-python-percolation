import numpy as np


def get_empty_grid(grid_size):
    return np.zeros(grid_size)


def fill_empty_grid(empty_grid, p):
    random_grid = np.random.random(empty_grid.shape)
    index_to_fill = random_grid <= p
    return empty_grid + 1 * index_to_fill


def get_filled_grid(grid_size, p):
    empty_grid = get_empty_grid(grid_size)
    return fill_empty_grid(empty_grid, p)

