# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 9: Favorite Places

favorite_places = {
    'Desai': ['Miami', 'New York', 'Dubai'],
    'Michael': ['Los Angeles', 'Paris'],
    'Chris': ['Tokyo', 'London', 'Atlanta'],
}

for name, places in favorite_places.items():
    print(f"\n{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
        