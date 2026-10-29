# Desai Drummond
# Chapter 15: Code Jam (Cubes)

import plotly.express as px
from die import Die

die = Die()

results = [die.roll() for roll_num in range(1000)]

frequencies = [results.count(value) for value in range(1, die.num_sides + 1)]

title = "Results of Rolling One d6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency'}

fig = px.bar(x=list(range(1, die.num_sides + 1)), y=frequencies, title=title, labels=labels)
fig.show()