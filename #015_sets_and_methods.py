# ============================ Sets and Methods =============================
# A. What are Sets?
# ---> Sets are used to store multiple items in a single variable.
# ---> Sets items are enclosed with curly braces {}.
s = {"Ahmad", "Ali"}
print(s)
print(type(s))
print("#" * 75)

# ---> Sets are not ordered, we cannot use indexing and slicing to access their items.
a = {"A", "B", "C", "D", "E", "F", "G", "H"}
print(a)
# Indexing
# print(a[0]) # error

# # Slicing # error
# print(a[0:4]) # error
print("#" * 75)

# ---> The items are unique.
a = {"Ahmad", "Ali", "Ali"}
print(a)
print(len(a))
print("#" * 75)

# ---> Sets can only have immutable data types. => List not allowd
a = {"A", 1, True, 1.9, 1+1j, (1, 2, 3)}
# a = {"A", 1, True, 1.9, 1+1j, (1, 2, 3), [1, 2, 3]} # error
print(a)
print("#" * 75)

# B. Sets Methods
# ---> add() => Adds an element to the set
a = {1, 2, 3}
a.add(4)
# a.add([1, 2, 3]) # error
print(a)
print("#" * 75)

# ---> clear() => Removes all the elements from the set
a = {1, 2, 3}
a.clear()
print(a)
print("#" * 75)

# ---> copy() => Returns a copy of the set
a = {1, 2, 3}
b = a.copy()
a.add(4)
print(a)
print(b)
print("#" * 75)

# discard() => Remove the specified item
a = {1, 2, 3}
a.discard(1)
a.discard(5)
print(a)
print("#" * 75)

# pop()	=> Removes an element from the set
a = {10, 2, 3, 4, 6, 7, 9, -10}
b = a.pop()
print(a)
print(b)
print("#" * 75)

# remove()	=> Removes the specified element
a = {10, 2, 3, 4, 6, 7, 19}
a.remove(10)
# a.remove(100) # error
print(a)
print("#" * 75)

# union()	=> Return a set containing the union of sets
a = {1, 2, 3, 4}
b = {3, 5, 7}
print(a.union(b))
print(a)
print("#" * 75)

# update()	=> Update the set with another set, or any other iterable
a = {1, 2, 3, 4}
b = {3, 5, 7}
a.update(b)
print(a)
print("#" * 75)

# ---> difference() => Returns a set containing the difference between two or more sets
a = {1, 2, 3, 8}
b = {2, 3, 5, 6}

print(a.difference(b))
print(b.difference(a))
print(a)
print("#" * 75)

# difference_update() => Removes the items in this set that are also included in another, specified set
a = {1, 2, 3, 8}
b = {2, 3, 5, 6}

a.difference_update(b)
b.difference_update(a)
print(a)
print(b)
print("#" * 75)

# intersection() => Returns a set, that is the intersection of two or more sets
a = {1, 2, 3, 4, 5}
b = {1, 2, 4, 7, 9}

print(a.intersection(b))
print(b.intersection(a))
print("#" * 75)

# intersection_update() => Removes the items in this set that are not present in other, specified set(s)
a = {1, 2, 3, 4, 5}
b = {1, 2, 4, 7, 9}

a.intersection_update(b)
b.intersection_update(a)
print(a)
print(b)
print("#" * 75)

# symmetric_difference() => Returns a set with the symmetric differences of two sets
a = {1, 2, 4, 6, 3}
b = {1, 3, 9, 8}
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print("#" * 75)

# symmetric_difference_update()	=> inserts the symmetric differences from this set and another
a = {1, 2, 4, 6, 3}
b = {1, 3, 9, 8}
a.symmetric_difference_update(b)
b.symmetric_difference_update(a)
print(a)
print(b)
print("#" * 75)

# isdisjoint() => Returns whether two sets have a intersection or not
a = {2, 3, 4}
b = {1, 8, 9}
c = {1, 4}
print(a.isdisjoint(b))
print(a.isdisjoint(c))
print("#" * 75)

# issubset()	=> Returns whether another set contains this set or not
a = {1, 2, 3}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(b.issubset(a))
print("#" * 75)

# issuperset()	=> Returns whether this set contains another set or not
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4}
print(a.issuperset(b))
print(b.issuperset(a))
print("#" * 75)

# ================================= End ======================================
