print("---------- PRACTICE 1 ----------")
print("--------- Lots of Math ---------")

def lots_of_math(a, b, c, d):
  a_plus_b = a + b
  print(a_plus_b)
  c_minus_d = c - d
  print(c_minus_d)
  third = a_plus_b * c_minus_d
  print(third)
  fin = third % a
  return fin

print(lots_of_math(1, 2, 3, 4))     # should print 3, -1, -3, 0
print(lots_of_math(1, 1, 1, 1))     # should print 2, 0, 0, 0
print()

print("---------- PRACTICE 2 ----------")
print("--------- TripPlanner ----------")
# Welcome message
def trip_planner_welcome(name):
  print(f"Welcome to TripPlanner v1.0 {name}")

trip_planner_welcome("Jesse")
print()

# Calculate rounded time
def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time)
  return rounded_time

estimate = estimated_time_rounded(5.6)

# Generate messages for a user’s planned trip.
def destination_setup(origin, destination, estimated_time, mode_of_transport = "Car"):
  print(f"Your trip starts off in {origin}")
  print(f"And you are traveling to {destination}")
  print(f"You will be traveling by {mode_of_transport}")
  print(f"It will take approximately {estimated_time} hours")

destination_setup("Mexico", "USA", estimate)
print()

print("---------- PRACTICE 3 ----------")
print("------- Lambda functions -------")
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use a lambda function to filter out odd numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# Use a lambda function to filter out even numbers
odds = list(filter(lambda x: x % 2 != 0, numbers))
# Use a lambda function to square each number
squares = list(map(lambda x: x ** 2, numbers))
# Use a lambda function to filter numbers divided by 3
threes = list(filter(lambda x: x % 3 == 0, numbers))
# Print the results
print("Original numbers:", numbers)
print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Squared numbers:", squares)
print("Numbers divided by 3:", threes)
print()

print("---------- PRACTICE 4 ----------")
print("-------- Map functions ---------")
# Sample lists of names
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
last_names = ['Smith', 'Jay', 'Stone', 'Hill', 'Doe']
# Use map with a lambda function to get the length of each name
name_lengths = list(map(lambda x: len(x), names))
# Use map with a defined function to capitalize each name
def capitalize_name(name):
    return name.upper()
capitalized_names = list(map(capitalize_name, names))
# Use map to combine names + last names
full_names = list(map(lambda x, y: x + ' ' + y, names, last_names))
# Print the results
print("First names:", names)
print("Last names:", last_names)
print("Name lengths:", name_lengths)
print("Capitalized names:", capitalized_names)
print("List of full names:", full_names)
print()

print("---------- PRACTICE 5 ----------")
print("-------- Physics Class ---------")
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# Create a function that converts Fahrenheit to Celsius:
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp
f100_in_celsius = f_to_c(100)

# Create a function that converts Celsius to Fahrenheit:
def c_to_f(c_temp):
  f_temp = c_temp * (9 / 5) + 32
  return f_temp
c0_in_fahrenheit = c_to_f(0)

# Create a function to calculate the force
# force = mass * acceleration
def get_force(train_mass, train_acceleration):
  force = train_mass * train_acceleration
  return force
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")

# Create a function to calculate the energy
# energy = mass * c
def get_energy(mass, c = 3*10**8):
  energy = mass * c
  return energy
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")

# Create a function to calculate the work
# work = force * distance
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  work = force * distance
  return work
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")