from scipy.ndimage import label
import numpy as np


def get_labeled_clusters(grid):
    labeled_grid, nb_of_clusters = label(grid)
    return labeled_grid


def get_clusters_in_a_col(labeled_grid, col_index):
    col = labeled_grid[:, col_index]
    clusters_in_col = set(col)
    clusters_in_col.discard(0)
    return clusters_in_col


def get_clusters_spanning_from_left_to_right(labeled_grid):
    first_col_clusters = get_clusters_in_a_col(labeled_grid, 0)
    last_col_clusters = get_clusters_in_a_col(labeled_grid, -1)
    return set.intersection(first_col_clusters, last_col_clusters)


def is_a_cluster_spanning_left_to_right(labeled_grid):
    clusters = get_clusters_spanning_from_left_to_right(labeled_grid)
    if len(clusters) > 0:
        return True
    else:
        return False


def get_clusters_number_and_counts(labeled_grid):
    clusters, counts = np.unique(labeled_grid, return_counts=True)

    # remove the 0 cluster from clusters and counts
    zero_index = np.where(clusters == 0)[0][0]
    clusters = np.delete(clusters, zero_index)
    counts = np.delete(counts, zero_index)

    return clusters, counts


def get_biggest_cluster(labeled_grid):
    clusters, counts = get_clusters_number_and_counts(labeled_grid)
    max_value_index = np.argmax(counts)
    return clusters[max_value_index]


def get_descriptive_stats_about_clusters(labeled_grid):
    clusters, counts = get_clusters_number_and_counts(labeled_grid)
    nb_clusters = len(clusters)
    average_cluster_size = np.mean(counts)
    median_cluster_size = int(np.median(counts))
    biggest_cluster_size = np.max(counts)
    smallest_cluster_size = np.min(counts)

    return {
        "nb_clusters": nb_clusters,
        "average_cluster_size": average_cluster_size,
        "median_cluster_size": median_cluster_size,
        "biggest_cluster_size": biggest_cluster_size,
        "smallest_cluster_size": smallest_cluster_size,
    }
