# Practice example from practicepython.org
# Exercise 1 - Character Input (input strings types int)

# Create a program that asks the user to enter their name and their age. Print out a message addressed to them
# that tells them the year that they will turn 100 years old. Note: for this exercise. The expectation is that you explicitly
# write out the year (and therefore be out of date the next year).

current_year = 2026
user_name = input('Enter your name: ')
user_age = input('Enter your age: ')
when_100 = 100 - int(user_age)
print(f"Welcome {user_name}. In {when_100} years you will be 100 years old.")