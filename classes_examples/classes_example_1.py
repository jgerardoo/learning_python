# Create a class
class Turbo:
    pass                                # the class was intentionally left blank with this keyword

# Instantiate the class
turbo_1 = Turbo()                       # instantiation takes a class and turns it into an object

print(type(turbo_1))                    # this object is of type "__main__.Turbo"
print("-------------------")

# Class variables
## the same data to be available to every instance of a class
class Musician:
    title = "Rockstar"                  # this is the class variable

drummer = Musician()                    # instantiate the class
print(drummer.title)                    # print the drummer's title which is a class variable that we defined as the string “Rockstar”
guitarist = Musician()
print(guitarist.title)
print("-------------------")

# Methods
## functions that are defined as part of a class
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):         # method created
        print(f"Dogs experience {self.dog_time_dilation} years for every 1 human year.")
        print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pitbull = Dog()                         # instantiate the class
pitbull.time_explanation()              # called the .time_explanation() method on our new object
print("-------------------")

# Methods with Arguments
class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):              # method created with one parameter
        return miles * self.kms_in_a_mile

converter = DistanceConverter()                 # instantiate the class
kms_in_2_miles = converter.how_many_kms(2)      # called the method with its argument (we only pass "miles", because "self" is implicitly passed)
print(kms_in_2_miles)
print("-------------------")

class Circle:
    pi = 3.14
    def area(self, radius):
        area = Circle.pi * radius ** 2
        return area

circle = Circle()                               # instantiate the class
pizza_area = circle.area(6)                     # called the method with its argument
teaching_table_area = circle.area(18)
round_room_area = circle.area(10000)
print(pizza_area)                               # print the results
print(teaching_table_area)
print(round_room_area)
print("-------------------")

# Constructors
## __init__ method
class Greeting:
    def __init__(self):
        print("HELLO?!")

greet1 = Greeting()                              # the __init__ method is executed as soon as the class is instantiated
print("-------------------")

## __init__ method with parameters and conditionals
class Shouter:
    def __init__(self, phrase):
        if type(phrase) == str:                 # validation to ensure the argument is a string
            print(phrase.upper())               # if the argument is string, print it out using capital letters
shout1 = Shouter("hello")                       # prints "HELLO"
shout2 = Shouter(25)                            # prints nothing since the argument is not a string
shout3 = Shouter("hi")                          # prints "HI"
print("-------------------")

# Instance variables
## We can instantiate two different objects from a class and assign instance variables to these objects
class FakeDict:
    pass

fake_dict1 = FakeDict()                                 # instantiate the class
fake_dict2 = FakeDict()
fake_dict1.fake_key = "This is a fake key!"             # instance variable created and assigned
fake_dict2.fake_key = "This is another fake key!"
print(fake_dict1.fake_key)                              # print the instance variable of the objects
print(fake_dict2.fake_key)
print("-------------------")

# Attribute functions
fake_dict3 = FakeDict()                                 # instantiate the class. This object has no instance variable (no attributes)
print(hasattr(fake_dict3, "fake_key"))                  # returns "False" since "fake_dict3" does not have the "fake_key" attribute
print(getattr(fake_dict3, "fake_key", "No attributes")) # returns "No attributes", the default value
print("-------------------")

elements_list = [{'s': False}, "pencil", 18, ["a", "c", "s", "d", "s"]]
for element in elements_list:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute")
print("-------------------")

# Self
class SearchEngineEntry:
  def __init__(self, url):
    self.url = url                  # this is an instance variable named "self.url" and it gets the value of the parameter passed into the constructor

codecademy = SearchEngineEntry("www.codecademy.com")        # crete a class instance and pass the URL as an argument to the constructor
wikipedia = SearchEngineEntry("www.wikipedia.org")

print(codecademy.url)               # print to verify that the URL has been assigned to the url instance variable of the class instance
print(wikipedia.url)
print("-------------------")

# "self" accessing both the class variable and the instance variable
class SecureSearchEngineEntry:
  secure_prefix = "https://"
  def __init__(self, url):
    self.url = url                  # this is an instance variable named "self.url" and it gets the value of the parameter passed into the constructor

# method on the SecureSearchEngineEntry class that returns the secure link to an entry
  def secure(self):
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)    # access both the class variable and the instance variable to return a secure URL

codecademy = SecureSearchEngineEntry("www.codecademy.com")      # create a class instance and pass the URL as an argument to the constructor
wikipedia = SecureSearchEngineEntry("www.wikipedia.org")

print(codecademy.secure())          # print to verify that the URL has been assigned to the url instance variable of the class instance
print(wikipedia.secure())
print("-------------------")

# String representation
class Employee:
    def __init__(self, name):
        self.name = name
person1 = Employee("Mike")
print(person1)                      # this default string representation gives us some information about the object
print("-------------------")

# String representation with __repr__()
class Employees:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
person2 = Employees("Juan")
print(person2)                      # the __repr__() method returns the .name attribute of the object