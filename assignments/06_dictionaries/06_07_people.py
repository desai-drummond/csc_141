# Desai Drummond
# Chapter 6: Dictionaries
# Exercise 7: People

person = {
    "first_name": "Desai",
    "last_name": "Drummond",
    "age": 19,
    "city": 'Wilmington'
}

person2 = {
    "first_name": "Marcus",
    "last_name": "Johnson",
    "age": 20,
    "city": 'Los Angeles'
}

person3 = {
    "first_name": "Jordan",
    "last_name": "Smith",
    "age": 21,
    "city": 'New York'
}

people = [person, person2, person3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Name: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}\n")