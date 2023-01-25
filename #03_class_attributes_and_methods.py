# ========================= Class Attributes And Methods =========================
class User:
    
    emails = []
    users_number = 0
    
    @classmethod
    def show_users_count(cls):
        
        return f"We have now {User.users_number} users in our application."
    
    def __init__(self, first_name, last_name, email):
        
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        if self.email not in User.emails:
            User.emails.append(self.email)
            User.users_number += 1
        else:
            raise ValueError("Email already exists.")
    
    def get_full_info(self):
        
        return f"Welcome {self.first_name} {self.last_name} your email is {self.email}"


print(User.users_number)     
user_one = User("Yehya", "Ali", "y@y.com")
user_two = User("Ahmad", "Ali", "a@y.com")
user_three = User("Ahmad", "Ali", "a1@y.com")
print(User.users_number)     


print(User.show_users_count())



print(User.emails)
# print(user_one.get_full_info())