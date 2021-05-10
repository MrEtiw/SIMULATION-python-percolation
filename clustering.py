from scipy.ndimage import label


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


def is_cluster_spanning_left_to_right(labeled_grid):
    clusters = get_clusters_spanning_from_left_to_right(labeled_grid)
    if len(clusters) > 0:
        return True
    else:
        return False
