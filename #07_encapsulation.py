# ========================= Encapsulation =========================
# class User:
#     def __init__(self, name):
#         self.name = name # public
# user_one = User("Yehya")

# print(user_one.name)
# user_one.name = "Alaa"
# print(user_one.name)

# class User:
#     def __init__(self, name):
#         self._name = name # protected
        
# user_one = User("Yehya")

# print(user_one._name)
# user_one._name = "Alaa"
# print(user_one._name)

# class User:
#     def __init__(self, name):
#         self.__name = name # private
        
#     def hi(self):
#         return f"Hi {self.__name}"  
        
# user_one = User("Yehya")

# print(user_one.hi())

# print(user_one.__name) # error

# print(user_one._User__name)


# user_one._User__name = "Alaa"

# print(user_one._User__name)


class User:
    def __init__(self, name):
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
user_one = User("Yehya")

print(user_one.get_name())

user_one.set_name("Alaa")

print(user_one.get_name())