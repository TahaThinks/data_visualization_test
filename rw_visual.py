import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Make a random walk.
while True:
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots() # Create a figure containing one single axis
    
    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.sm.Blues, edgecolors = 'none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break