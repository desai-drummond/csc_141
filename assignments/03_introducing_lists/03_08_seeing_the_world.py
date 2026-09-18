# Desai Drummond
# Chapter 3

places = ["Paris", "Dubai", "New York City", "Sydney", "Rio de Janeiro"]

# Original order
print(places)

# Alphabetical order without changing the list
print(sorted(places))

#Show the original order
print(places)

# Reverse alphabetical order without changing the list
print(sorted(places, reverse=True))

# Show the original order again
print(places)

# Reverse the order of the list
places.reverse()
print(places)

# Reverse the order of the list again to get back to the original order
places.reverse()
print(places)

# Permanently sort the list alphabetically
places.sort()
print(places)

# Permanently sort the list in reverse alphabetical order
places.sort(reverse=True)
print(places)
