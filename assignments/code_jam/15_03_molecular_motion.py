# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new random walks as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5_000)
    rw.fill_walk()

    # Plot the points as a line.
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.plot(rw.x_values, rw.y_values, linewidth=1)  

    # Show the plot.
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break   