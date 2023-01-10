# ============================ Concatenation and String Formatting ============================
# ---> Concatenating means obtaining a new string that contains both of the original strings. 
# ---> We use + operator to concatenate two or more strings.

# ---> Concatenation:
a = "Hello"
b = "Python"
s = " "
c = a + s + b
print(c)
print("=" * 75)

name = "Yehya"
age = 33
print("My name is " + name)
# print("My age is " + age) # TypeError: can only concatenate str (not "int") to str
print("My age is " + str(age))
print("=" * 75)

# ---> String Formatting:
# --->String formatting is also known as String interpolation. 
#     It is the process of inserting a custom string or variable in predefined tex
name = "Yehya"
age = 20
ranking = 9.7

print("My name is %s and my age is %d and my ranking is %f" %(name, age, ranking))
print("My name is %s and my age is %d and my ranking is %.2f" % (name, age, ranking))
print("=" * 75)

print("My name is {:s} and my age is {:d} and my ranking is {:f}" .format(name, age, ranking))
print("My name is {:s} and my age is {:d} and my ranking is {:.2f}" .format(name, age, ranking))
print("=" * 75)

print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:f}")
print(f"my name is {name:s}, my age is {age:d}, my ranking is {ranking:.2f}")

print("=" * 75)

# ---> Escape Sequences Characters
# ---> \b
a = "Hello\bPython"
print(a)
print("#" * 75)

# ---> \
a = "Hello \"Python\""
b = 'Hello \'Python\''
c = "Hello \\ Python"
d = "Hello \
Python"
print(a)
print(b)
print(c)
print(d)
print("#" * 75)

# ---> \n
print( "Hello\nPython" )
print("#" * 75)

# ---> \t
a = "Hello\tPython"
print( a )

b = a.expandtabs(20)
print(b)

# ================================== End =================================

