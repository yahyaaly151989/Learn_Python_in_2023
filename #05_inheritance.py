# ========================= Inheritance =========================
class Employee:    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name.lower() + "." + last_name.lower() + "@company.com"
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# emp_one = Employee("Yehya", "Ali", 1000)

class Developer(Employee):
    def __init__(self, first_name, last_name, salary, lang):

        super().__init__(first_name, last_name, salary)
        
        self.lang = lang
        
    def my_lang(self):
        return f"I am good at {self.lang} programming language."

emp_one = Employee("Ahmad", "Ali", 1000)
dev_one = Developer("Yehya", "Ali", 1000, "Python")

# print(dev_one.lang)
print(dev_one.full_name())
print(dev_one.my_lang())

# print(emp_one.my_lang()) # error
    

print(dir(emp_one))
print(dir(dev_one))