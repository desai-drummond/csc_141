# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import plotly.express as px
from die import Die

# Create two 8-sided dice.
die_1 = Die(8)
die_2 = Die(8)

# Roll the dice 1,000 times and store the results.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

    # Analyze the results.
    frequencies = []
    max_result = die_1.num_sides + die_2.num_sides

    for value in range(2, max_result + 1):
        frequency = results.count(value)
        frequencies.append(frequency)

        # Visualize the results.
        title = "Results of Rolling Two D8 Dice 1,000 Times"
        labels = {'x': 'Result', 'y': 'Frequency'}
        fig = px.bar(x=list(range(2, max_result + 1)), y=frequencies, title=title, labels=labels)
        
        fig.show()
