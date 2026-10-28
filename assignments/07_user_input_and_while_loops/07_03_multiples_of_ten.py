# Desai Drummond
# Chapter 7: User Input and While Loops
# Exercise 3: Multiples of Ten

number = input("Enter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# Enter a number: 50
# 50 is a multiple of 10.

# Enter a number: 33
# 33 is not a multiple of 10.