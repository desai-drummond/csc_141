# Desai Drummond
# Chapter 7: User Input and While Loops
# Exercise 6: Three Exits

# Method 1: Conditional test in the while statement 
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished. "

topping = ""
while topping != 'quit':
    topping = input(prompt)
    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")

# Method 2: Active variable to control the loop
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")

# Method 3: Use a break statement
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")