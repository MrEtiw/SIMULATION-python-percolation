from matplotlib import pyplot as plt
import numpy as np


def show_grid(grid):
    plt.figure()
    plt.imshow(grid, cmap = "binary")
    plt.colorbar()


def show_clusters(labeled_grid):
    labeled_grid[labeled_grid==0] = -1
    plt.figure()
    plt.imshow(labeled_grid, cmap = "tab10")
    #plt.imshow(labeled_grid)
