# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 11: Cities

cities = {
    'Wilmington': {
        'country': 'United States',
        'population': 120000,
        'fact': 'Wilmington is known for its beautiful riverfront and historic architecture.'
    },
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'It is known as the City of Light.'
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13960000,
        'fact': 'It has one of the busiest train systems in the world.'
    }
}

for city, information in cities.items():
    country = information['country']
    population = information['population']
    fact = information['fact']
    
    print(f"\nCity: {city.title()}")
    print(f"Country: {country}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")