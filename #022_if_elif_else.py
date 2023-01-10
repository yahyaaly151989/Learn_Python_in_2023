# ========================== Control Flow - If, Elif, Else ===========================
# A- What is control flow in programming?
# ---> The control flow is the order in which the computer executes statements in a script.
# ---> Code is run in order from the first line in the file to the last line, 
#      unless the computer runs across the (extremely frequent) 
#      structures that change the control flow, such as conditionals and loops.

# Syntax:
# if condition:
#     Code to run if True


# age = 20

# if age > 18:
#     print("Accepted!")

# your_age = int(input("Enter your age: ").strip())

# if your_age >= 18:
#     print("Accepted")
# else:
#     print("Not Accpted")


# number = int(input("Enter a number. ").strip())

# if number < 18:
#     print(f"the number {number} is less than 18")
# elif number >= 18 and number < 40:
#     print(f"the number {number} is between 18 and 40")
# else:
#     print(f"the number {number} is greater than 40")
    


# age = 20
# has_skill = True

# if age > 18:
#     print("Good > 18")
    
#     if has_skill == True:
#         print("Good, > 18 and has skill =>  Accepted!")
    
is_subsribed = False

print("Welcome to my channel" if is_subsribed else "Please subsribe to our channel")

        