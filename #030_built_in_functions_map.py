# ========================== Built In Functions [Map] ===========================
# A- What is map()?
# ---> Map in Python is a function that works as an iterator to return a result 
#      after applying a function to every item of an iterable (tuple, lists, etc.)

# Syntax :

# map(fun, iter)

# Parameters :

# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

# NOTE : You can pass one or more iterable to the map() function.

# CODE 1:
# Python program to demonstrate working
# of map.
  
# Return double of n
def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)

result = map(addition, numbers)

print(tuple(result))

print("=" * 75)

# CODE 2
# We can also use lambda expressions with map to achieve above result.

# Double all numbers using map and lambda

numbers = [1, 2, 3, 4]

result = map(lambda x: x + x, numbers)

print(list(result))

print("=" * 75)

# CODE 3:

# Add two lists using map and lambda

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
numbers3 = [2, 4, 6]

result = map(lambda x, y, z: (x + y) * z, numbers1, numbers2, numbers3)

print(list(result))

# [10, 28, 54]

print("=" * 75)

# CODE 4:
# List of strings
l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually

test = list(map(list, l))

print(test)
