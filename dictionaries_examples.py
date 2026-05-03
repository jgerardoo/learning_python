# Dictionaries
# data set of key-value pairs. It maps pieces of data to each other
# and allows quick access to values associated with keys.

# Syntax for creating an empty dictionary:
dictionary_name = {}
print(dictionary_name)

# The dict() function can also be used:
dictionary_name_2 = dict()
print(dictionary_name_2)

# Syntax for creating a dictionary with entries:
dictionary_name_3 = {"key1": "value1",  "key2": "value2",  "key3": "value3"}
print(dictionary_name_3)
coffee_shop = {"cold brew": 3.50, "latte": 4.25, "cappuccino": 3.99}
print(coffee_shop)
print()

# Accessing Items in a Dictionary
print(coffee_shop["cold brew"])

# Adding Items to a Dictionary (1 key:value at the time)
coffee_shop["espresso"] = 4.72
print(coffee_shop)

# Changing items in a Dictionary
coffee_shop["cold brew"] = 4.5
print(coffee_shop)

# Removing items from a Dictionary using the del statement
del coffee_shop["espresso"]
print(coffee_shop)
print()

# Add multiple key:value entries
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print(sensors)
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)
print()

# Merge two dictionaries using the .update() method
dictionary_name.update(dictionary_name_2)
print(dictionary_name)
print()

# Clear a dictionary
print(dictionary_name_3)
dictionary_name_3.clear()
print(dictionary_name_3)
print()

# Dic comprehensions
## We have two lists that we want to combine into a dictionary
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
students = {key:value for key, value in zip(names, heights)}
print(students)
print()

# Check if the key exists in the dictionary
# to avoid getting a KeyError
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights)

key_to_check = "Landmark 81"
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# .get() method
print(building_heights.get("Shanghai Tower"))
print(building_heights.get("My House"))

## specify a value to return if the key doesn’t exist
print(building_heights.get('Mt Olympus', 0))
print(building_heights.get('Kilimanjaro', 'No Value'))
print()

# Delete a key from a dictionary
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle)
print(raffle.pop(298787, "No Prize"))
print(raffle)
print(raffle.pop(100000, "No Prize"))
print(raffle)
print(raffle.pop(412123, "No Prize"))
print(raffle)
print()

# Get all keys using .list()
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(test_scores)
for student in test_scores.keys():
 print(student)
print()

# Get all keys using .keys()
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
print(user_ids)
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
print(num_exercises)

users = user_ids.keys()
print(users)
lessons = num_exercises.keys()
print(lessons)
print()

# Get all values
print(test_scores)
for score_list in test_scores.values():
 print(score_list)
print()

test_scores_values = test_scores.values()
print(test_scores_values)
print()

# Iterate through the values in a dictionary and add each value to a variable
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
print(num_exercises)
total_exercises = 0
for value in num_exercises.values():
  total_exercises += value
print(f"The number of total exercises is: {total_exercises}")
print()

# Get all items using .items()
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
print(biggest_brands)
for company, value in biggest_brands.items():
    print(f"{company} has a value of {value} billion dollars")
print()

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
print(pct_women_in_occupation)
for position, pct in pct_women_in_occupation.items():
  print(f"Women make up {pct} percent of {position}s.")
print()

# Exercise
tarot = { 1:"The Magician", 2:"The High Priestess", 3:"The Empress", 4:"The Emperor", 5:"The Hierophant", 6:"The Lovers", 7:"The Chariot"}
print(tarot)
## Pop the value assigned to the key 2 out of the tarot dictionary and assign it as the value of the "past" key of fortune
fortune = {}
fortune["past"] = tarot.pop(2)
## Pop the value assigned to the key 4 out of the tarot dictionary and assign it as the value of the "present" key of fortune
fortune["present"] = tarot.pop(4)
## Pop the value assigned to the key 6 out of the tarot dictionary and assign it as the value of the "future" key of fortune
fortune["future"] = tarot.pop(6)
## Iterate through the items in the fortune dictionary
for key, value in fortune.items():
  print(f"Your {key} is the {value} card.")
print(tarot)
print()