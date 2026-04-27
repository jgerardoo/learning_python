user_name = "Jesse"
user_last_name = "Varela"
user_gender = "Male"
user_location = "Katy Texas"
user_item = "phone"
user_item_2 = "TABLET"
user_description = "this is a description"
color_list = ["blue", "red", "brown", "white"]
line_with_space = "    Space."

# String slicing
print(user_name[2:4])
print(user_last_name[:3])
print(user_last_name[3:])
print(user_last_name[0:5:2])
print(user_last_name[::-1])
print()

# ----- String Methods -----
# upper()
print(user_name)
print(user_name.upper())
print()

# lower()
print(user_last_name)
print(user_last_name.lower())
print()

# replace (old, new)
print(user_location)
print(user_location.replace("Katy Texas", "Orlando Florida"))
print()

# Split (separator)
print(user_location)
print(user_location.split())
print()

# Join (iterable)
print(color_list)
print(' '.join(color_list))
print('.'.join(color_list))
print(' | '.join(color_list))
print()

# startswith (prefix)
print(user_name)
print(user_name.startswith("Je"))
print(user_name.startswith("Ga"))
print()

# endswith (suffix)
print(user_last_name)
print(user_last_name.endswith("to"))
print(user_last_name.endswith("la"))
print()

# find (substring)
print(user_location)
print(user_location.find("Katy"))   # Returns the index of the argument found
print(user_location.find("Texas"))  # Returns the index of the argument found
print(user_location.find("x"))      # Returns the index of the argument found
print(user_name.find("Katy"))       # Returns a -1 if not found
print()

# count (substring)
print(user_location)
print(user_location.count("a"))
print(user_location.count("t"))
print(user_location.count("T"))
print(user_location.count("z"))
print()

# capitalize()
print(user_item)
print(user_item.capitalize())
print()

# isupper()
print(user_name)
print(user_name.isupper())
print(user_item_2)
print(user_item_2.isupper())
print()

# islower()
print(user_item)
print(user_item.islower())
print(user_item_2)
print(user_item_2.islower())
print()

# title()
print(user_description)
print(user_description.title())
print()

# strip()
print(line_with_space)
print(line_with_space.strip())
print()

# in
print("e" in "blueberry")
print("a" in "blueberry")
print("blue" in "blueberry")
print("blue" in "strawberry")
print("e" in "blueberry" and "e" in "carrot")
print("e" in "blueberry" and not "e" in "carrot")
print()

# .format()
def poem_title_card(title, poet):
  return "The poem {} is written by {}".format(title, poet)
print(poem_title_card("I Hear America Singing", "Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
  return poem_desc
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"
my_beard_description = poem_description(publishing_date, author, title, original_work)
print(my_beard_description)
