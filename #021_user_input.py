# ========================== User Input ===========================
# A- What is User Input?
# ---> The input() function reads a line from the input (usually from the user), 
#       converts the line into a string by removing the trailing newline, and returns it.

# your_name = input("Enter your name. ")
# your_age = input("Enter your age. ")

# print(f"Your name is {your_name} and your age is {your_age}")

# x = input("Enter your..")

# print(x)
# print(type(x))

your_name = input("Enter your name. ").strip().capitalize()
your_age = input("Enter your age. ").strip()

print(f"Your name is {your_name} and your age is {your_age}")