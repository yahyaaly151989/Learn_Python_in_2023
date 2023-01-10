# ========================== Importing Modules ===========================
# A- What is Python module with example?
# ---> A Python module is a file containing Python definitions and statements. 
#      A module can define functions, classes, and variables. A module can also include runnable code. 
#      Grouping related code into a module makes the code easier to understand and use.

# B- Importing Modules:

# ---> First Method:
# import random 
# a = random.random()
# b = random.randint(1, 10)
# print(a)
# print(b)
print("=" * 75)

# ---> Second Method:
# from random import randint, random
# a = random()
# b = randint(1, 10)
# print(a)
# print(b)
print("=" * 75)

# ---> Third Method:
# from random import *
# a = random()
# b = randint(1, 10)
# print(a)
# print(b)
print("=" * 75)

# ---> Fourth Method:
# import random as rn
# a = rn.random()
# b = rn.randint(1, 10)
# print(a)
# print(b)
print("=" * 75)

# C- Importing my Module:
# import sys
# sys.path.append(r"E:\YouTube\Code\Learn_Python_in_2023\yehya")
# import yehya as y
# y.sum_numbers(10, 20)
# y.multiply_numbers(10, 20)
print("=" * 75)

# D- Importing External Modules:
# ---> pip install module_name
# import numpy as np
# print(np.__version__)