# ========================== Exercises About Function ===========================
# 1. What is the output of the following function call?
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
print("==========================================================================")

# 2. What is the output of the following function call?
def fun1(num):
    return num + 25

num = fun1(5)

print(num)
print("==========================================================================")

# 3. What is the output of the following function call?
def outer_fun(a, b):
    
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)

    return a

result = outer_fun(5, 10)

print(result)
print("==========================================================================")

# 4. What is the output of the add() function call?
def add(a, b):
    return a+5, b+5

result = add(3, 2)

print(result)
print(type(result))
print("==========================================================================")

# =================================== End =======================================
