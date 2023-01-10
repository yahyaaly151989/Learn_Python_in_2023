# ============================ String and (Indexing, Slicing) ============================
# 1- What is a String?
# ---> In computer programming, a string is a sequence of characters. 
#      For example, "hello" is a string containing a sequence of 
#      characters 'h', 'e', 'l', 'l', and 'o'.

# ---> We use single quotes or double quotes to represent a string in Python.
# ---> We use len(iterable) to know its length.
my_name = "Ahmad"
my_name = 'Ahmad'
print(len ( my_name ) )
print("=" * 75)

# 2- What is String Indexing?
# ---> Indexing means referring to an element of an iterable by its position within the iterable. 
# ---> We use string[element position] to access to an element.
# ---> Python uses Zero based indexing => index starts from zero.
my_string = "I love Python"   
print( my_string[0] ) # I
print( my_string[1] ) # " "
print( my_string[2] ) # l
print( my_string[-1] ) # n
print( my_string[-2] ) # 0
print(" " * 75)

# 3- What is String Slicing?
# ---> Slicing means getting a subset of elements from an iterable based on their indices.
# ---> we use string[start position:end position:steps].
my_string = "I love Python"
print( my_string[0:6:1] ) # I love
print(" " * 75)

# ---> start position => is the index of the first element, if not written this means index = 0
my_string = "I love Python"
print( my_string[7:13] ) # Python
print( my_string[7:13:1] ) # Python

print( my_string[:13] ) # I love Python
print( my_string[:13:1] ) # I love Python
print(" " * 75)

# ---> end position => is the index of the last element, if not written this means index = len(string)
#      end not included.
my_string = "I love Python"
print(len(my_string)) # 13
print( my_string[7:13] ) # Python
print( my_string[7:] ) # Python
print(" " * 75)

# ---> steps => steps, if not written this means steps = 1
my_string = "I love Python"
print( my_string[7:13:1] ) # Python
print( my_string[7:13:2] ) # Pto
print(" " * 75)

# ---> if no start, no end, no steps => full data
print(my_string[::]) # I love Python

# ---> String is immutable data type. => We cannot add, edit, or delete its elements.
my_name = "Alaa"
my_name[0] = "Y" # TypeError: 'str' object does not support item assignment

print(my_string)

# ==================================== End ====================================
