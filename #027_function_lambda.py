# ========================== Function Lambda ===========================
# 1- Function Lambda:
# ---> A lambda function is a small anonymous function.
# ---> A lambda function can take any number of arguments, but can only have one expression.


# def mu_function(name):
#     return f"Hello {name}"

# r = mu_function("Alaa")

# print(r)

# r = lambda name: f"Hello {name}"
# print(r("Alaa"))


x = lambda a : a + 10
print( x(5) )

x = lambda a, b : a * b
print( x(5, 6) )

x = lambda a, b, c : a + b + c
print( x(5, 6, 2) )


print("============================================================")

# 2- Function Scope:

# a = 10

def test():
    
    global a
    a = 20

    print(a)
    
test()


print(a)
