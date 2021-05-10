from matplotlib import pyplot as plt
import numpy as np


def show_grid(grid):
    plt.figure()
    plt.imshow(grid, cmap="binary")
    plt.colorbar()


def show_clusters(labeled_grid):
    # Setting zeros to -1 so that the "empty" slots are always the same color
    copy_labeled = np.copy(labeled_grid)
    copy_labeled[copy_labeled == 0] = -1
    plt.figure()
    plt.imshow(copy_labeled, cmap="tab10")
    del copy_labeled
