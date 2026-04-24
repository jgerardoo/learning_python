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
#
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
for number in big_number_list:
    if number <= 0:
        continue
    print(number)