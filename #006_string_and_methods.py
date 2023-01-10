# ============================ String Methods ============================
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
print( a.index("I") )
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
a = "100name" #False
b = "my_name" # True
print( a.isidentifier() )
print( b.isidentifier() )

# ================================== End =================================
