from setup import get_filled_grid
from display import show_grid, show_clusters, show_biggest_cluster
from clustering import (get_labeled_clusters,
                        is_a_cluster_spanning_left_to_right,
                        get_descriptive_stats_about_clusters,
                        get_biggest_cluster)
from matplotlib import pyplot as plt
import numpy as np


def main():
    plt.close("all")


if __name__ == "__main__":
    main()


grid = get_filled_grid((500, 500), 0.55)
b = get_labeled_clusters(grid)
show_biggest_cluster(b)



### Next step = fill a grid with p=0.01
## Then, take that same filled grid and add ones until we reached a total prop of 0.02 of being filled
# That way, we can get a visualisation of clusters merging with each others


### Next next step = run many times for a same p a simulation and calculate the propability of percolation for a
# given value of p (the probability for a single position to be filled)









