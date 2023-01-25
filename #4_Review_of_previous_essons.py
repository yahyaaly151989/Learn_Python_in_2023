# ========================= Review of Previous Lessons =========================
class Employee:
    
    number_of_employees = 0
    @classmethod
    def show_employees_number(cls):
        return f"We have now {cls.number_of_employees} employees in our company."
    
    @staticmethod
    def have_nice_day(day):
        
        if day == "Friday":
            return "Have a nice Friday"
        else:
            return "We should work today."
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = first_name.lower() + "." + last_name.lower() + "@company.com"
        Employee.number_of_employees += 1
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

print(Employee.number_of_employees)
emp_one = Employee("Yehya", "Ali", 1000)
emp_two = Employee("Ahmad", "Mohamed", 2000)
emp_three = Employee("Alaa", "Mohamed", 3000)
print(Employee.number_of_employees)

print(Employee.show_employees_number())

print(Employee.have_nice_day("Sunday"))

# print(emp_one.first_name)
# print(emp_one.last_name)
# print(emp_one.email)
# print(emp_one.salary)

# print(emp_one.full_name())
# print(Employee.full_name(emp_one))

# print(emp_two.first_name)
# print(emp_two.last_name)
# print(emp_two.email)
# print(emp_two.salary)

# the_name = "Programming"
# print(type(the_name))
# print(the_name.upper())
# print(str.upper(the_name))