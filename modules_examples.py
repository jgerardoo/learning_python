from datetime import datetime
import random
from decimal import Decimal
from modules_examples_two import always_ten
from modules_examples_two import imported_string
from modules_examples_two import imported_int
from modules_examples_two import imported_list

# datetime
current_time = datetime.now()
print(current_time)
birthday = datetime(1990, 10, 11, 23,12)
print(birthday)
print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.weekday())
print()

# datetime.now
print(datetime.now())
print()

# datetime operations
print(datetime(2026, 4, 29) - datetime(1990,10,11))
print()
time_this_year = datetime.now() - datetime(2026, 1, 1)
print(time_this_year)
print()

# strptime = string + parse + time
# create a datetime from a string
# format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
parsed_date = datetime.strptime('Jan 15, 2026', '%b %d, %Y')
print(parsed_date)
parsed_date_2 = datetime.strptime('Oct 11, 1990', '%b %d, %Y')
print(parsed_date_2)
print()

# strftime = string + format + time
# create a string from a datetime
# format: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
date_string = datetime.strftime(datetime.now(), '%b %d, %Y')
print(date_string)
date_string_2 = datetime.strftime(datetime(1190, 10,11), '%b %d, %Y')
print(date_string_2)
print()

# random.randint
## Create random_list below:
random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)
## Create randomer_number below:
randomer_number = random.choice(random_list)
## Print randomer_number below:
print(randomer_number)
print()

# random.sample
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums)
sample_nums = random.sample(nums, 5)
print(sample_nums)
print()

# Generate a 2D graphic using pyplot
# import codecademylib3_seaborn
# from matplotlib import pyplot as plt
# import random
#
# numbers_a = range(1, 13)
# numbers_b = random.sample(range(1000), 12)
# print(list(numbers_a))
# print(numbers_b)
#
# plt.plot(numbers_a, numbers_b)
# plt.show()

# Decimal
multiple_decimal_points = 0.2 + 0.69
print(multiple_decimal_points)
two_decimal_points = Decimal('0.2') + Decimal('0.69')
print(two_decimal_points)

multiple_decimal_points_2 = 0.53 * 0.65
print(multiple_decimal_points_2)
four_decimal_points = Decimal('0.53') * Decimal('0.65')
print(four_decimal_points)
print()

# Use a function from another file
## this function was not defined in this file, it was defined in modules_examples_two
always_ten()
print(imported_string)
print(imported_int)
print(imported_list)