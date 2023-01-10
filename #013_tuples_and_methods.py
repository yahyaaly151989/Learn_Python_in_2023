# ============================ Tuple and Methods =============================
# A- What are Tuples?
# ---> Tuples are used to store multiple items in a single variable.
names = ("Ahmad", "Alaa", "Ali", "Mona")
print(names)
print(type(names))
print("=" * 75)

# ---> Tuples items are enclosed with parentheses ().
names = ("Ahmad", "Alaa", "Ali", "Mona")
print(names)
print(type(names))
print("=" * 75)

# ---> If we have one single item, we should put coma after it.
name = ("Ahmad", )
name = "Ahmad", 
print(name)
print(type(name))
print(len(name))
print("=" * 75)

# ---> Tuples are ordered, we use indexing and slicing to access their items.
langs = ("Python", "Java", "JavaScript", "C++")
fl = langs[0]
print(fl)
ll = langs[-1]
print(ll)
ftl = langs[0:2]
print(ftl)
print("=" * 75)

names = ( "Ahmad", [ "Ali", [ "Yehya", "Alam" ] ] )

m = names[1][1][1][-1].upper()
print(m)
print("=" * 75)

# ---> Tuples are immutable, we can NOT add, edit and delete.
names = ("Ahmad", "Alaa", "Ali", "Mohamed")
# names[0] = "Ah" # error
# print(names)

# names[0:2] = ["Ali"] # error
# print(names)

# names[-1] = ["A", "B", "C", "D", "E"] # error
# print(names)
print("=" * 75)

# ---> The items are not unique.
names = ("Ahmad", "Alaa", "Ahmad", "Alaa", "Alaa", "Mohamed")
print(names)
print(len(names))
print("=" * 75)

# ---> Tuples can have different data types.
my_list = ("A", 1, 10.9, 1+8j, True, [1, 2, 3], (1, 2, 3, 4), {1, 2}, {"a":1, "b":1})
print(my_list)
print("=" * 75)

# B- Tuples Methods:
# ---> + => Concatenation
t1 = ("Alaa", "Ali")
t2 = ("Ahmad", "Mona")
t3 = ("Maher",)
t = t1 + t2
print(t)
t = t1 + t2 + t3
print(t)

l1 = ["A", "B"]
l2 = ["C", "D"]
# l3 = "Yehya" # error
l = l1 + l2
print(l)
# l = l1 + l2 + l3 # error
# print(l)
print("=" * 75)

# ---> * => repeat object
t = ("A", "B")
print(t * 5)
print("=" * 75)

# ---> count() => Returns the number of elements with the specified value
t = ("Ahmad", "Ali", "Alaa", "Ali")
c = t.count("Ali")
print(c)
print("#" * 75)

# ---> index() => Returns the index of the first element with the specified value
t = ("A", "B", "C", "D", "A")
i = t.index("A")
# e = t.index("Z") # error
print(i)
# print(e) # error

# ================================ End ======================================
