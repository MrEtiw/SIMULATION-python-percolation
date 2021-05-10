from scipy.ndimage import label
import numpy as np


def get_labeled_clusters(grid):
    labels, nb_of_clusters = label(grid)
    return labels


def get_clusters_first_col(labeled_grid):
    first_col = labeled_grid[:, 0]
    first_col_clusters = set(first_col)
    first_col_clusters.discard(0)
    return first_col_clusters


def get_clusters_last_col(labeled_grid):
    last_col = labeled_grid[:, -1]
    last_col_clusters = set(last_col)
    last_col_clusters.discard(0)
    return last_col_clusters


def get_clusters_spanning_from_left_to_right(labeled_grid):
    first_col_clusters = get_clusters_first_col(labeled_grid)
    last_col_clusters = get_clusters_last_col(labeled_grid)
    return set.intersection(first_col_clusters, last_col_clusters)


def is_cluster_spanning_left_to_right(labeled_grid):
    clusters = get_clusters_spanning_from_left_to_right(labeled_grid)
    if len(clusters) > 0:
        return True
    else:
        return False
