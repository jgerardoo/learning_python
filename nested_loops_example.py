project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
# Using a for or while loop to get each
for team in project_teams:
  print(team)

# Using a nested loop to print each individual person
for team in project_teams:          # Loop through each sublist
    for person in team:             # Loop elements in each sublist
        print(person)
print("----------")

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
print(sales_data)
scoops_sold = 0
for location in sales_data:
  print(location)
  for flavor in location:
    scoops_sold += flavor
print(scoops_sold)
print("----------")