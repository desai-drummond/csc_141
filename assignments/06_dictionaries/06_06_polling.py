# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 6: Polling

favorite_lanugages = {
    'Desai': 'Python',
    'sarah': 'JavaScript',
    'edward': 'rust',
    'phil': 'python',
}

people = ['Desai', 'sarah', 'edward', 'phil', 'michael', 'jessica']

for person in people:
    if person in favorite_lanugages:
        print(f"Thank you for taking the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")
        