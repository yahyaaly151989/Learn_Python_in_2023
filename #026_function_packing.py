# 7- Default Parameter Value:
# ---> 
def my_function(country = "Syria"):
    print("I am from " + country)

my_function("Egypt")
my_function()
print("=" * 75)

# 8- Arbitrary Arguments, *args
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

# 9- Arbitrary Keyword Arguments, **kwargs
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