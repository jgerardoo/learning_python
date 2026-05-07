# Exercise 1
## Task 1: Create a list called single_digits that consists of the numbers 0-9 (inclusive).
## Task 2: Create a for loop that goes through single_digits and prints out each one
## Task 3: Before the loop, create a list called squares. Assign it to be an empty list to begin with
## Task 4: Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares
## Task 5: After the for loop, print out squares
## Task 6: Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power
## Task 7: Print cubes
print("---- Exercise 1 ----")
single_digits = list(range(10))
print(single_digits)
print("----------")

squares = []
for num in single_digits:
  print(num)
  squares.append(num ** 2)
print(squares)
print("----------")

cubes = [num ** 3 for num in single_digits]
print(cubes)
print("------------------------------------------------------------")
print()

# You have been provided with three lists:
## hairstyles: the names of the cuts offered at Carly’s Clippers.
## prices: the price of each hairstyle in the hairstyles list.
## last_week: the number of purchases for each hairstyle type in the last week.
## Each index in hairstyles corresponds to an associated index in prices and last_week.
# Task 1: Create a variable total_price, and set it to 0
# Task 2: Loop through the prices list and add each price to the variable total_price
# Task 3: After your loop, create a variable called average_price that is the total_price divided by the number of prices
# Task 4: Print the value of average_price so the output looks like: Average Haircut Price: <average_price>
# Task 5: Use a list comprehension to make a list called new_prices, which has each element in prices minus 5
# Task 6: Print new_prices
# Task 7: Create a variable called total_revenue and set it to 0
# Task 8: Use a for loop to create a variable i that goes from 0 to len(hairstyles)
# Task 9: Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step
# Task 10: After your loop, print the value of total_revenue, so the output looks like: Total Revenue: <total_revenue>
# Task 11: Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out
# Task 12: Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30
print("---- Exercise 2 ----")
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Task 1
total_price = 0

# Task 2
for price in prices:
  total_price += price

# Task 3
average_price = total_price / len(prices)

# Task 4
print(f"Average Haircut Price: {average_price}")

# Task 5
new_prices = [num - 5 for num in prices]

# Task 6
print(f"New prices for haircuts: {new_prices}")

# Task 7
total_revenue = 0

# Task 8
for i in range(len(hairstyles)):
# Task 9
  revenue = prices[i] * last_week[i]
  total_revenue += revenue

# Task 10
print(f"Total revenue from last week: {total_revenue}")

# Task 11
average_daily_revenue = total_revenue / 7
print(f"Average daily revenue from last week: {average_daily_revenue}")

# Task 12
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]

# Task 13
print(f"These are the cuts under $30: {cuts_under_30}")
print()