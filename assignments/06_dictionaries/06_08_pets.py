# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 8: Pets

pets = {
    'animal1': 'dog',
    'owner': 'Desai',
}

pet2 = {
    'animal2': 'cat',
    'owner': 'Michael',
}

pet3 = {
    'animal3': 'fish',
    'owner': 'Chris',
}

pets = [pets, pet2, pet3]

for pet in pets:
    print(f"\n{pet['owner'].title()} has a {pet['animal1'] if 'animal1' in pet else pet['animal2'] if 'animal2' in pet else pet['animal3']}.")