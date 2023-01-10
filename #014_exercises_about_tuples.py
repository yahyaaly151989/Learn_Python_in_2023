# ============================ Exercises About Tuples =============================
# 1. What is the output of the following code
a = (100, 200, 300, 400, 500)
# a[1] = 800 # error
print(a)
print("########################################################")

# 2. What is the output of the following tuple operation
a = (100,)
b = (100)
print(a * 2)
print(b * 2)
print("########################################################")


# 3. A Python tuple can also be created without using parentheses
a = 100, 200, 300
print(type(a))
True
False
print("########################################################")

# 4. What is the output of the following
# tuple1 = (1120, 'a')
# print(max(tuple1))
print("########################################################")

# 5. What is the output of the following
aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
print(aTuple[2:5]) # (30, 40, 50)
print(aTuple[:4]) # (10, 20, 30, 40)
print(aTuple[3:]) # (40, 50, 60, 70, 80)
print("########################################################")

# 6. Choose the correct way to access value 20 from the following tuple
q = ("Orange", [10, 20, 30], (5, 15, 25))

# print( q[1:2][1] ) # ([10, 20, 30],) # error
# print(q[1:2])

# print(q[1:2](1)) # error
print(q[1][1])
print("########################################################")

# 7. What is the output of the following tuple operation
a = (100, 200, 300, 400, 500)
# a.pop(2)
# print(a)
print("########################################################")

# 8. What is the output of the following code
aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2]) # 400
print(aTuple[-4:-1]) # (200, 300, 400)
print("########################################################")

# 9. What is the type of the following variable
aTuple = ("Orange")
print(type(aTuple))
print("########################################################")

# 10. What is the output of the following
aTuple = "Yellow", 20, "Red"
a, b, c = aTuple
print(a)
print(b)
print(c)
print("########################################################")

# =================================== End =========================================
