# ============================ Boolean and Methods ================================
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
print("#" * 75)

# B- Boolean Operators
# and
x = 10
y = 20

print(x < y and x == y )

# or
print(x < y or x == y )

# not
print(not (x < y and x == y) )
print("#" * 75)

# C- Assignments Operators
# =
x = 10
print(x)
print("#" * 75)

# +=
x = 20
x += 10 # x = x + 10
print(x)
print("#" * 75)

# -=
x = 30
x -= 20 # x = x - 20
print(x)

x = 3
x **= 3 # x = x ** 3
print(x)
print("#" * 75)

# D- Comparison Operators 
# ==    Equal
print(10 == 10)
print(10 == 20)
print("#" * 75)

# !=      Not Equal
print(10 != 10)
print(10 != 20)
print("#" * 75)

# >       Grater Than
print(30 > 20)
print(30 > 60)
print("#" * 75)

# <       Less Than
print(10 < 40)
print(10 < 8)
print("#" * 75)

# >=     Grater Than or Equal
print(10 >= 10)
print(10 >= 20)
print("#" * 75)

# <=     Less Than or Equal
print(10 <= 10)
print(10 <= 8)
print("#" * 75)


# ===================================== End =======================================
