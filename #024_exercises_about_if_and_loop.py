# ========================== Exercises About If and Loop ===========================
# 1. What is the value of x after the following nested for loop completes its execution?
x = 0
for i in range(10):
    for j in range(-1, -10, -1):
        x += 1
print(x)

print("====================================================")

# 2- What is the output of the following nested loop?
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
    for y in items:
        print(x, y)
print("====================================================")

# 3- Given the nested if-else structure below, what will be the value of x after code execution completes?
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)
print("====================================================")

# 4- What is the value of x
x = 0
while (x < 100):
    x+=2
print(x)
print("====================================================")

# 5- What is the output of the following if statement?

a, b = 12, 4
if a % b:
    print('True')
else:
    print('False')



