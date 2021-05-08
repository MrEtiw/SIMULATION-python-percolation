import numpy as np


def get_empty_grid(grid_size):
    return np.zeros(grid_size)


def fill_empty_grid(empty_grid, p):
    threshold_grid = np.random.random(empty_grid.shape)
    threshold_grid[threshold_grid >= p] = 1
    threshold_grid[threshold_grid < p] = 0
    return empty_grid + threshold_grid


def get_filled_grid(grid_size, p):
    empty_grid = get_empty_grid(grid_size)
    return fill_empty_grid(empty_grid, p)


