# Lists
# Begins and ends with square brackets [ ]
# Each item is separated by a comma (,)
sports_list = ["Soccer", "Golf", "Basketball", "Tennis"]
heights = [61, 70, 67, 64]
stuff_list = ["Jesse", 70, 6.7, True]
empty_list = []             # values can be added later based on some other input

# List index
print(sports_list)
print(sports_list[2])
print(sports_list[-1])
sports_list[1] = "Hockey"
print(sports_list)
print()

# .append()
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)
print()

# .remove()
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
print(shopping_line)
shopping_line.remove("Chris")
print(shopping_line)
print()
shopping_line_2 = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
print(shopping_line_2)
shopping_line_2.remove("Chris")     # removes only the first instance of the matching element
print(shopping_line_2)
print()

# Two-Dimensional (2D) Lists
names_heights = [["John", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
print(names_heights)
sam_height = names_heights[2][1]
vik_height = names_heights[-1][-1]
print(sam_height)
print(vik_height)
print()
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
print(class_name_hobbies)
class_name_hobbies[0][1] = "Meditation"
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)
print()
incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)
print()

# Combine two different list into one 2D list nesting lists as rows
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
print(toppings)
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)
toppings_and_prices = [toppings, prices]
print(toppings_and_prices)
print()

# Combine two different list into one 2D list pairing elements (column-wise)
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
print(toppings)
prices = [2, 6, 1, 3, 2, 7, 2]
print(prices)
toppings_and_prices = list(map(list, zip(toppings, prices)))
print(toppings_and_prices)
print()

# Remove a value from a 2D list
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[1].remove(False)
print(customer_data)
customer_data[0].remove("Small")
print(customer_data)
print()

# Combine two 2D lists
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
print()

# List methods
# .insert()
store_line = ['Karla', 'Max', 'Martim', 'Isabella']
print(store_line)
store_line.insert(2, "Victor")
print(store_line)
print()

# .pop()
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
print(cs_topics)
cs_topics.pop()
print(cs_topics)
cs_topics.pop(2)
print(cs_topics)
print()

# range()
my_range = range(10)
print(my_range)
print(list(my_range))
print()
zero_to_seven = range(0,8)
print(list(zero_to_seven))
print()

my_range_2 = range(2,11)
print(list(my_range_2))
print()

my_range_3 = range(3,16,3)
print(list(my_range_3))
print()

my_range4 = range(1, 100, 10)
print(list(my_range4))
print()

# len()
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(len(my_list))
print()
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
print(long_list)
long_list_len = len(long_list)
print(long_list_len)
print()

# slicing lists
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters)
sliced_letters_list = letters[2:6]
print(sliced_letters_list)
print()
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books.csv"]
print(suitcase)
last_two_elements = suitcase[-2:]
print(last_two_elements)
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)
print()

# Counting in a List
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
print(letters)
num_i = letters.count("i")
num_p = letters.count("p")
print(num_i)
print(num_p)
print()
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
print(number_collection)
num_pairs = number_collection.count([100, 200])
print(num_pairs)
print()

# Sorting a list
# .sort()
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
print(addresses)
addresses.sort()
print(addresses)
print()
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
print(names)
names.sort()
print(names)
print()
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
print(cities)
cities.sort(reverse = True)
print(cities)
print()

# combining/nesting lists using the zip() function
names_2 = ["Jenny", "Alexus", "Sam", "Grace"]
heights_2 = [61, 70, 67, 64]
print(names_2)
print(heights_2)
names_and_heights = zip(names_2, heights_2)
print(names_and_heights)
print(type(names_and_heights))
# this prints "<zip object at 0x7f1631e86b48>" so we need to make this object a list using list()
names_and_heights = list(names_and_heights)
print(names_and_heights)
print(type(names_and_heights))
print()

# combine two simple lists using a for loop
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_B:
  students_period_A.append(student)
  print(f"Adding {student} to students_period_A")
print(students_period_A)