# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import matplotlib.pyplot as plt
from die import Die

die = Die()

results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

plt.bar(range(1, die.num_sides + 1), frequencies)

plt.title("Results of Rolling One d6 1,000 Times")
plt.xlabel("Result")
plt.ylabel("Frequency")

plt.show()


import plotly.express as px
from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

fig = px.scatter(x=rw.x_values, y=rw.y_values, title="Random Walk", labels={'x': 'X Values', 'y': 'Y Values'})
fig.show()