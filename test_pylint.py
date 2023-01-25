# # ============================== Pylint ========================
# """
# This module bla bla bla
# """


# MY_NAME = 33

# print(MY_NAME)

# def say_hello(the_name):
#     """This function is bla bla bla"""
#     print(f"Hello {the_name}")
# say_hello("Yehya")



# def remainder(a,b):
#     try:
#         return max(a,b) % min(a,b)
#     except:
#         return None

        
# print(remainder(17, 5))
# print(remainder(13, 72))
# print(remainder(-1, 0))
# print(remainder(1, 0))

def excluding_vat_price(price):
    return price - price * 0.15

print(excluding_vat_price(230))