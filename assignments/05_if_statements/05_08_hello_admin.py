# Desai Drummond
# Chapter 5 Hello Admin
# This program contains some useful commands using lists, for loops, and if statements



users = ['admin', 'Colton', 'Desai', 'Robert']

for user in users:
    if user == 'admin':
        print('Hello Administrator, you are special.')
    else:
        print(f"Hello {user}, thank you for logging in.")