# ========================== Built In Functions [Reduce] ===========================
# A- What is reduce()?
# ---> The reduce(fun,seq) function is used to apply a particular function 
#      passed in its argument to all of the list elements mentioned in the sequence passed along.
#      This function is defined in “functools” module.

# Working :  

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number 
# just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

from functools import reduce

numbers = [1, 2, 3, 4, 5] 

# def sumAll(n1, n2):
    
#     return n1 + n2

# result = reduce(sumAll, numbers)

# print(result)


result = reduce(lambda n1, n2: n1 + n2, numbers)


print(result)


letters = ["Y", "e", "h", "y", "a"] 

my_name = reduce(lambda l1, l2: l1 + l2, letters)


print(my_name)
# print( "".join(letters) )

print("=" * 75)


words = ["yehya", "alaa", "Maher", "Ebrahim", "Hiba"]

def compare(w1, w2):
    
    if len(w1) > len(w2):
        return w1
    else:
        return w2
    
result = reduce(compare, words)

print(result)