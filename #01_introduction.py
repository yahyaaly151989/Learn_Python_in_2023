# ========================= Introcuction =========================
# 1- What is OOP?
# ---> OOP is a programming paradigm that uses classes and objects in programming.
# ---> OOP helps you to organize your code and make it reusable and readable.

# 2- What is a Programming Paradigm?
# ---> Programming paradigms are different ways or styles in which a given program 
#      or programming language can be organized.

# ---> Python is a multi-paradigm programming language. 
#    Meaning it supports different styles of writing code.

# 2- What is Class:
# ---> A class is a collection of objects. 
#      A class contains the blueprints or the prototype from which the objects are being created. 
#      It is a logical entity that contains some attributes and methods.

# ---> Attributes are the variables that belong to a class.
# ---> Methods are actions that use the data to do something.

# ---> Classes are created by keyword class.

class User:
    pass

# ---> An instance of a class is an object. It is also known as a class object or class instance.

user_one = User()

print( type(user_one)  )
# ---> Everything in Python is object.

x = 10

print( type(x) )

int(10)

# ---> When creating a class instance Python look for a method called __init__:

# ---> The __init__ method is similar to constructors in C++ and Java. 
#      It is run as soon as an object of a class is instantiated. 
#      The method is useful to do any initialization you want to do with your object. 

# ---> The __init__ methods should contain a parameter called "self," and it should be the first one.

# ---> self-refer to the current object.

class User:
    def __init__(self):
        print("I am a new user.")
        
    def test():
        print("This will not print for now")
        
user_one = User()


print( user_one.__class__ )

x = 10

print( x.__class__ )
print( "yehya".__class__ )
