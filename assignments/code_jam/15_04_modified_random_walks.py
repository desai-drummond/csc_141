# Desai Drummond
# Chapter 15: Code Jam (Cubes)

from random import choice, randint 

# Choose x and y directions.
x_direction = choice([1, -1])
y_direction = choice([1, -1])

# Choose the distance for each step.
x_distance = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y_distance = [0, 1, 2, 3, 4, 5, 6, 7, 8]

x_step = choice(x_direction * choice(x_distance))
y_step = choice(y_direction * choice(y_distance))