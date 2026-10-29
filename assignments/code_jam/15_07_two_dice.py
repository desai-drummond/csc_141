# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import matplotlib.pyplot as px
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []

for roll_num in range(1000):
    result = die_1.ROLL() + die_2.roll() + die_3.roll()
    results.append(result)

    frequencies = []

    for value in range(3, 19):
        frequency = results.count(value)
        frequencies.append(frequency)

        title = "Results of Rolling Three Dice 1,000 Times"
        labels = {'x': 'Result', 'y': 'Frequency'}

        fig = px.bar(x=list(range(3, 19)), y=frequencies, title=title, labels=labels)

        fig.show()