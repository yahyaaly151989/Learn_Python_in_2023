# ============================ Dictionary and Methods =============================
# A- What are Dictionaries
# ---> Dictionaries are used to store data values in key:value pairs.
# ---> Dict items are enclosed in curly braces {}.
# ---> Dict items contains keys:values separated by coma.
person = {
    "name": "Yehya",
    "age": 33
}
print(person)
print(type(person))
print("##############################################################")

# ---> The kays must be immutable data type. List not allowed
# person = {
#     "name": "Yehya",
#     [1, 2, 3]: "test"
# }
# print(person)
print("##############################################################")

# ---> The kays should be unique.
person = {
    "name": "Yehya",
    "age": 33,
    "name": "Ahmad"
}
print(person)
print("##############################################################")

# ---> The values can be any data type.
person = {
    "name": "Yehya",
    "age": 33,
    "skills": [1, 2, 3],
    "reating": 9.8
}
print("##############################################################")

# ---> Dict items are not ordered, we use key name to access the value.
person = {
    "name": "Yehya",
    "age": 33,
    0: "Zero"
}
print( person["name"] )
print( person["age"] )
print( person[0] )
print("##############################################################")

# B- Dict Methods:
# ---> clear()	Removes all the elements from the dictionary
person = {
    "name": "Yehya",
    "age": 22
}
print(person)
print(len(person))

person.clear()
print(person)
print(len(person))
print("##############################################################")

# ---> update()	Updates the dictionary with the specified key-value pairs
user = {
    "name": "Yehya",
    "age": 33,
    "skills": "Test"
}

print(user)

user.update({"country": "Syria"})

print(user)

user["skills"] = [1, 2, 3]
print(user)
print("##############################################################")

# ---> copy() Returns a copy of the dictionary
user = {
    "name": "Ahmad",
    "age": 34
}

print(user)

user_two = user.copy()

user.update({"country": "Syria"})

print(user)
print(user_two)
print("##############################################################")

# ---> get() Returns the value of the specified key
user = {
    "name": "Alaa",
    "age": 33
}

print(user.get("name"))
print(user.get("age"))
print(user.get("ageeee")) # None
print("##############################################################")

# ---> keys()	Returns a list containing the dictionary's keys
# ---> values()	Returns a list of all the values in the dictionary
# ---> items()	Returns a list containing a tuple for each key value pair
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}

print(user.keys())
print(user.values())
print(user.items())
print("##############################################################")

# ---> pop()	Removes the element with the specified key
# ---> popitem()	Removes the last inserted key-value pair
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}
print(user)
user.pop("age")
print(user)

user["skills"] = [1, 2, 3]
print(user)
user.popitem()
print(user)
print("##############################################################")

# ---> setdefault()	Returns the value of the specified key. 
#      If the key does not exist: insert the key, with the specified value
user = {
    "name": "Alaa",
    "age": 33,
    "country": "KSA"
}

user.setdefault("name", "Ahmad")

user.setdefault("skills", [1, 2, 3])
print(user)
print("##############################################################")

# ---> fromkeys() Returns a dictionary with the specified keys and value

a = ["name", "age", "country"]
b = "x"

user = dict.fromkeys(a, b)

print(user) 
print("##############################################################")

# ===================================== End ========================================
