# ========================== Built In Functions ===========================
# A- What are Built in Functions?
# ---> The built-in Python functions are pre-defined by the python interpreter. 
#      There are 68 built-in python functions. 
#      These functions perform a specific task and can be used in any program, 
#      depending on the requirement of the user.

# 1- print()
a = 10
b = 20
# print(a, b, sep=", ")
# print(a, b, sep="\n")

print(a, end=" | ")
print(b, end="\n")
print("=" * 75)

# 2- all()

numbers = [2, 4, 6, 8, 10, 0]

if all(numbers):
    
    print("All numbers are true")
else:
    print("There is one false value at least")

print("=" * 75)

# 2- any()

numbers = [0, [], ""]

if any(numbers):
    
    print("There is one true value at least")
else:
    print("All numbers are false")

print("=" * 75)

# 4- bin()
print(bin(10))
print("=" * 75)

# 5- id()
a = 10
b = 20
print(id(a))
print(id(b))
print("=" * 75)

# 6- slice()
a = "Yehya"

print(a[ slice(1, 5) ])
print("=" * 75)

# 7- enumerate()
langs = ["HTML", "CSS", "Python", "JavaScript", "PHP"]

for i, lang in enumerate(langs, 1):
    
    print(f"{i} => {lang}")
print("=" * 75)

# 8- help()

# print( help(print) )

print("=" * 75)

# 9- reversed()
langs = ["HTML", "CSS", "Python", "JavaScript", "PHP"]


for lang in reversed(langs):
    
    print(lang)

print("=" * 75)


# =================================== End =======================================

