from matplotlib import pyplot as plt
import numpy as np


from clustering import get_biggest_cluster


def show_grid(grid):
    plt.figure()
    plt.imshow(grid, cmap="binary")
    plt.colorbar()
    return None


def show_clusters(labeled_grid):
    # Setting zeros to -1 so that the "empty" slots are always the same color
    copy_labeled = np.copy(labeled_grid)
    copy_labeled[copy_labeled == 0] = -1
    plt.figure()
    # plt.imshow(copy_labeled, cmap="tab10")
    plt.imshow(copy_labeled)
    del copy_labeled
    return None


def show_biggest_cluster(labeled_grid):

    fill_empty_value = -100
    fill_biggest_value = 100
    fill_others_value = 1

    copy_labeled = np.copy(labeled_grid)
    biggest_cluster_number = get_biggest_cluster(copy_labeled)

    # biggest cluster
    biggest_positions = copy_labeled == biggest_cluster_number

    # empty positions
    empty_positions = copy_labeled == 0

    # other positions
    other_positions = np.invert(empty_positions + biggest_positions)

    copy_labeled[biggest_positions] = fill_biggest_value
    copy_labeled[empty_positions] = fill_empty_value
    copy_labeled[other_positions] = fill_others_value

    plt.figure()
    plt.imshow(copy_labeled)

    del copy_labeled
    return None
