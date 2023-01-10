# ========================== Loop - While, For and Else ===========================
# A- What is loop in Python?
# ---> Looping means repeating something over and over until a particular condition is satisfied.


# B- Loop => While Loop:
# ---> Syntax:
# while true_condition:
#     code to run
# else:
#     code to run when finished
print("#" * 75)

# x = 100

# while x <= 10:
#     print(x)
    
#     x = x + 1
# else:
#     print("Loop is done!")

# names = ["Ahmad", "Yehya", "Alaa", "Alam", "Mona", "Ali", "Alam", "Alam", "Alam", "Alam", "A"]

# # print(names[0])
# # print(names[1])
# # print(names[2])
# # print(names[3])
# # print(names[4])
# # print(names[5])

# x = 0

# while x < len(names):
    
#     print( names[x] )
    
#     x += 1 # x = x + 1

# C- Loop => For Loop:
# ---> Syntax:
# for item in iterable_object:
#     code to run
# else:
#     code to run when finished
print("#" * 75)

names = ["Ahmad", "Yehya", "Alaa", "Alam", "Mona", "Ali"]

for name in names:
    print(name)
else:
    print("Loop is done")
print("#" * 75)

for number in range(1, 11):
    print(number)
    
print("#" * 75)

# D- Break, Continue, Pass
# ---> break:

for year in range(2000, 2024):
    
    if year == 2020:
        break
    
    print(year)

# ---> continue

for year in range(2000, 2024):
    
    if year == 2020:
        
        continue
    
    print(year)
    
# ---> pass

if True:
    pass
for year in range(2000, 2022):
    pass

def test():
    pass

print("#" * 75)


