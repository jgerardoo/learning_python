user_name = "Jesse"         # Python knows this is a string
user_age = 35               # Python knows this is a string
print(user_name)
print(user_age)
print()

print("This is my Python practice file")

print("My favorite colors are", "blue", "brown")
print()

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

print(type(integer_var))
print(type(boolean_var))
print()

print(isinstance('Pizza', str))
print(isinstance(integer_var, int))
print(isinstance(float_var, int))
print()

multi_line_string = """Multi
line
string"""
print(multi_line_string)
print()

print("Jesse" in user_name)
print("s" in user_name)
print("r" in user_name)
print()

print(len(user_name))
print(user_name[0])
print(user_name[1])
print(user_name[2])
print(user_name[-2])
print(user_name[-1])
print(user_name.upper())
print(user_name.lower())
print()

str_1 = "Hello"
str_2 = "World"
str_plus_str = str_1 + ' ' + str_2
print(str_plus_str)
print()

name_and_age = user_name + str(user_age)
print(name_and_age)
print()

print(f"My name is {user_name} and I am {user_age} years old.")
num_1 = 10
num_2 = 5
print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")