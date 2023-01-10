# ========================== Built In Functions [Filter] ===========================
# A- What is filter()?
# ---> The filter() method filters the given sequence with the help of a function 
#      that tests each element in the sequence to be true or not.


# B- Syntax:
# ---> filter(function, sequence)

# Parameters:
# ---> function: function that tests if each element of a sequence true or not.
# ---> sequence: sequence which needs to be filtered, 
#      it can be sets, lists, tuples, or containers of any iterators.

# Returns:
# ---> returns an iterator that is already filtered.


# Code 1 :
# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
 
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r', 'o']

# using filter function
filtered = list(filter(fun, sequence))

print('The filtered letters are:')

print(filtered)

print("=" * 75)

# Code 2:
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list

result = filter(lambda x: x % 2 != 0, seq)

print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)

print(list(result))


def my_func(number):
    
    return number % 2 == 0
    
result = filter(my_func, seq)

print(list(result))
