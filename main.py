user_name = "Jesse"         # Python knows this is a string
user_age = 35               # Python knows this is a string
print(user_name)
print(user_age)
print()

print("This is my Python practice file")

print("My favorite colors are", "blue", "brown")
print()

# Declaring different data type variables
integer_var = 10
float_var = 9.8
string_var = "hello"
boolean_var = True
set_var = {1.5, "apple", 5}
dict_var = {"name": "Rosy", "age": 34}
tuple_var = ("banana", 1.2, 9, False)
range_var = range(9)
list_var = [22, "taco", 3.14, True]
none_var = None

# Get the variables value
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("Dict:", dict_var)
print("Tuple:", tuple_var)
print("Range:", range_var)
print("List:", list_var)
print("None:", none_var)
print()

# Get the data type of the variables
print(type(integer_var))
print(type(boolean_var))
print()

# Check if a variable matches a specific data type
print(isinstance('Pizza', str))
print(isinstance(integer_var, int))
print(isinstance(float_var, int))
print()

# Declaring and printing a multi-line string
multi_line_string = """Multi
line
string"""
print(multi_line_string)
print()

# Check if a string contains one or more characters
print("Jesse" in user_name)
print("s" in user_name)
print("r" in user_name)
print()

# Get the length of a string
print(len(user_name))

# Get individual characters of a string
print(user_name[0])
print(user_name[1])
print(user_name[2])
print(user_name[-2])
print(user_name[-1])

# Print the string in uppercase
print(user_name.upper())

# Print the string in lowercase
print(user_name.lower())
print()

# String concatenation
str_1 = "Hello"
str_2 = "World"
str_plus_str = str_1 + ' ' + str_2
print(str_plus_str)
print()

# String and int concatenation
name_and_age = user_name + str(user_age)
print(name_and_age)
print()

# String interpolation
print(f"My name is {user_name} and I am {user_age} years old.")
num_1 = 10
num_2 = 5
print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")