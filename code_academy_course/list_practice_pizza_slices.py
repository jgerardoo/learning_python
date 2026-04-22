# Pizzas and prices in separate lists
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
print(toppings)
print(prices)
print()

# Task 1: how many slices costs $2
num_two_dollar_slices = prices.count(2)

# Task 2: length of the toppings list
num_pizzas = len(toppings)

# Task 3: print the string
print(f"We sell {num_pizzas} different kinds of pizza!")
print()

# Task 4: create a new two-dimensional list from two single lists
pizza_and_prices = list(map(list, zip(prices, toppings)))
print(pizza_and_prices)
print()

# Task 5: sort pizzas and prices
pizza_and_prices.sort()
print(pizza_and_prices)
print()

# Task 6: find the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
print()

# Task 7: find the priciest pizza
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
print()

# Task 8: remove the last item on the list
pizza_and_prices.pop()
print(pizza_and_prices)
print()

# Task 9: add a new pizza
pizza_and_prices.insert(4, [2.5, "peppers"])

# after appending peppers, re-sort to ensure order is maintained
pizza_and_prices.sort()
print(pizza_and_prices)
print()

# Task 10: store the 3 lowest cost pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
print()