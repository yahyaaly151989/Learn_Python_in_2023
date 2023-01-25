# ============================== Decorators ========================


# def my_decorator(func):
#     def apply_decorator(first, last):
#         print("Hello")
#         func(first, last)
#         print("Bye")
#     return apply_decorator


# @my_decorator
# def full_name(fn, ln):
#     print(fn + " " + ln)
    
# full_name("Yehya", "Ali")


# def my_decorator(func):
#     def apply_decorator(num1, num2):
#         if type(num1) == str or type(num2) == str:
#             print("+ is concatenation not sum")
#         func(num1, num2)
#     return apply_decorator


# @my_decorator
# def calc(n1, n2):
#     print(n1 + n2)
    
# calc("10", "20")

def my_decorator(func):
    def apply_decorator(num1, num2):
        if type(num1) == str or type(num2) == str:
            print("* is repeat not sum")
        func(num1, num2)
    return apply_decorator


@my_decorator
def calc(n1, n2):
    print(n1 * n2)
    
calc("10", 3)