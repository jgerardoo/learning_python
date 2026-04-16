# Integers
int_1 = 15
int_2 = 5
sum_ints = int_1 + int_2
dif_ints = int_1 - int_2
product_ints = int_1 * int_2
div_ints = int_1 / int_2
print('Integer addition:', sum_ints)
print('Integer substraction:', dif_ints)
print('Integer multiplication:', product_ints)
print('Integer division:', div_ints)
print()

# Floats
float_1 = 5.5
float_2 = 4.5
sum_floats = float_1 + float_2
dif_floats = float_1 - float_2
product_floats = float_1 * float_2
div_floats = float_1 / float_2
print('Float Addition:', sum_floats)
print('Float substraction:', dif_floats)
print('Float multiplication:', product_floats)
print('Float division:', div_floats)
print()

int_3 = 7
float_3 = 2.4
sum_int_and_float = int_3 + float_3
print("Int and Float addition:", sum_int_and_float)
print(type(sum_int_and_float))
print()

# The (%) operator returns the remainder (residue) when the value on the left is divided by the value on the right
int_4 = 56
int_5 = 12
float_4 = 8.8
float_5 = 7.7
mod_ints = int_4 % int_5
mod_floats = float_4 % float_5
print("Integer modulus:", mod_ints)
print("Float modulus:", mod_floats)
print()

# The floor division (//) operator divides two numbers and returns the greatest integer less than or equal to the result
int_6 = 28
int_7 = 12
float_6 = 9.9
float_7 = 7.7
floor_div_ints = int_6 // int_7
floor_div_floats = float_6 // float_7
print("Integers floor division:", floor_div_ints)
print("Float floor division:", floor_div_floats)
print()

# Exponentiation (**) raises a number to the power of another
int_8 = 2
int_9 = 3
float_8 = 11.5
float_9 = 3.5
exp_ints = int_8 ** int_9
exp_floats = float_8 ** float_9
print("Integer exponent:", exp_ints)
print("Float exponent:", exp_floats)
print()

# integer to float()
int_10 = 6
print(f"Integer: {int_10}")
print(type(int_10))
int_to_float = float(int_10)
print("Integer as float is:", int_to_float)
print(type(int_to_float))
print()

# float to int()
float_10 = 3.1416
print(f"Float: {float_10}")
print(type(float_10))
float_to_int = int(float_10)
print(f"Float as integer is: {float_to_int}")
print(type(float_to_int))
print()

# string to either int() or float()
str_1 = "33"
print(str_1)
print(type(str_1))
str_2 = "9.8"
print(str_2)
print(type(str_2))
str_to_int = int(str_1)
print(str_to_int)
print(type(str_to_int))
str_to_float = float(str_2)
print(str_to_float)
print(type(str_to_float))
print()

# round()
num_decimals = 0.1 + 0.2
print(num_decimals)
print(type(num_decimals))
print(round(num_decimals))
print(round(num_decimals,1))
print(f"{num_decimals:.1f}") # this is another way to reduce the decimals
print()

# abs() returns the absolute value of a number
negative_num = -10
print(negative_num)
print(type(negative_num))
absolute_value = abs(negative_num)
print(absolute_value)
print(type(absolute_value))
print()

# pow() raises a number to the power of another or performs modular exponentiation
result_1 = pow(2, 3)
print(result_1)
print(type(result_1))
result_2 = pow(2, 3, 5)     # this is 2 * 2 * 2 = 8, then 8 mod 5 = 3
print(result_2)
print(type(result_2))
print()