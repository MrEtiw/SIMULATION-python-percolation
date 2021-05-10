from scipy.ndimage import label

def get_labeled_clusters(grid):
    labels, nb_of_clusters = label(grid)
    return labels