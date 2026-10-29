# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import plotly.express as ps
from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

    frequencies = []

    for value in range(1, 37):
        frequency = results.count(value)
        frequencies.append(frequency)

        title = "Results of Rolling Two Dice 1,000 Times"
        labels = {'x': 'Result', 'y': 'Frequency'}

        fig = ps.bar(x=list(range(1, 37)), y=frequencies, title=title, labels=labels)

        fig.show()