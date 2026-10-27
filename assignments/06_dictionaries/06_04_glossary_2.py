# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 4: Glossary 2

glossary = {
    'variable': 'A name that stores a value.',
    'string': 'A sequence of characters.',
    'list': 'A collection of items stored in order.',
    'loop': 'A way to repeat a block of code.',
    'dictionary': 'A collection of key-value pairs.',
    'integer': 'A whole number.',
    'float': 'A number with a decimal point.',
    'boolean': 'A value that is either True or False.',
    'function': 'A reusable block of code that performs a task.',
    'comment' : 'A note in code that Python does not execute.'
}

for word, definition in glossary.items():
    print(f"{word.capitalize()}: {definition}")