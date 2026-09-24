# Desai Drummond
# Chapter 4 buffet

# Create a tuple containing five foods offered at the buffet
buffet_foods = ("Pizza", "Burger", "Pasta", "Ice Cream", "Salad")

# Use a loop to print each food on the original menu
for food in buffet_foods:
    print(food)

# Try to change one of the foods in the tuple
# Python will reject this because tuples cannot be changed
# buffet_foods[0] = "Tacos"  # This will cause an error

# The restaurant changes its menu by replacing two foods
# Rewrite the entire tuple with the new menu
buffet_foods = ("Tacos", "Burger", "Pasta", "Ice Cream", "Sushi")

# Use a loop to print each food on the updated menu
for food in buffet_foods:
    print(food)

# End of program 
