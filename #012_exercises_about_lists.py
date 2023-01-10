# ============================ Exercises About Lists =============================
# 1. In Python, list is mutable
# -> True # -> True
# -> False
print("########################################################")

# 2. What is the output of the following list operation
a = [10, 20, 30, 40, 50]
print (a[-2] ) # 40
print( a[-4:-1] ) # [20, 30, 40]
print("########################################################")

# 3. What is the output of the following
a = [5, 10, 15, 25]
print( a[::-2] ) # [25, 10]
print("########################################################")

# 4. What is the output of the following list function?
a = [10, 20, 30, 40, 50]
a.append(60)
a.append(60)
print(a) # [10, 20, 30, 40, 50, 60, 60]
print("########################################################")

# 5. What is the output of the following code
a = ['zyz', 'zara', 'PYnative']
print ( max(a) ) # zyz
print("########################################################")

# 6. What is the output of the following list assignment
a = [4, 8, 12, 16]
a[1:4] = "yehya" # [8, 12, 16] => "yehya"
# a[1:4] = ["yehya"] # [8, 12, 16] => ["yehya"]
print(a)  # [4, "y", "e", "h", "y", "a"]
print("########################################################")

# 7. What is the output of the following list operation
a = [10, 20, 30, 40, 50, 60, 70, 80]
print(a[2:5]) # [30, 40, 50]
print(a[:4]) # [10, 20, 30, 40]
print(a[3:]) # [40, 50, 60, 70, 80]
print("########################################################")

# 8. What is the output of the following code
a = ["PYnative", [4, 8, 12, 16]]
print( a[0][1] ) # Y   
print( a[1][3] ) # 16
print("########################################################")

# 9. What is the output of the following
l = [None] * 10
print(l)
print(len(l))
print(type(None))
print("########################################################")

# 10. What is the output of the following list function?
a = [10, 20, 30, 40, 50]
a.pop()
print(a) # [10, 20, 30, 40]

a.pop(2)
print(a) # [10, 20, 40]
print("########################################################")

# =================================== End =========================================
