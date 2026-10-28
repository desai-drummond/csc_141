# Desai Drummond 
# Chapter 7: User Input and While Loops
# Exercise 10: Dream Vacation

dream_vacation = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    vacation = input("If you could visit one place in the world, where would you go")

dream_vacation[name] = vacation

repeat = input("Would you like to let another person respond? (yes/no) ")
if repeat == 'no':
    polling_active = False

print("\n--- Poll Results ---")
for name, vacation in dream_vacation.items():
    print(f"{name} would like to visit {vacation}.")