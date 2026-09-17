# Desai Drummond
# Chapter 3

guests = ["Lebron James", "Michael Jordan", "Tom Brady", "Shaquille O'Neal"]

print(f"Hello {guests[0]}, I would like to invite you to dinner.")
print(f"Hello {guests[1]}, I would like to invite you to dinner.")
print(f"Hello {guests[2]}, I would like to invite you to dinner.")
print(f"Hello {guests[3]}, I would like to invite you to dinner.")


print(f"\nUnfortunately, {guests[2]} cannot make it to dinner.\n")

# Replacing the guest who cannot make it with a new guest
guests[2] = "Stephen Curry"

print(f"Hello {guests[0]}, I would like to invite you to dinner.")
print(f"Hello {guests[1]}, I would like to invite you to dinner.")
print(f"Hello {guests[2]}, I would like to invite you to dinner.")
print(f"Hello {guests[3]}, I would like to invite you to dinner.")