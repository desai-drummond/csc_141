# Desai Drummond
# Chapter 3

guests = ["Kevin Durant", "Michael Jordan", "Kobe Bryant", "Lebron James", "Stephen Curry", "Giannis Antetokounmpo"]

print(" I found out my new dinner table won't arrive in time.")
print("I can invite only two guests for dinner.\n")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\n" + guests[0] + ", you're still invited to dinner.")
print(guests[1] + ", you're still invited to dinner.")

print("I am inviting " + str(len(guests)) + " people to dinner.")