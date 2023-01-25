# ========================= Object Attributes And Methods =========================
class User:
    
    def __init__(self, fn, ln, email):
        
        self.first_name = fn
        
        self .last_name = ln
        
        self.email = email
        
    def login(self):
        
        return "I am signed in."
    
    def get_full_name(self):
        
        return f"{self.first_name} {self.last_name}"
        
        
user_one = User("Yehya", "Ali", "y@yahoo.com")

user_two = User("Alaa", "Ahmad", "a@a.com")

print( user_one.first_name )
print( user_one.last_name )
print(user_one.email )

print( user_one.login() )

print( user_one.get_full_name() )

print("=" * 75)

print( user_two.first_name )
print( user_two.last_name )
print(user_two.email )
print( user_two.get_full_name() )

print( dir(user_one) )

print("=" * 75)

print( dir(str) )