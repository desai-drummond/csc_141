# Desai Drummond
# Chapter 7: User Input and While Loops
# Exercise 2: Restaurant Seating

people = input("How many people are in your dinner group?")
people = int(people)

if people > 11:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")