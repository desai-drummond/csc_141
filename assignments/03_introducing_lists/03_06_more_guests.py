# Desai Drummond
# Chapter 3

guests = ["Michael Jordan", "Lebron James", "Stephen Curry", "Kobe Bryant",]

print(f"Hello {guests[0]}, I would like to invite you to dinner.")
print(f"Hello {guests[1]}, I would like to invite you to dinner.")
print(f"Hello {guests[2]}, I would like to invite you to dinner.")
print(f"Hello {guests[3]}, I would like to invite you to dinner.")

print(f"\nGood news! I have found a bigger dinner table, so I can invite more guests.\n")

guests.insert(0, "Shaquille O'Neal")
guests.insert(2, "Kawhi Leonard")
guests.append("Kevin Durant")

print("\nNew dinner invitations:\n")

for guest in guests:
    print("You are invited to dinner, " + guest + ".")
    