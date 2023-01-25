# # # ========================= Multiple Inheritance and Method Overriding =========================
# # # class Employee:    
# # #     def __init__(self, first_name, middle_name, last_name, salary):
# # #         self.first_name = first_name
# # #         self.last_name = last_name
# # #         self.salary = salary
# # #         self.email = first_name.lower() + "." + last_name.lower() + "@company.com"
# # #         self.middle_name = middle_name
        
# # #     def full_name(self):
# # #         return f"{self.first_name} {self.middle_name} {self.last_name}"

# # # class Developer(Employee):
# # #     def __init__(self, first_name, middle_name, last_name, salary, lang):
# # #         super().__init__(first_name, middle_name, last_name, salary)
# # #         self.lang = lang
# # #     def my_lang(self):
# # #         return f"I am good at {self.lang} programming language."
    
# # #     def full_name(self):
# # #         return f"{self.first_name} {self.middle_name[0]} {self.last_name}"

# # # emp_one = Employee("Ahmad", "Ebrahim", "Ali", 1000)
# # # dev_one = Developer("Yehya", "Maher", "Mohamed", 2000, "Python")

# # # print(emp_one.full_name())
# # # print(dev_one.full_name())


# # class A:
# #     def __init__(self):
# #         print("I am A")
        
# #     def test_a(self):
# #         print("Test A")
        
# # class B:
# #     def __init__(self):
# #         print("I am B")
        
# #     def test_b(self):
# #         print("Test B")
        
# # class C(A, B):
# #     pass


# # c = C()

# # c.test_a()
# # c.test_b()

# # # print(C.mro())


# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass



# # ========================= Polymorphism =========================

a = 10
b = 20

print(a + b)

s1 = "Hello"
s2 = " Python"

print(s1 + s2)

print(len([1, 2, 3, 4]))


print(len("Hello Python"))

print(len({"One": 1, "Two": 2, "Three": 3}))


class A:
    def test(self):
        print("I am A")
        raise NotImplementedError("This method should be implemented in subclasses.")

class B(A):
    def test(self):
        print("I am B")

class C(A):
    def test(self):
        print("I am C")

c = C()
b = B()

c.test()
b.test()







