# ========================== Function Introduction ===========================
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
# ---> Function Return:
def sum_two_numbers(n1, n2):
    
    return n1 + n2

result = sum_two_numbers(10, 20) * 10


print(result)

print("=" * 75)

# G- Default Parameter Value:
# ---> 
def my_function(country = "Syria"):
    print("I am from " + country)

my_function("Egypt")
my_function()
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

my_langs = ("HTML", "CSS", "Python", "Js")

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
    "CSS": "90%"
} 
my_function("Yehya", **my_langs)

# ==================================== End =========================================


















# ================================ End =======================================
