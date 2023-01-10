# ============================ List and Methods =============================
# A- What are Lists?
# ---> Lists are used to store multiple items in a single variable.
names = ["Ahmad", "Alaa", "Ali", "Mona"]
print(names)
print("=" * 75)

# ---> List items are enclosed with square brackets [].
names = ["Ahmad", "Alaa", "Ali", "Mona"]
print(names)
print(type(names))
print("=" * 75)

# ---> Lists are ordered, we use indexing and slicing to access their items.
langs = ["Python", "Java", "JavaScript", "C++"]
fl = langs[0]
ll = langs[-1]
ftl = langs[0:2]
print("=" * 75)

names = [ "Ahmad", [ "Ali", [ "Yehya", "Alam" ] ] ]

m = names[1][1][1][-1].upper()
print(m)
print("=" * 75)

# ---> Lists are mutable, we can add, edit and delete.
names = ["Ahmad", "Alaa", "Ali", "Mohamed"]
names[0] = "Ah"
print(names)


names[0:2] = ["Ali"]
print(names)

names[-1] = ["A", "B", "C", "D", "E"]
print(names)
print("=" * 75)

# ---> The items are not unique.
names = ["Ahmad", "Alaa", "Ahmad", "Alaa", "Alaa", "Mohamed"]
print(names)
print("=" * 75)

# ---> Lists can have different data types.
my_list = ["A", 1, 10.9, 1+8j, True, [1, 2, 3], (1, 2, 3, 4), {1, 2}, {"a":1, "b":1}]
print(my_list)
print("=" * 75)

# B- List Methods:
# ---> append() => append() => Adds an element at the end of the list.
a = ["Ahmad", "Ali", "Alaa"]
a.append("Yehya")
a.append([1, 2, 3])
print(a)
print("=" * 75)

# ---> extend() => Add the elements of a list (or any iterable), to the end of the current list.
a = [1, 2, 3]
# a.append([4, 5, 6])
a.extend([4, 5, 6])
# a.extend(True) # error
# a.extend(1) # error
a.extend("Yehya") # error
print(a)
print("=" * 75)

# ---> insert() => Adds an element at the specified position.
a = ["A", "B", "C", "D", "E", "F", "D"]

a.insert(0, "Y")
a.insert(3, "DDD")
a.insert(-1, "ZZ")
print(a)
print("=" * 75)

# ---> clear() => Removes all the elements from the list.
a = ["A", "B", "C"]
a.clear()
print(a)
print(len(a))
print("=" * 75)

# ---> copy() => Returns a copy of the list
a = [1, 2, 3]

b = a.copy()

print(b)

a.append(4)
print(a)
print(b)
print("=" * 75)

# ---> count() => Returns the number of elements with the specified value.
names = ["Yehya", "Ahmad", "Alam", "Yehya"]

c = names.count("Yehya")
d = names.count("a")
print(c)
print(d)
print("=" * 75)

# ---> index() => Returns the index of the first element with the specified value.
a = ["A", "B", "C", "D", "E", "F", "D"]
i = a.index("D")
# i = a.index("DDDD")
print(i)
print("=" * 75)

# ---> pop() => Removes the element at the specified position
a = ["A", "B", "C", "D", "E"]

a.pop(1)

print(a)

a.pop(2)
print(a)
print("=" * 75)

# ---> remove() => Removes the first item with the specified value.
a = ["A", "B", "C", "D", "E"]

a.remove("C")
print(a)
# a.remove("Z") # error
print(a)
print("=" * 75)

# ---> reverse() => Reverses the order of the list.
a = [1, 4, 7, 8, 2]

a.reverse()
print(a)
print("=" * 75)

# ---> sort() => Sorts the list
a = [1, 12, 3, -10, 90]
a.sort(reverse=False)
a.sort(reverse=True)
print(a)



a = ["A", "C", "B", "Z", "F"]
a.sort(reverse=True)
print(a)
print("=" * 75)

# a = [1, "A", 2, 3, "B"] # error
# a.sort()
# print(a)

# ================================ End ======================================
