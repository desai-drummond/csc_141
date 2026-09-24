# Desai Drummond
# Chapter 4 my pizzas your pizzas

# Original list of my favorite pizzas 
pizzas = ["Cheese", "Beef pepperoni", "Barbecue Chicken"]

# Make a copy of the list for your friend's favorite pizzas
your_pizzas = pizzas[:]

# Add a new pizza to each list
pizzas.append("Sausage")
your_pizzas.append("Buffalo Chicken")

# Print both lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in your_pizzas:
    print(pizza)

# End of program 