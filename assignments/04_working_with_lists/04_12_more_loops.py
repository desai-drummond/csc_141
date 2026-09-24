# Desai Drummond
# Chapter 4 more loops

# Print list of foods 

my_foods = ["Pizza", "Burger", "Pasta","Ice Cream"]
for food in my_foods:
    print(food)

# Make a copy of list for friends foods
friends_foods = my_foods[:]


# Add a new list to original list 
my_foods.append("Tacos")

# Add a new food to friend's list
friends_foods.append("Sushi")

# Print both lists
print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friends_foods:
    print(food)

# End of program