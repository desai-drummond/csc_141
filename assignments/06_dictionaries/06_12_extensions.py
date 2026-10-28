# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 12: Extensions

cities = {
    'new_york': {
        'country': 'United States',
        'population': 8419600,
        'fact': 'New York City is known as the "Big Apple".',
        'language': 'English',
        'famous_food': 'Pizza',
        'visited': False    
    },
    'paris': {
        'country': 'France',
        'population': 2148000,
        'fact': 'Known as the City of Light.',
        'language': 'French',
        'famous_food': 'Croissant',
        'visited': False
    },
    'tokyo': {
        'country': 'Japan',
        'population': 13960000,
        'fact': 'It has one of the busiest train systems in the world.',
        'language': 'Japanese',
        'famous_food': 'Sushi',
        'visited': True
    },
    'miami': {
        'country': 'United States',
        'population': 467963,
        'fact': 'Miami is known for its beautiful beaches and vibrant nightlife.',
        'language': 'English',
        'famous_food': 'Cuban Sandwich',
        'visited': False
    },
    'dubai': {
        'country': 'United Arab Emirates',
        'population': 3331420,
        'fact': 'Dubai is famous for its modern architecture and luxury shopping.',
        'language': 'Arabic',
        'famous_food': 'Shawarma',
        'visited': False
    },

}

for city, information in cities.items():
    country = information['country']
    population = information['population']
    fact = information['fact']
    language = information['language']
    famous_food = information['famous_food']
    visited = information['visited']

    print(f"\nCity: {city.title()}")
    print(f"Country: {country}")
    print(f"Population: {population}")
    print(f"Fact: {fact}")
    print(f"Language: {language}")
    print(f"Famous Food: {famous_food}")
    print(f"Visited: {'Yes' if visited else 'No'}")

    print("\nSummary:")
    print("These five cities have different cultures , foods, and famous attractions.")
    print("I have marked Tokyo as visited and the other cities as not visited. ")
    print(" I would like to exlore mnore of these places in the future.")