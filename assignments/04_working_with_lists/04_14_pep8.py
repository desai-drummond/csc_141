# Desai Drummond 
# Chapter 4 PEP 8 example

#PEP 8 is Python's official style guide for coding conventions, authored by Guido van Rossum, Barry Warsaw, and Alyssa Coghlan. The core philosophy behind PEP 8 is 
# that code is read far more often than it is written, making readability and consistency paramount.


# Program 1
pizzas = ['pepperoni', 'cheese', 'sausage']
for pizza in pizzas:
    print(pizza)

# End of program


# Program 2
pizzas = ['pepperoni', 'cheese', 'sausage']

friends_pizzas = pizzas[:]

pizzas.append('buffalo chicken')
friends_pizzas.append('veggie')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)

# End of program    


# Program 3
buffet_foods = ('Chicken', 'rice', 'salad', 'pizza')

print("The original buffet foods are:")
for food in buffet_foods:
    print(food)

buffet_foods = ('Steak', 'rice', 'salad', 'tacos', 'dessert')

print("\nThe updated buffet foods are:")
for food in buffet_foods:
    print(food)

# End of program
