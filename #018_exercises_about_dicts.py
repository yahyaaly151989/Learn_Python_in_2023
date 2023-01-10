# ============================ Dictionary and Methods =============================
# 1- Select the correct way to access the value of a history subject.

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sampleDict["class"]["student"]["marks"]["history"])

print("============================================================")

# 2- Select the all correct way to remove the key marks from a dictionary
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

# student.pop("marks") # True
# del student["marks"] # True
# student.remove("marks") # False
# student.popitem("marks") # False
student.popitem() # True

print(student)
print("============================================================")

# 3- Select the correct way to print Emma’s age.
student = {1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
           2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}}



# print( student[0][1] ) # False
print( student[1]["age"] ) # True
# print(student[0]["age"]) # False
print("============================================================")

# 4- Please select all correct ways to empty the following dictionary
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

# del student # False
# del student[0:2] # False
student.clear() # True

print( student  )
print("============================================================")


# 5- What is the output of the following dictionary operation
# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("age")

# print(temp)

# KeyError: ‘age’
# None
print("============================================================")

# 6- Select the correct ways to get the value of marks key.
student = {
  "name": "Emma",
  "class": 9,
  "marks": 75
}

# m = student.get(2) # False
m = student.get('marks') # True
# m = student[2]
m = student['marks'] # True

print(m)
# ===================================== End ========================================