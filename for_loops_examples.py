ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])
print("----------------")

# For loop
for ingredient in ingredients:
    print(ingredient)
print("----------------")

six_steps = range(6)
print(list(six_steps))
for temp in range(6):
    print("Learning Loops!")
print("----------------")

for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))
print("----------------")

promise = "I will try to lear loops in Python!"
for temp in range(5):
  print(promise)
print("----------------")

# One-line 'for' loops are useful for simple programs
for ingredient in ingredients: print(ingredient)
print("----------------")

# Loop control: Break
# When the program hits a break statement it immediately terminates a loop
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
print("Checking the sale list!")
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
print("End of search!")
print("----------------")

# Loop control: Continue
# Every time our loop hits the continue control statement it simply moves to the next iteration
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for number in big_number_list:
    if number <= 0:
        continue
    print(number)
print("----------------")

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
print(numbers)
doubled = [num * 2 for num in numbers]
print(doubled)
print("----------------")

grades = [90, 88, 62, 76, 74, 89, 48, 57]
print(grades)
scaled_grades = [grade + 10 for grade in grades]
print(scaled_grades)
print("----------------")

# List Comprehensions: Conditionals
numbers = [2, -1, 79, 33, -45]
print(numbers)
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)
print("----------------")

numbers = [2, -1, 79, 33, -45]
print(numbers)
doubled = [num * 1 if num < 0 else num * 2 for num in numbers]
print(doubled)
print("----------------")

numbers = [2, -1, 79, 33, -45]
print(numbers)
no_if   = [num * 1 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 10 if num < 0 else num * 100 for num in numbers]
print(no_if)
print(if_only)
print(if_else)