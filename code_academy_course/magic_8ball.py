# Write a magic8.py Python program that can answer any “Yes” or “No” question
# with a different fortune each time it executes.
#
# The output of the program should have the following format:
# [name] asks: [question]
# Magic 8-Ball’s answer: [answer]
#
# If the name string is empty, the output should look like the following:
# Question: [question]
# Magic 8-Ball’s answer: [answer]
#
# if the question string is empty the program should output "You have to make a question first"

import random
name = "Jesse"
question = "Will I win the lottery?"
answer = ""
random_number = random.randint(1, 13)
# print(random_number)

# If statement for the answer number
if random_number == 1:
  answer += "Yes - definitely"
elif random_number == 2:
  answer += "It is decidedly so"
elif random_number == 3:
  answer += "Without a doubt"
elif random_number == 4:
  answer += "Reply hazy, try again"
elif random_number == 5:
  answer += "Ask again later"
elif random_number == 6:
  answer += "Better not tell you now"
elif random_number == 7:
  answer += "My sources say no"
elif random_number == 8:
  answer += "Outlook not so good"
elif random_number == 9:
  answer += "Very doubtful"
elif random_number == 10:
  answer += "Ask your mom"
elif random_number == 11:
  answer += "Honestly, i don't know"
else:
  answer += "Sorry, there was an error loading your answer"

# If statement to evaluate questioners name
if name == "":
  print(f"Question: {question}")
else:
  print(f"{name} asks: {question}")

# If statement to evaluate the question
if question == "":
  print("You have to make a question first")
else:
  print(f"Magic 8-Ball's answer: {answer}")

# print random name
print()
print(f"(btw the randon number generated was {random_number})")