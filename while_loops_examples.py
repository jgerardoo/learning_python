count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
print("----------")

countdown = 5
while countdown >= 0:
  print(str(countdown))
  countdown -= 1
print("We have liftoff!")
print("----------")

# while loops from a list
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0
while index < length:
    print(ingredients[index])
    index += 1
print("----------")

python_topics = ["variables", "control flow", "loops", "modules", "classes"]
length_2 = len(python_topics)
index_2 = 0
while index_2 < length_2:
    print("I am learning about " + python_topics[index_2])
    index_2 += 1
print("----------")

# One-line 'while' loops are useful for simple programs
count_2 = 0
while count_2 <= 3: print(count_2); count_2 += 1
print("----------")