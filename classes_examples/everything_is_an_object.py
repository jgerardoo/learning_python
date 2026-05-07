# check the attributes of the int object
print(dir(5))

# check the attributes of a class instance
class FakeDict:
  pass
fake_dict = FakeDict()              # class instantiated
fake_dict.color = "Blue"            # adding an instance variable (an attribute to the object)
print(type(fake_dict))              # check the type of the object
print(dir(fake_dict))               # check the attributes of the object. "color" should be listed
print("-------------------")

# check the attributes of a list object
fun_list = [10, "string", {'abc': True}]    # define the list
print(type(fun_list))                       # check the type of the object
print(dir(fun_list))                        # check the attributes of the object
print("-------------------")

# check the attributes of a function
def one_digit(number):
    if number > 9:
        print(F"{number} is not a one digit number")
    else:
        print(F"{number} is a one digit number")
one_digit(4)
one_digit(88)
print(type(one_digit))                      # check the type of the object
print(dir(one_digit))                       # check the attributes of the object