# Desai Drummond
# Chapter 3

teams = ["Eagles", "Cowboys", "Ravens", "Cheifs", "Bills"]
print(teams) 

print(teams[0])
print(teams[-1])

teams.append("Dolphins")
print(teams)

teams.insert(2, "Lions")
print(teams)

del teams[2]
print(teams)

removed_team = teams.pop()
print("Removed:", removed_team)
print(teams)

teams.remove("Cowboys")
print(teams)

print(sorted(teams))
print(sorted(teams, reverse=True))

teams.reverse()
print(teams)

teams.reverse()
print(teams)

teams.sort()
print(teams)

teams.sort(reverse=True)
print(teams)

print("There are", len(teams), "teams in the list.")