# Desai Drummond
# Chapter 15: Cubes

import matplotlib.pyplot as plt

# Generate the first 5,000 cubic numbers
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

# Create a scatter plot with a colormap
plt.scatter(x_values, y_values, c=y_values, cmap='viridis', s=10)

plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.show()