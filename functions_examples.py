# Define a function
def hello():
  print("Hello, world!")
# Call the function
hello()
print()

# Define a function with parameters
def generate_trip_instructions(location):
  print(f"Looks like you are planning a trip to visit {location}")
  print("You can use the public subway system to get to " + location)
generate_trip_instructions("Central Park")
print()

# Define a function with multiple parameters
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price
  print(f"The total of your trip will be ${trip_total}")
  return trip_total
calculate_expenses(200, 100, 100, 5)
print()

# Types of arguments
def trip_planner(first_destination, second_destination, final_destination = "Italy"):
  print("Here is what your trip will look like!")
  print(f"First, we will stop in {first_destination}, then {second_destination}, and lastly {final_destination}")

## Positional arguments
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
print()

## Keyword arguments
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")
print()

## Default arguments
trip_planner("Spain", "Portugal")
print()

# Return a value from a function and store that value in a variable
def add(a, b):
  result = a + b
  return result
addition = add(10, 20)
print(addition)
print()

## Return multiple values
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  return first, second, third
most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()
print(most_popular1)
print(most_popular2)
print(most_popular3)
print()

weather_data = ['Sunny', 'Cloudy', 'Raining', 'Snowing']
def three_day_weather_report(weather):
  first_day = "Tomorrow the weather will be " + weather[0]
  second_day = "The following day it will be " + weather[1]
  third_day = "Two days from now it will be " + weather[2]
  fourth_day = "Three days from now it will be " + weather[3]
  return first_day, second_day, third_day, fourth_day
monday, tuesday, wednesday, thursday = three_day_weather_report(weather_data)
print(monday)
print(tuesday)
print(wednesday)
print(thursday)
print("---------------------------------")

# Lambda functions
## Lambda function to add two numbers:
add = lambda a, b: a + b
print(add(3, 5))

## Lambda function to print a name:
greeting = lambda name: f"Hello, {name}!"
print(greeting("Alice"))

## Using Lambda with map()
## applies the given lambda function to each item in a list
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

## Using Lambda with filter()
## creates a new list of elements for which the given lambda function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

## Using Lambda with sorted()
## can use a lambda function as a key for custom sorting
students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)]
sorted_students = sorted(students, key=lambda x: x[2])
print(sorted_students)
print("---------------------------------")

# Map functions
## Using map() to apply a function to each item on an iterable object
def double(x):
  return x * 2
numbers = [1, 2, 3, 4, 5]
doubled_numbers = map(double, numbers)
print(list(doubled_numbers))

## Using map() with built-in functions (Converting strings to integers)
str_nums = ['1', '2', '3', '4', '5']
int_nums = list(map(int, str_nums))
print(int_nums)

## Using map() with built-in functions (Finding the length of strings)
words = ['apple', 'banana', 'cherry']
word_lengths = list(map(len, words))
print(word_lengths)

# Using map() with Lambda functions
## double each number in a list:
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Multiple iterables with map()
list1 = [1, 2, 3]
list2 = [10, 20, 30]
result = list(map(lambda x, y: x + y, list1, list2))
print(result)
