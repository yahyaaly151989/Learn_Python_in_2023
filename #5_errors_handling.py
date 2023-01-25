# ============================== Errors Handling ========================


# print(10 / 0)

# print(x)

# def calc(x, y):
    
#     if x < 0 or y < 0:
#         raise ValueError("The numbers should be positive.")
#     return x + y

# print(calc(-10, 20))

# print("After Function.")


try:
    # print(10 / 2)
    print(10 / 0)
    # print(x)
    
    # print(int("Hi"))

except ZeroDivisionError:
    print("You cannot divide by zero.")
    # print(None)

# except NameError:
#     print("The variable not found.")

# except:
#     print("Error Found, please fix it.")
    
else:
    print("Good, you have no errors.")
    
finally:
    print("This will print.")
    
print("Hi")
