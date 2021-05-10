from setup import get_filled_grid
from display import show_grid, show_clusters
from clustering import get_labeled_clusters


def main():
    a="hello"

if __name__ == "__main__":
    main()


grid = get_filled_grid((10,10),0.5)
show_grid(grid)
b = get_labeled_clusters(grid)
show_clusters(b)