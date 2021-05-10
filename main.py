from setup import get_filled_grid
from display import show_grid, show_clusters
from clustering import get_labeled_clusters, is_cluster_spanning_left_to_right


def main():
    a = "hello"


if __name__ == "__main__":
    main()


grid = get_filled_grid((10, 10), 0.7)
show_grid(grid)
b = get_labeled_clusters(grid)
show_clusters(b)
c = is_cluster_spanning_left_to_right(b)

## Next:
# descriptive stats about clusters (nb per cluster, average, median, biggest, etc.)

