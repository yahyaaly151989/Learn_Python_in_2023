# ============================ Exercises About Previous Lessons ============================
# ---> Introduction
# ---> Syntax and Comments
# ---> Variables
# ---> Data Types
# ---> String (Indexing, Slicing, Methods, Concatenation)
print("######################################################")
# 1- Output the following message to the screen in one statement:
# Python is an "interpreted" programming language.
# It is a 'high-level' programming language.
print("Python is an \"interpreted\" programming language.\nIt is a 'high-level' programming language.")
print("######################################################")

# 2- Output the following message to the screen in two statements in one line:
# Python is an "interpreted" programming language.
# It is a 'high-level' programming language.
print("Python is an \"interpreted\" programming language"); print("It is a 'high-level' programming language.")
print("######################################################")

# 3- What is the output of these commands?
print( type( 34 ) ) # int
print( type( -91.0 ) ) # float
print( type( -9.8 + 3.0j ) ) # complex
print( type( "Hi All" ) ) # str
print( type( "I am 30 years old"[5] ) ) # str
print( type( "Hello All".split() ) ) # list
print( type( (1, 2, 3) ) ) # tuple
print( type( {1, 2, 3} ) ) # set
print( type( {"A": 1, "B": 2, "C": 3} ) ) # dict
print( len( "Hello-Python".split() )  ) # 1
print( len( "Hello-Python".split("-") )  ) # 2
print( len( "Hello-Python" ) ) # 12
print("######################################################")

# 4- Write 3 variables (name, age, and country) and give them ("Ali", 25, "Egypt")
# Put them all on one line.
name, age, country = "Ali", 25, "Egypt"
print(name, age, country)
print("######################################################")

# 5- Obtian the same output in one line:
my_string = "          i love python.#@#@#@#@#@#@"

# a = my_string.lstrip()
# b = a.rstrip("#@")
# c = b.title()
# print(c)

print( my_string.lstrip().rstrip("#@").title() ) # I Love Python.
print("######################################################")

# 6- Obtian the same output in one line:
a = "EstrMacbOfghCzyxLtrnEabcw"
# b = "1234"

# print( b[-1:-5:-1] )

print( a[-1:-(len(a) + 1):-4].swapcase() ) # Welcome
print("######################################################")

# 7- Obtian the same output in one line:
a = "I love Python + I love Programming"

print( a.replace("+", "|") ) # I love Python | I love Programming

print( " | ".join(a.split(" + ")) ) # I love Python | I love Programming
print("######################################################")

# 8- What is the output of these commands?
a = "I love Python, I love it because Python is easy."
print( a.index("I") ) # 0
print( a.index("P") ) # 7
print( a.index("Python") ) # 7
print( a.index("I", 10, 20) ) # 15
# print( a.index("Python", 10, 20) ) # error
# print( a.index("I", 20) ) # error
print( a.find("I", 20) ) # -1
print( a.count("I", 2, 6) ) # 0
print( a.count("Python", 2, 6) ) # 0
print( len( " ".join( ["Yehya", "Ali"] ) ) ) # 9
print("######################################################")

# 9- What is the output of these commands?
a = "I love Python"

print( a.istitle() ) # False
print( a.isupper() ) # False
print( a.lower().islower() ) # True
print( a.startswith("I", 1) ) # False
print( a.endswith(" ", 0, 2) ) # True
print( a.isidentifier() ) # False
print( a.replace(" ", "_").isidentifier() ) # True
print("######################################################")

# 10- Obtian the same output in one line:
a = "10"
b = "3"
print( b + a.zfill(3) ) # 3010

# ======================================= End ===============================================
