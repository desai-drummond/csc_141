# Desai Drummond
# Chapter 5 Checking Usernames
# This program contains some useful commands using lists, for loops, and if statemnts

current_users = ['Colton', 'Desai', 'Robert', 'Zach']
new_users = ['Admin', 'Jace', 'Desai', 'Robert', 'Tim']

for user in current_users:
    if user in new_users:
        print(f'{user} IS in both lists')
    else:
        print(f'{user} is NOT in both lists')