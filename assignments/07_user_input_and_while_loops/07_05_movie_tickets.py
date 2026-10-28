# Desai Drummond
# Chapter 7: User Input and While Loops
# Exercise 5: Movie Tickets

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)

    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 13:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")