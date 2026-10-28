# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 10: Favorite Numbers

favorite_numbers = {
    'Desai': [7, 10, 12],
    'Michael': [5, 8],
    'Chris': [3, 15],
    'Jordan': [2, 9],
    'Kevin': [4, 11],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")