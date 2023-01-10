# ================================= Learn Python in 2023 =====================
# ================================= Level #I =================================
# 01- Introcuction:
# --------- 01- Introcuction: ----------
# A- What is Python?
# ---> High-level programming language.
print("Hello Python!")
print("=" * 75)

# ---> Interpreted programming language
print("Line 1")
print("Line 2")
# print(10 / 0) # ZeroDivisionError
print("Line 3")
print("=" * 75)

# ---> Interactive
print("Hello Python!")
print("=" * 75)

# ---> Object-Oriented (OOP)
# ---> Free and open source

# B- Why to Learn Python?
# ---> Easy to learn
# ---> Easy to install
# ---> Error handling and debugging
# a, b, c = 1, 2, 3, 4 # => too many values to unpack (expected 3)
# a, b, c, d = 1, 2, 3 # not enough values to unpack (expected 4, got 3)
# ---> Cross platform (Windows, MacOS, Linux)
# ---> Supports modules and packages
# ---> It has a large community
# ---> Expressive
is_subscribed = False
print("Welcome to my channel. Enjoy our lessons." if is_subscribed else "Please subscribe to my channel.")
# ---> It is required for large corporations as well as master's and PhD programs.
# ---> ...
print("=" * 75)

# C- What Can I Do with Python?
# ---> Web development
# ---> Machine learning and artificial intelligence
# ---> Data science and data visualization
# ---> Desktop GUI
# ---> Web scraping applications
# ---> ...

# D- What I need to Start Learning?
# ---> Download Python 
# ---> Text Editor or IDE (Visual Studio Code or PyCharm)
# ---> Python Extension

print("###########################################################################")

# ---------- 02- Syntax and Comments: ----------
# A- What is Syntax?
# ---> The syntax of the Python programming language is the set of rules that 
#      defines how a Python program will be written and interpreted 
#      (by both the runtime system and by human readers).

# ---> print()
print("Hello Python!")
# console.log("Hello Python!") # JavaScript
print("=" * 75)

# ---> Python uses something called indentation.
if 10 == 20: 
    print("Hello Python!")
else:
    print("Hello Programming!")
print("=" * 75)

# For example, in other languages:
# if (10 == 10) {
#     console.log("Hello Python!");
# }

# ---> Python does not have a semicolon (;).
print("Hello Python,");
print("How are you?");
print("=" * 75)

# ---> But we use it if we write two statements in the same line.
print("Hello Python."); print("How are you?")
print("=" * 75)

# B- What is Comment?
# ---> Comments in Python are the lines in the code that are ignored by 
#      the interpreter during the execution of the program.
#      We use hashtag symbol ( # ) to write comments.

# print("This will NOT be printed, because it is a comment")
print("=" * 75)

# ---> Single line comments
# This is a single line comment
print("Hello Python!") # This is a single line comment
print("=" * 75)

# ---> Multiline Comments
# This will print 15,
# because it adds two numbers which are 10 and 5,
# for that the result will be 15.
print(10 + 5)
print("=" * 75)

# ---> Docstring comment
"""
We will learn this section in the next lessons.
"""
print("###########################################################################")

# ----------- 03- Data Types Overview: ---------------
# A- What is Data Type?
# ---> A data type, in programming, is a classification that specifies which type of 
#      value a variable has and what type of mathematical, 
#      relational or logical operations can be 
#      applied to it without causing an error.

# ---> Data is stored in computer memory.
# ---> We use variables to refer to this data.
name = "Yehya"
print(name)
print("=" * 75)

# B- What are Data Types in Python?
# ---> We use type(data) to know the type of data.

# ---> int => Integer
print( type(10) )
print( type(-90) )
print("=" * 75)

# ---> float => Float
print( type( 10.0 ) )
print( type( -8.79 ) )
print("=" * 75)

# ---> complex => Complex
print( type( 2 - 2j ) )
print( type( 12 + 90j ) )
print("=" * 75)

# ---> str => String
print( type( "Yehya" ) )
print( type( 'Ahmad' ) )
print("=" * 75)

# ---> list => List
print( type(  [1, 2, 3]  )  )
print("=" * 75)

# ---> tuple => Tuple
print( type(  (1, 2, 3)  )  )
print("=" * 75)

# ---> set => Set
print( type(  {1, 2, 3}  )  )
print("=" * 75)

# ---> dict => Dictionary
print( type(  {"one": 1, "two": 2}  )  )
print("=" * 75)

# ---> bool => Boolean
print( type( True ) )
print( type( False ) )
print( type( 10 == 10 ) )
print("=" * 75)

# ---> None => NoneType
print( type( None ) )
print("=" * 75)
print("###########################################################################")

# ---------- 04- Variables: ----------
# A- What is a Variable?
# ---> In programming, a variable is a value that can change, depending on conditions or
#      on information passed to the program.

language = "Js"

print("Hello " + language)
print("I love " + language)
print(language + " is very easy")
print("=" * 75)

# ---> A program consists of instructions that tell the computer what to do and 
#      data that the program uses when it is running.
# ---> Data is stored in computer memory.
# ---> We use variables to refer to this data.

# B- Syntax and Naming Rules.
# ---> variable_name = variable_value
name = "Yehya"
print(name)
print("=" * 75)

# ---> We can start with letters [a-z A-Z]
name = "Yehya"
Country = "Syria"
print("=" * 75)

# ---> We cannot start with numbers and special characters not allowed.
# 100name = "Yehya" # error
# print(100name)

the100name = "Yehya"
print(the100name)

name100 = "Yehya"
print(name100)
print("=" * 75)

# @name = "Yehya" # error
# the/name = "Yehya" # error
# my-name = "Yehya" # error

# ---> We cannot use space, we use underscore
# my name = "Yehya" # error
my_name = "Yehya"
print(my_name)
print("=" * 75)

# ---> Case sensitive => name /= Name
age = 33
Age = 22
print(age) # 33
print(Age) # 22
print("=" * 75)

# ---> We should declare a variable and then use it.
# print(country) # error
country = "Syria"
print("=" * 75)

# ---> Reserved words are not permitted.  help(“keywords”)
# class = "Lang"
help("keywords")
print("=" * 75)

# ---> Single Word
name = "Yehya"
print(name)
print("=" * 75)

# ---> Two or more words
myName = "Yehya"
print(myName)
print("=" * 75)

my_name = "Yehya"
print(my_name)
print("=" * 75)


# ---> Python is dynamically typed language. 
name = "Ahmad"
print(name) 

name = 10
print(name)
print("###########################################################################")

# ---------- 05- String and Methods: ----------
# A- What is a String?
# ---> In computer programming, a string is a
#      For example, "hello" is a string containing a sequence of  sequence of characters. 
#      characters 'h', 'e', 'l', 'l', and 'o'.

# ---> We use single quotes or double quotes to represent a string in Python.
# ---> We use len(iterable) to know its length.
my_name = "Ahmad"
my_name = 'Ahmad'
print(len ( my_name ) )
print("=" * 75)

# B- What is String Indexing?
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

# C- What is String Slicing?
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
# my_name[0] = "Y" # TypeError: 'str' object does not support item assignment

# print(my_string)

# D- String Methods:
# ---> strip(characters to remove) => Returns a trimmed version of the string
# ---> rstrip(characters to remove) => Returns a right trim version of the string
# ---> lstrip(characters to remove) => Returns a left trim version of the string
# ---> if characters to remove not written => default value is spaces
a = "    I love Python    "
print( a.strip() ) 
print("=" * 75)

a = "########I love Python##########"
print( a.strip() )
print( a.strip("#") )
print( a.rstrip("#") )
print( a.lstrip("#") )
print("=" * 75)


# ---> capitalize() => Converts the first character to upper case
a = "yehya ali"
print( a.capitalize() )
print("=" * 75)

# ---> title() => Converts the first character of each word to upper case
a = "yehya ali alaa ahmad"
print( a.title() )
print("=" * 75)

# ---> upper() => Converts a string into upper case
a = "I love Python"
print( a.upper() )
print("=" * 75)

# ---> lower() => Converts a string into lower case
a = "I love Python"
print( a.lower() )
print("=" * 75)

# ---> swapcase() => Swaps cases, lower case becomes upper case and vice versa
a = "I LOve PythOn."
print( a.swapcase() )
print("=" * 75)

# ---> zfill() => Fills the string with a specified number of 0 values at the beginning
a, b, c = "1", "11", "111"
print( a.zfill(3) )
print( b.zfill(3) )
print( c.zfill(3) )
print("=" * 75)

# ---> split(separator) => Splits the string at the specified separator, and returns a list
# ---> separator by default => space
a = "I love Python"
print( a.split() )
print( a.split(" ") )
print( a.split("P") )
print("=" * 75)

a = "I love Python and programming"
print( a.split(" ", 2) )
print( a.rsplit(" ", 2) )
print("=" * 75)

# ---> splitlines() => Splits the string at line breaks and returns a list
a = "I\nlove\nPython"
print(a)
print( a.splitlines() )
print("=" * 75)

# ---> join() => Converts the elements of an iterable into a string
a = "Yehya"
b = ["Yehya", "Ahmad", "Alaa"]
print( ", ".join(a) )
print( " | ".join(b) )
print("=" * 75)

# ---> count(element) => Returns the number of times a specified value occurs in a string
a = "I love Python because Python is easy."
print( a.count("Python") )
print( a.count("e") )
print("=" * 75)

# ---> find() => Searches the string for a specified value and returns the position of where it was found
# ---> index() => Searches the string for a specified value and returns the position of where it was found
a = "I love Python, I love it because Python is easy."
print( a.index("I", 4, 20) )
print( a.index("Python") )
# print( a.index("Z") ) # error

print( a.find("I") )
print( a.find("Python") )
print( a.find("Z") ) # -1
print("=" * 75)

# ---> startswith() => Returns True if the string starts with the specified value
a = "I love Python"
print( a.startswith("I") )
print( a.startswith("Z") )
print( a.startswith("P", 7, 13) )
print("=" * 75)

# ---> endswith() => Returns True if the string ends with the specified value
a = "I love Python"
print( a.endswith("n") )
print( a.endswith("e") )
print( a.endswith("e", 2, 6) )
print("=" * 75)

# ---> istitle() => Returns True if the string follows the rules of a titl
a = "I Love Python"
print( a.istitle() )

# ---> isupper() => Returns True if all characters in the string are upper case
a = "I Love Python"
print( a.isupper() )
print("=" * 75)

# ---> islower() => Returns True if all characters in the string are lower case
a = "I Love Python"
print( a.islower() )
print("=" * 75)

# ---> isnumeric() => Returns True if all characters in the string are numeric
a = "1234"
b = "123yehya45"
print( a.isnumeric() )
print( b.isnumeric() )
print("=" * 75)

# ---> isalpha() => Returns True if all characters in the string are in the alphabet
a = "1234"
b = "123yehya45"
c = "yehya"
print( a.isalpha() )
print( b.isalpha() )
print( c.isalpha() )
print("=" * 75)

# ---> isalnum() => Returns True if all characters in the string are alphanumeric
a = "1234"
b = "123yehya45"
c = "yehya"
d = "yehya@"
print( a.isalnum() )
print( b.isalnum() )
print( c.isalnum() )
print( d.isalnum() )
print("=" * 75)

# ---> isidentifier() => Returns True if the string is an identifier
a = "100name" # False
b = "my_name" # True
print( a.isidentifier() )
print( b.isidentifier() )
print("=" * 75)

# E- What is Concatenation?
# ---> Concatenating means obtaining a new string that contains both of the original strings. 
# ---> We use + operator to concatenate two or more strings.

# ---> Concatenation:
a = "Hello"
b = "Python"
s = " "
c = a + s + b
print(c)
print("=" * 75)

name = "Yehya"
age = 33
print("My name is " + name)
# print("My age is " + age) # TypeError: can only concatenate str (not "int") to str
print("My age is " + str(age))
print("=" * 75)

# F- What is String Formatting?
# ---> String formatting is also known as String interpolation. 
#     It is the process of inserting a custom string or variable in predefined tex.

name = "Yehya"
age = 20
ranking = 9.7

print("My name is %s and my age is %d and my ranking is %f" %(name, age, ranking))
print("My name is %s and my age is %d and my ranking is %.2f" % (name, age, ranking))
# print("=" * 75)

print("My name is {:s} and my age is {:d} and my ranking is {:f}" .format(name, age, ranking))
print("My name is {:s} and my age is {:d} and my ranking is {:.2f}" .format(name, age, ranking))
print("=" * 75)

print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:f}")
print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:.2f}")
print("=" * 75)

# G- Escape Sequences Characters:
# ---> To insert characters that are illegal in a string, use an escape character. 
#      An escape character is a backslash \ followed by the character you want to insert.

# ---> \b
a = "Hello\bPython"
print(a)
print("=" * 75)

# ---> \
a = "Hello \"Python\""
b = 'Hello \'Python\''
c = "Hello \\ Python"
d = "Hello \
Python"
print(a)
print(b)
print(c)
print(d)
print("=" * 75)

# ---> \n
print( "Hello\nPython" )
print("=" * 75)

# ---> \t
a = "Hello\tPython"
print( a )

b = a.expandtabs(20)
print(b)
print("###########################################################################")

# 06- ---------- Numbers and Methods: ----------
# A- What is Numbers in Python?
# ---> Python has three built-in numeric data types: 
# -----> Integers
# -----> Floating-Point Numbers
# -----> Complex Numbers

# ---> int => Integer
print( type( 10 ) )
print( type( -10 ) )
print("=" * 75)

# ---> float => Floating-Point Numbers
print( type( 10.0 ) )
print( type( -10.89 ) )
print("=" * 75)

# ---> complex => Complex Numbers
print( type( 10 + 2j ) )
print( type( -4.8 + 4j ) )
print( type( 4.1 - 8.9j ) )
print("=" * 75)

# ---> We can convert int to float and complex using float() and complex() methods.
i = 15
f = float( i )
print( f )
print( type( f ) )

c = complex( i )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We can convert float to int and complex using int() and complex() methods.
f = 15.9
i = int( f )
print( i )
print( type( i ) )

c = complex( f )
print( c )
print( type( c ) )
print("=" * 75)

# ---> We cannot convert complex to int or float
c = 10 + 2j

real_part = c.real
print( real_part )
print( type( real_part ) )

imaginary_part = c.imag
print( imaginary_part )
print( type( imaginary_part ) )
print("=" * 75)

# B- Arithmetic Operators:
print(10 + 2)
print(10 - 8)
print(20 * 3)
print(100 / 4)
print(103 // 4) 
print(104 // 4)
print(2 ** 4) # 2 * 2 * 2 * 2 
print(5 ** 3) # 5 * 5 * 5
print(10 % 3) # 1
print(26 % 3) # 2
print(4 % 2) # 0
print("=" * 75)

# C- Numbers Methods:
# ---> Python has a few built-in functions that you can use to work with numbers.

# round() => Rounding numbers to some number of decimal places
a = 9.75
b = round(a)
print(b)

a = 7.7
b = round(a)
print(b)

c = 9.226
d = round(c, 2)
d = round(c, 1)
print(d)

# abs() => Getting the absolute value of a number
a = -10
b = abs(a)
print(b)
print("=" * 75)

# pow() => Raising a number to some power
a = pow(2, 3)
print(a)
a = pow(4, 4)
print(a)

a = pow(3, 3, 2)
print(a)
print("=" * 75)

# min() => The min number in a collection of numbers
# max() => The max number in a collection of numbers
print(min(1, 2, -10, 4, -100, 100))
print(max(1, 2, -10, 4, -100, 100))
print("=" * 75)

# sum() => Sum of numbers
print(sum([1, 2, 3]))
print(sum([1, 2, 3], 10))
print(sum((2, 5, 6), 8))
print("=" * 75)

# range() => Range of numbers
print(range(0, 10))
print("=" * 75)
print("###########################################################################")

# ---------- 07- List and Methods: ----------
# A- What are Lists?
# ---> Lists are used to store multiple items in a single variable.
names = ["Ahmad", "Alaa", "Ali", "Mona"]
print(names)
print("=" * 75)

# ---> List items are enclosed with square brackets [].
names = ["Ahmad", "Alaa", "Ali", "Mona"]
print(names)
print(type(names))
print("=" * 75)

# ---> Lists are ordered, we use indexing and slicing to access their items.
langs = ["Python", "Java", "JavaScript", "C++"]
fl = langs[0]
ll = langs[-1]
ftl = langs[0:2]
print("=" * 75)

names = [ "Ahmad", [ "Ali", [ "Yehya", "Alam" ] ] ]

m = names[1][1][1][-1].upper()
print(m)
print("=" * 75)

# ---> Lists are mutable, we can add, edit and delete.
names = ["Ahmad", "Alaa", "Ali", "Mohamed"]
names[0] = "Ah"
print(names)


names[0:2] = ["Ali"]
print(names)

names[-1] = ["A", "B", "C", "D", "E"]
print(names)
print("=" * 75)

# ---> The items are not unique.
names = ["Ahmad", "Alaa", "Ahmad", "Alaa", "Alaa", "Mohamed"]
print(names)
print("=" * 75)

# ---> Lists can have different data types.
my_list = ["A", 1, 10.9, 1+8j, True, [1, 2, 3], (1, 2, 3, 4), {1, 2}, {"a":1, "b":1}]
print(my_list)
print("=" * 75)

# B- List Methods:
# ---> append() => append() => Adds an element at the end of the list.
a = ["Ahmad", "Ali", "Alaa"]
a.append("Yehya")
a.append([1, 2, 3])
print(a)
print("=" * 75)

# ---> extend() => Add the elements of a list (or any iterable), to the end of the current list.
a = [1, 2, 3]
# a.append([4, 5, 6])
a.extend([4, 5, 6])
# a.extend(True) # error
# a.extend(1) # error
a.extend("Yehya") # error
print(a)
print("=" * 75)

# ---> insert() => Adds an element at the specified position.
a = ["A", "B", "C", "D", "E", "F", "D"]

a.insert(0, "Y")
a.insert(3, "DDD")
a.insert(-1, "ZZ")
print(a)
print("=" * 75)

# ---> clear() => Removes all the elements from the list.
a = ["A", "B", "C"]
a.clear()
print(a)
print(len(a))
print("=" * 75)

# ---> copy() => Returns a copy of the list
a = [1, 2, 3]

b = a.copy()

print(b)

a.append(4)
print(a)
print(b)
print("=" * 75)

# ---> count() => Returns the number of elements with the specified value.
names = ["Yehya", "Ahmad", "Alam", "Yehya"]

c = names.count("Yehya")
d = names.count("a")
print(c)
print(d)
print("=" * 75)

# ---> index() => Returns the index of the first element with the specified value.
a = ["A", "B", "C", "D", "E", "F", "D"]
i = a.index("D")
# i = a.index("DDDD")
print(i)
print("=" * 75)

# ---> pop() => Removes the element at the specified position
a = ["A", "B", "C", "D", "E"]

a.pop(1)

print(a)

a.pop(2)
print(a)
print("=" * 75)

# ---> remove() => Removes the first item with the specified value.
a = ["A", "B", "C", "D", "E"]

a.remove("C")
print(a)
# a.remove("Z") # error
print(a)
print("=" * 75)

# ---> reverse() => Reverses the order of the list.
a = [1, 4, 7, 8, 2]

a.reverse()
print(a)
print("=" * 75)

# ---> sort() => Sorts the list
a = [1, 12, 3, -10, 90]
a.sort(reverse=False)
a.sort(reverse=True)
print(a)

a = ["A", "C", "B", "Z", "F"]
a.sort(reverse=True)
print(a)
print("=" * 75)

# a = [1, "A", 2, 3, "B"] # error
# a.sort()
# print(a)
print("###########################################################################")

# 08- Tuple and Methods:
# A- What are Tuples?
# ---> Tuples are used to store multiple items in a single variable.
names = ("Ahmad", "Alaa", "Ali", "Mona")
print(names)
print(type(names))
print("=" * 75)

# ---> Tuples items are enclosed with parentheses ().
names = ("Ahmad", "Alaa", "Ali", "Mona")
print(names)
print(type(names))
print("=" * 75)

# ---> If we have one single item, we should put coma after it.
name = ("Ahmad", )
name = "Ahmad", 
print(name)
print(type(name))
print(len(name))
print("=" * 75)

# ---> Tuples are ordered, we use indexing and slicing to access their items.
langs = ("Python", "Java", "JavaScript", "C++")
fl = langs[0]
print(fl)
ll = langs[-1]
print(ll)
ftl = langs[0:2]
print(ftl)
print("=" * 75)

names = ( "Ahmad", [ "Ali", [ "Yehya", "Alam" ] ] )

m = names[1][1][1][-1].upper()
print(m)
print("=" * 75)

# ---> Tuples are immutable, we can NOT add, edit and delete.
names = ("Ahmad", "Alaa", "Ali", "Mohamed")
# names[0] = "Ah" # error
# print(names)

# names[0:2] = ["Ali"] # error
# print(names)

# names[-1] = ["A", "B", "C", "D", "E"] # error
# print(names)
print("=" * 75)

# ---> The items are not unique.
names = ("Ahmad", "Alaa", "Ahmad", "Alaa", "Alaa", "Mohamed")
print(names)
print(len(names))
print("=" * 75)

# ---> Tuples can have different data types.
my_list = ("A", 1, 10.9, 1+8j, True, [1, 2, 3], (1, 2, 3, 4), {1, 2}, {"a":1, "b":1})
print(my_list)
print("=" * 75)

# B- Tuples Methods:
# ---> + => Concatenation
t1 = ("Alaa", "Ali")
t2 = ("Ahmad", "Mona")
t3 = ("Maher",)
t = t1 + t2
print(t)
t = t1 + t2 + t3
print(t)

l1 = ["A", "B"]
l2 = ["C", "D"]
# l3 = "Yehya" # error
l = l1 + l2
print(l)
# l = l1 + l2 + l3 # error
# print(l)
print("=" * 75)

# ---> * => repeat object
t = ("A", "B")
print(t * 5)
print("=" * 75)

# ---> count() => Returns the number of elements with the specified value
t = ("Ahmad", "Ali", "Alaa", "Ali")
c = t.count("Ali")
print(c)
print("=" * 75)

# ---> index() => Returns the index of the first element with the specified value
t = ("A", "B", "C", "D", "A")
i = t.index("A")
# e = t.index("Z") # error
print(i)
# print(e) # error
print("###########################################################################")

# 09- Sets and Methods:
# A. What are Sets?
# ---> Sets are used to store multiple items in a single variable.
# ---> Sets items are enclosed with curly braces {}.
s = {"Ahmad", "Ali"}
print(s)
print(type(s))
print("=" * 75)

# ---> Sets are not ordered, we cannot use indexing and slicing to access their items.
a = {"A", "B", "C", "D", "E", "F", "G", "H"}
print(a)
# Indexing
# print(a[0]) # error

# # Slicing # error
# print(a[0:4]) # error
print("=" * 75)

# ---> The items are unique.
a = {"Ahmad", "Ali", "Ali"}
print(a)
print(len(a))
print("=" * 75)

# ---> Sets can only have immutable data types. => List not allowd
a = {"A", 1, True, 1.9, 1+1j, (1, 2, 3)}
# a = {"A", 1, True, 1.9, 1+1j, (1, 2, 3), [1, 2, 3]} # error
print(a)
print("=" * 75)

# B. Sets Methods
# ---> add() => Adds an element to the set
a = {1, 2, 3}
a.add(4)
# a.add([1, 2, 3]) # error
print(a)
print("=" * 75)

# ---> clear() => Removes all the elements from the set
a = {1, 2, 3}
a.clear()
print(a)
print("=" * 75)

# ---> copy() => Returns a copy of the set
a = {1, 2, 3}
b = a.copy()
a.add(4)
print(a)
print(b)
print("=" * 75)

# discard() => Remove the specified item
a = {1, 2, 3, "Y", "D"}
a.discard("Y")
a.discard("Z")
print(a)
print("=" * 75)

# pop()	=> Removes an element from the set
a = {10, 2, 3, 4, 6, 7, 9, -10}
b = a.pop()
print(a)
print(b)
print("=" * 75)

# remove()	=> Removes the specified element
a = {10, 2, 3, 4, 6, 7, 19}
a.remove(10)
# a.remove(100) # error
print(a)
print("=" * 75)

# union()	=> Return a set containing the union of sets
a = {1, 2, 3, 4}
b = {3, 5, 7}
print(a.union(b))
print(a)
print("=" * 75)

# update()	=> Update the set with another set, or any other iterable
a = {1, 2, 3, 4}
b = {3, 5, 7}
a.update(b)
print(a)
print("=" * 75)

# ---> difference() => Returns a set containing the difference between two or more sets
a = {1, 2, 3, 8}
b = {2, 3, 5, 6}

print(a.difference(b))
print(b.difference(a))
print(a)
print("=" * 75)

# difference_update() => Removes the items in this set that are also included in another, specified set
a = {1, 2, 3, 8}
b = {2, 3, 5, 6}

a.difference_update(b)
b.difference_update(a)
print(a)
print(b)
print("=" * 75)

# intersection() => Returns a set, that is the intersection of two or more sets
a = {1, 2, 3, 4, 5}
b = {1, 2, 4, 7, 9}

print(a.intersection(b))
print(b.intersection(a))
print("=" * 75)

# intersection_update() => Removes the items in this set that are not present in other, specified set(s)
a = {1, 2, 3, 4, 5}
b = {1, 2, 4, 7, 9}

a.intersection_update(b)
b.intersection_update(a)
print(a)
print(b)
print("=" * 75)

# symmetric_difference() => Returns a set with the symmetric differences of two sets
a = {1, 2, 4, 6, 3}
b = {1, 3, 9, 8}
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print("=" * 75)

# symmetric_difference_update()	=> inserts the symmetric differences from this set and another
a = {1, 2, 4, 6, 3}
b = {1, 3, 9, 8}
a.symmetric_difference_update(b)
b.symmetric_difference_update(a)
print(a)
print(b)
print("=" * 75)

# isdisjoint() => Returns whether two sets have a intersection or not
a = {2, 3, 4}
b = {1, 8, 9}
c = {1, 4}
print(a.isdisjoint(b))
print(a.isdisjoint(c))
print("=" * 75)

# issubset()	=> Returns whether another set contains this set or not
a = {1, 2, 3}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(b.issubset(a))
print("=" * 75)

# issuperset()	=> Returns whether this set contains another set or not
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4}
print(a.issuperset(b))
print(b.issuperset(a))
print("=" * 75)
print("###########################################################################")

# 10- Dictionary and Methods:
# A- What are Dictionaries
# ---> Dictionaries are used to store data values in key:value pairs.
# ---> Dict items are enclosed in curly braces {}.
# ---> Dict items contains keys:values separated by coma.
person = {
    "name": "Yehya",
    "age": 33
}
print(person)
print(type(person))
print("=" * 75)

# ---> The kays must be immutable data type. List not allowed
# person = {
#     "name": "Yehya",
#     [1, 2, 3]: "test"
# }
# print(person)
print("=" * 75)

# ---> The kays should be unique.
person = {
    "name": "Yehya",
    "age": 33,
    "name": "Ahmad"
}
print(person)
print("=" * 75)

# ---> The values can be any data type.
person = {
    "name": "Yehya",
    "age": 33,
    "skills": [1, 2, 3],
    "reating": 9.8
}
print("=" * 75)

# ---> Dict items are not ordered, we use key name to access the value.
person = {
    "name": "Yehya",
    "age": 33,
    0: "Zero"
}
print( person["name"] )
print( person["age"] )
print( person[0] )
print("=" * 75)

# B- Dict Methods:
# ---> clear()	Removes all the elements from the dictionary
person = {
    "name": "Yehya",
    "age": 22
}
print(person)
print(len(person))

person.clear()
print(person)
print(len(person))
print("=" * 75)

# ---> update()	Updates the dictionary with the specified key-value pairs
user = {
    "name": "Yehya",
    "age": 33,
    "skills": "Test"
}

print(user)

user.update({"country": "Syria"})

print(user)

user["skills"] = [1, 2, 3]
print(user)
print("=" * 75)

# ---> copy() Returns a copy of the dictionary
user = {
    "name": "Ahmad",
    "age": 34
}

print(user)

user_two = user.copy()

user.update({"country": "Syria"})

print(user)
print(user_two)
print("=" * 75)

# ---> get() Returns the value of the specified key
user = {
    "name": "Alaa",
    "age": 33
}

print(user.get("name"))
print(user.get("age"))
print(user.get("ageeee")) # None
print("=" * 75)

# ---> keys()	Returns a list containing the dictionary's keys
# ---> values()	Returns a list of all the values in the dictionary
# ---> items()	Returns a list containing a tuple for each key value pair
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}

print(user.keys())
print(user.values())
print(user.items())
print("=" * 75)

# ---> pop()	Removes the element with the specified key
# ---> popitem()	Removes the last inserted key-value pair
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}
print(user)
user.pop("age")
print(user)

user["skills"] = [1, 2, 3]
print(user)
user.popitem()
print(user)
print("=" * 75)

# ---> setdefault()	Returns the value of the specified key. 
#      If the key does not exist: insert the key, with the specified value
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}

user.setdefault("name", "Ahmad")

user.setdefault("skills", [1, 2, 3])
print(user)
print("=" * 75)

# ---> fromkeys() Returns a dictionary with the specified keys and value

a = ["name", "age", "country"]
b = "x"

user = dict.fromkeys(a, b)

print(user) 
print("=" * 75)
print("###########################################################################")

# 11- Boolean and Methods:
# A- What is boolean?
# ---> In programming you often need to know if an expression is True or False.
x = 10
y = 20

print( x == y )
print(20 == 20)
print(type(True))
print(type(False))
print("=" * 75)

# ---> The bool() function allows you to evaluate any value, and give you True or False in return,

# True values
print(bool(True))
print(bool("Yehya"))
print(bool(" "))
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool(100))
print(bool(100.90))
print(bool(100 + 3j))
print("=" * 75)

# ---> False values
print(bool(False))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(0))
print(bool(None))
print("=" * 75)

# B- Boolean Operators
# and
x = 10
y = 20

print(x < y and x == y )

# or
print(x < y or x == y )

# not
print(not (x < y and x == y) )
print("=" * 75)

# C- Assignments Operators
# =
x = 10
print(x)
print("=" * 75)

# +=
x = 20
x += 10 # x = x + 10
print(x)
print("=" * 75)

# -=
x = 30
x -= 20 # x = x - 20
print(x)

x = 3
x **= 3 # x = x ** 3
print(x)
print("=" * 75)

# D- Comparison Operators 
# ==    Equal
print(10 == 10)
print(10 == 20)
print("=" * 75)

# !=      Not Equal
print(10 != 10)
print(10 != 20)
print("=" * 75)

# >       Grater Than
print(30 > 20)
print(30 > 60)
print("=" * 75)

# <       Less Than
print(10 < 40)
print(10 < 8)
print("=" * 75)

# >=     Grater Than or Equal
print(10 >= 10)
print(10 >= 20)
print("=" * 75)

# <=     Less Than or Equal
print(10 <= 10)
print(10 <= 8)
print("=" * 75)
print("###########################################################################")

# 12- Type Conversion:
# A- What is type conversion with example?
# ---> type conversion, type casting, type coercion, and type juggling 
#      are different ways of changing an expression from one data type to another.

my_age = 33

print("My age is " + str(my_age))

# str()
a = 10
b = 10.9
c = 10 + 5j

print(str(a))
print(str(b))
print(str(c))
print("=" * 75)

# int()
a = "10"
b = "Yehya"
print(int(a))
# print(int(b)) # error
print("=" * 75)

# list()
a = 10
b = "Yehya"
c = (1, 2, 3)
d = {1, 2, 3, 4}
e = {"one": 1, "two": 2, "three": 3}
f = True

# print( list(a) ) # error
print(list(b)) 
print(list(c))
print(list(d))
print(list(e))
# print(list(f)) # error
print("=" * 75)

# tuple()
a = 10
b = "Yehya"
c = [1, 2, 3]
d = {1, 2, 3, 4}
e = {"one": 1, "two": 2, "three": 3}
f = True

# print(tuple(a)) # error
print(tuple(b)) 
print(tuple(c))
print(tuple(d))
print(tuple(e))
# print(tuple(f)) # error
print("=" * 75)

# set()
a = 10
b = "Yehyaa"
c = [1, 2, 3]
d = (1, 2, 3, 4)
e = {"one": 1, "two": 2, "three": 3}
f = True

# print(set(a)) # error
print(set(b)) 
print(set(c))
print(set(d))
print(set(e))
# print(set(f)) # error
print("=" * 75)

# dict()
a = 10
b = "Yehya"
c = [["key1", "value1"], ["key2", "value2"]]
d = (("key1", "value1"), ("key2", "value2"))
# e = {{"key1", "value1"}, {"key2", "value2"}} 
f = True

# print(dict(a)) # error
# print(dict(b)) # error
print(dict(c))
print(dict(d))
# print(dict(e)) #error
# print(dict(f)) # error
print("=" * 75)
print("###########################################################################")

# 13- User Input:
# A- What is User Input?
# ---> The input() function reads a line from the input (usually from the user), 
#       converts the line into a string by removing the trailing newline, and returns it.

# your_name = input("Enter your name. ")
# your_age = input("Enter your age. ")

# print(f"Your name is {your_name} and your age is {your_age}")

# x = input("Enter your..")

# print(x)
# print(type(x))

# your_name = input("Enter your name. ").strip().capitalize()
# your_age = input("Enter your age. ").strip()

# print(f"Your name is {your_name} and your age is {your_age}")
print("###########################################################################")

# 14- Control Flow - If, Elif, Else:
# A- What is control flow in programming?
# ---> The control flow is the order in which the computer executes statements in a script.
# ---> Code is run in order from the first line in the file to the last line, 
#      unless the computer runs across the (extremely frequent) 
#      structures that change the control flow, such as conditionals and loops.

# Syntax:
# if condition:
#     Code to run if True


age = 20

if age > 18:
    print("Accepted!")

# your_age = int(input("Enter your age: ").strip())

# if your_age >= 18:
#     print("Accepted")
# else:
#     print("Not Accpted")


# number = int(input("Enter a number. ").strip())

# if number < 18:
#     print(f"the number {number} is less than 18")
# elif number >= 18 and number < 40:
#     print(f"the number {number} is between 18 and 40")
# else:
#     print(f"the number {number} is greater than 40")
    


age = 20
has_skill = True

if age > 18:
    print("Good > 18")
    
    if has_skill == True:
        print("Good, > 18 and has skill =>  Accepted!")
    
is_subsribed = True
print("Welcome to my channel" if is_subsribed else "Please subsribe to our channel")
print("###########################################################################")

# 15- Loop - While, For and Else:
# A- What is loop in Python?
# ---> Looping means repeating something over and over until a particular condition is satisfied.


# B- Loop => While Loop:
# ---> Syntax:
# while true_condition:
#     code to run
# else:
#     code to run when finished
print("=" * 75)

x = 1

while x <= 10:
    print(x)
    
    x = x + 1
else:
    print("Loop is done!")

names = ["Ahmad", "Yehya", "Alaa", "Alam", "Mona", "Ali", "Alam", "Alam", "Alam", "Alam", "A"]

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])

x = 0
while x < len(names):
    
    print( names[x] )
    
    x += 1 # x = x + 1

# C- Loop => For Loop:
# ---> Syntax:
# for item in iterable_object:
#     code to run
# else:
#     code to run when finished
print("=" * 75)

names = ["Ahmad", "Yehya", "Alaa", "Alam", "Mona", "Ali"]

for name in names:
    print(name)
else:
    print("Loop is done")
print("=" * 75)

for number in range(1, 11):
    print(number)
    
print("=" * 75)

# D- Break, Continue, Pass
# ---> break:

for year in range(2000, 2024):
    
    if year == 2020:
        break
    
    print(year)

# ---> continue

for year in range(2000, 2024):
    
    if year == 2020:
        
        continue
    
    print(year)
    
# ---> pass

if True:
    pass
for year in range(2000, 2022):
    pass

def test():
    pass

print("=" * 75)
print("###########################################################################")

# 16- Function:
# A- What are Python Functions?
# ---> A function is a block of code which only runs when it is called.
# ---> You can pass data, known as parameters, into a function.
# ---> A function can return data as a result.

# B- Creating a Function:
# ---> In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")

# C- Calling a Function:
# ---> To call a function, use the function name followed by parenthesis:
def my_function():
  print("Hello from a function")

my_function()

print("=" * 75)

# D- Function Arguments:
# ---> Information can be passed into functions as arguments.

# ---> Arguments are specified after the function name, inside the parentheses. 
#      You can add as many arguments as you want, just separate them with a comma.

# ---> The following example has a function with one argument (fname). 
#      When the function is called, we pass along a first name, 
#      which is used inside the function to print hello + the name.

def my_function(fname):
    print("Hello " + fname)

my_function("Yehya")
# my_function("Alaa")
# my_function("Ali")
print("=" * 75)

# E- Parameters or Arguments?
# ---> The terms parameter and argument can be used for the same thing: 
#      information that are passed into a function.
# ---> From a function's perspective:
# ---> A parameter is the variable listed inside the parentheses in the function definition.
# ---> An argument is the value that is sent to the function when it is called.


# F6- Number of Arguments:
# ---> By default, a function must be called with the correct number of arguments. 
#      Meaning that if your function expects 2 arguments, 
#      you have to call the function with 2 arguments, not more, and not less.

def my_function(fname, lname):
    print("My full name is: " + fname + " " + lname)

my_function("Yehya", "Ali")
# ---> If you try to call the function with 1 or 3 arguments, you will get an error:
# my_function("Yehya") # error
# my_function("Yehya", "Ali", "Alaa") # error
print("=" * 75)

# G- Default Parameter Value:
# ---> 
def my_function(country = "Syria"):
    print("I am from " + country)

my_function("Egypt")
my_function()
print("=" * 75)

# ---> Function Return:
def sum_two_numbers(n1, n2):
    
    return n1 + n2

result = sum_two_numbers(10, 20) * 10


print(result)

print("=" * 75)

# H- Arbitrary Arguments, *args
# ---> If you do not know how many arguments that will be passed into your function, 
#      add a * before the parameter name in the function definition. 
#      This way the function will receive a tuple of arguments, 
#      and can access the items accordingly:

def my_function(name, *langs):

    print(f"My name is {name}")
    
    print(f"my langs are:")
    
    for lang in langs:
        
        print(lang)

my_langs = ("HTML", "CSS", "Python", "Js", "PHP")

my_function("Yehya", *my_langs)
print("=" * 75)

# I- Arbitrary Keyword Arguments, **kwargs
# ---> If you do not know how many keyword arguments that will be passed into your function, 
#      add two asterisk: ** before the parameter name in the function definition. 
#      This way the function will receive a dictionary of arguments, and can access the items accordingly:


def my_function(name, **langs):
    
    
    # print(type(langs))
    print(f"My name is {name}")
    
    print("My langs with progress are:")
    
    
    for lang_key, lang_value in langs.items():
        
        print(f"{lang_key} => {lang_value}")
    

my_langs = {
    "html": "80%",
    "CSS": "90%",
    "PHP": "70%"
} 
my_function("Yehya", **my_langs)
print("###########################################################################")

# 17- Built in Functions:
# A- What are Built in Functions?
# ---> The built-in Python functions are pre-defined by the python interpreter. 
#      There are 68 built-in python functions. 
#      These functions perform a specific task and can be used in any program, 
#      depending on the requirement of the user.

# 1- print()
a = 10
b = 20
# print(a, b, sep=", ")
# print(a, b, sep="\n")

print(a, end=" | ")
print(b, end="\n")
print("=" * 75)

# 2- all()

numbers = [2, 4, 6, 8, 10, 0]

if all(numbers):
    
    print("All numbers are true")
else:
    print("There is one false value at least")

print("=" * 75)

# 2- any()

numbers = [0, [], ""]

if any(numbers):
    
    print("There is one true value at least")
else:
    print("All numbers are false")

print("=" * 75)

# 4- bin()
print(bin(10))
print("=" * 75)

# 5- id()
a = 10
b = 20
print(id(a))
print(id(b))
print("=" * 75)

# 6- slice()
a = "Yehya"

print(a[ slice(1, 5) ])
print("=" * 75)

# 7- enumerate()
langs = ["HTML", "CSS", "Python", "JavaScript", "PHP"]

for i, lang in enumerate(langs, 1):
    
    print(f"{i} => {lang}")
print("=" * 75)

# 8- help()

# print( help(print) )

print("=" * 75)

# 9- reversed()
langs = ["HTML", "CSS", "Python", "JavaScript", "PHP"]

for lang in reversed(langs):
    
    print(lang)

print("=" * 75)
print("###########################################################################")

# 28- Built In Functions [Map]:
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
print("###########################################################################")

# 19- Built in Functions [Filter]:
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
print("###########################################################################")

# 20- Built in Functions [Reduce]:
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


words = ["yehya", "alaa", "Maherr", "Ebrahim", "Hiba"]

def compare(w1, w2):
    
    if len(w1) > len(w2):
        return w1
    else:
        return w2
    
result = reduce(compare, words)

print(result)
print("###########################################################################")

# 21- Importing Modules:
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

import my_module

my_module.sum_numbers(10, 20)

# D- Importing External Modules:
# ---> pip install module_name
# import numpy as np
# print(np.__version__)
print("###########################################################################")

# ================================ End Level #I ==============================