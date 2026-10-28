# Desai Drummond 
# Chapter 6: Dictionaries
# Exercise 5: Rivers

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states',
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print the name of each river
print("\nRivers:")
for river in rivers:
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())