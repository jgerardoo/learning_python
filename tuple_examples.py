tuple_1 = ('abc', 123, 'def', 456)
tuple_2 = ('xyz',)
print(tuple_1)
print(tuple_2)
print()

# Tuple indexing
tuple_3 = ('abc', 123, 'def', 456, 789, 'ghi')
print(tuple_3)
print(tuple_3[0])

# Tuple slicing
print(tuple_3[3:5])

# len
print(len(tuple_3))
print()

# max() / min()
tuple_4 = (65, 2, 88, 101, 25, 102)
print(tuple_4)
print(max(tuple_4))
print(min(tuple_4))
print()

tuple_5 = ('orange', 'blue', 'red', 'green', 'white', 'brown')
print(tuple_5)
print(max(tuple_5))
print(min(tuple_5))
print()

# .index() - takes in a value as the argument to find its index in the tuple
tuple_6 = ('abc', 234, 567, 'def')
print(tuple_6)
print(tuple_6.index('abc'))
print(tuple_6.index(567))
print()

# .count() - takes in a value as the argument to find the number of occurrences in the tuple
tuple_7 = ('abc', 'abc', 2, 3, 4)
print(tuple_7)
print(tuple_7.count('abc'))
print(tuple_7.count(3))
print()