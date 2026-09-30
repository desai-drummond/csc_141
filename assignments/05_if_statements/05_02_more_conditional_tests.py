# Desai Drummond
# Chapter 5 More Conditional Tests

# 1. Tests for equality and inequality with strings

favorite_sport = 'football'
print("1. Is favorite_sport equal to 'football'? I predict True.")
print(favorite_sport == 'football')

print("\n2. Is favorite_sport equal to 'basketball'? I predict False.")
print(favorite_sport == 'basketball')

print("\n3. Is favorite_sport not equal to 'soccer'? I predict True.")
print(favorite_sport != 'soccer')

print("\n4. Is favorite_sport not equal to 'football'? I predict False.")
print(favorite_sport != 'football')

# 2. Tests using the lower() method

name = 'Desai'
print("\n5. Is name.lower() equal to 'desai'? I predict True.")
print(name.lower() == 'desai')

print("\n6. Is name.lower() equal to 'Desai'? I predict False.")
print(name.lower() == 'Desai')

print("\n7. Is name.lower() not equal to 'football'? I predict True.")
print(name.lower() != 'football')

print("\n8. Is name.lower() not equal to 'desai'? I predict False.")
print(name.lower() != 'desai')

# 3. Numerical tests

age = 19 
print("\n9. Is age equal to 19? I predict True.")
print(age == 19)

print("\n10. Is age equal to 20? I predict False.")
print(age == 20)

print("\n11. Is age not equal to 18? I predict True.")
print(age != 18)

print("\n12. Is age not equal to 19? I predict False.")
print(age != 19)

print("\n13. Is age greater than 18? I predict True.")
print(age > 18)

print("\n14. Is age greater than 19? I predict False.")
print(age > 19)

print("\n15. Is age less than 20? I predict True.")
print(age < 20)

print("\n16. Is age less than 19? I predict False.")
print(age < 19)

# 4. Tests using the 'and' keyword
gpa = 3.4 
football_player = True

print("\n21. Is GPA greater than 3.0 AND football_player True? I predict True.")
print(gpa > 3.0 and football_player == True)

print("\n22. Is GPA greater than 3.5 AND football_player True? I predict False.")
print(gpa > 3.5 and football_player == True)

# 5. Tests using the 'or' keyword 
sport = 'football'

print('\n23. Is sport football OR basketball? I predict True.')
print(sport == 'football' or sport == 'basketball')

print('\n24. Is sport soccer OR baseball? I predict False.')
print(sport == 'soccer' or sport == 'baseball')

# 6. Test whether an item is in a list
sports = ['football', 'basketball', 'soccer', 'baseball']

print("\n25. Is 'football' in the sports list? I predict True.")
print('football' in sports)

print("\n26. Is 'tennis' in the sports list? I predict False.")
print('tennis' in sports)

# 7. Test whether an item is NOT in a list

print("\n27. Is 'tennis' NOT in the sports list? I predict True.")
print('tennis' not in sports)

print("\n28. Is 'football' NOT in the sports list? I predict False.")
print('football' not in sports)