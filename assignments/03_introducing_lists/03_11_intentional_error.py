# Desai Drummond
# Chapter 3

# 3.11 Intentional Error
# This program first has an intentional index error, then fixes it.

players = ["Hurts", "Brown", "Smith"]

print(players[2]) # This will print "Smith" (there is no index 3)


# After seeing the error, here is the correct version of the program:

players = ["Hurts", "Brown", "Smith"]

print(players[2]) # This correctly prints the last player
print("The last player on the list is:", players[2])