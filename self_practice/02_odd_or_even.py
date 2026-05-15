# Practice example from practicepython.org
# Exercise 2 - Odd Or Even (input if types int equality comparison numbers mod)

# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.

# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

number = input("Give me a number: ")
number = int(number)

if number % 4 == 0:
    print(f"{number} is a multiple of 4")
elif number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")
print("----------------------------------------")

print("Now, im going to ask you for two numbers and I am going to check if those numbers divide evenly")
num = input("Give me the first number: ")
num = int(num)
check = input("Give me the second number: ")
check = int(check)
division = num / check
if division % 2 == 0:
    print(f"{num} and {check} divide evenly")
else:
    print(f"{num} and {check} don't divide evenly")