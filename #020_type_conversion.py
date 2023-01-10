# ============================ Type Conversion ================================
# A- What is type conversion with example?
# ---> type conversion, type casting, type coercion, and type juggling 
#      are different ways of changing an expression from one data type to another.

my_age = 33

print("My age is " + str(my_age))

# str()
a = 10
b = 10.9
c = 10 + 5j

print(str(a))
print(str(b))
print(str(c))
print("#" * 75)

# int()
a = "10"
b = "Yehya"
print(int(a))
# print(int(b)) # error
print("#" * 75)

# list()
a = 10
b = "Yehya"
c = (1, 2, 3)
d = {1, 2, 3, 4}
e = {"one": 1, "two": 2, "three": 3}
f = True

# print( list(a) ) # error
print(list(b)) 
print(list(c))
print(list(d))
print(list(e))
# print(list(f)) # error
print("#" * 75)

# tuple()
a = 10
b = "Yehya"
c = [1, 2, 3]
d = {1, 2, 3, 4}
e = {"one": 1, "two": 2, "three": 3}
f = True

# print(tuple(a)) # error
print(tuple(b)) 
print(tuple(c))
print(tuple(d))
print(tuple(e))
# print(tuple(f)) # error
print("#" * 75)

# set()
a = 10
b = "Yehyaa"
c = [1, 2, 3]
d = (1, 2, 3, 4)
e = {"one": 1, "two": 2, "three": 3}
f = True

# print(set(a)) # error
print(set(b)) 
print(set(c))
print(set(d))
print(set(e))
# print(set(f)) # error
print("#" * 75)

# dict()
a = 10
b = "Yehya"
c = [["key1", "value1"], ["key2", "value2"]]
d = (("key1", "value1"), ("key2", "value2"))
e = {{"key1", "value1"}, {"key2", "value2"}} 
f = True

# print(dict(a)) # error
# print(dict(b)) # error
print(dict(c))
print(dict(d))
# print(dict(e)) #error
# print(dict(f)) # error
print("#" * 75)
# ===================================== End ===================================