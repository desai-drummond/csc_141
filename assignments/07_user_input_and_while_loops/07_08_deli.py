# Desai Drummond
# Chapter 7: User Input and While Loops
# Exercise 8: Deli

sandwich_orders = ['tuna', 'ham', 'turkey', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

    print("\nThe following sandwiches have been made:")
    for sandwich in finished_sandwiches:
        print(f"- {sandwich}")