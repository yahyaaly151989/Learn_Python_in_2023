# ============================ Exercises About Sets =============================
# 1. What is the output of the following code
# a = {1, 'PYnative', ['abc', 'xyz'], True}
# print(a)

# {1, ‘PYnative’, [‘abc’, ‘xyz’]}
# {1, ‘PYnative’, [‘abc’, ‘xyz’], True}
# TypeError
print("########################################################")

# 2. What is the output of the following set operation
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set1.difference_update(set2)
print(set1)
print("########################################################")

# 3. What is the output of the following
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.add("Blue")
sampleSet.add("Orange")
print(sampleSet)
print("########################################################")

# 4. What is the output of the following set operation
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.update(["Blue", "Green", "Red", "Orange"])
print(sampleSet)
print("########################################################")

# 5. What is the output of the following union operation
set1 = {10, 20, 30, 40}
set2 = {50, 20, "10", 60}

set3 = set1.union(set2)
print(set3)
print("########################################################")

# 6.  What is the output of the following set operation
set1 = {"Yellow", "Orange", "Black"}
set2 = {"Orange", "Blue", "Pink"}

set3 = set2.difference(set1)
print(set3)
print("########################################################")

# 7. What is the output of the following code
sampleSet = {"Yellow", "Orange", "Black"}
# print(sampleSet[1])

# Yellow
# TypeError
# Orange
print("########################################################")

# 8. What is the output of the following
sampleSet = {"Yellow", "Orange", "Black"}
sampleSet.discard("Blue")
print(sampleSet)

# {‘Yellow’, ‘Orange’, ‘Black’}
# KeyError: ‘Blue’
print("########################################################")

# 9. What is the output of the following
sampleSet = {"Yellow", "Orange", "Black"}
# sampleSet.remove("Blue")
# print(sampleSet)

# {‘Yellow’, ‘Orange’, ‘Black’}
# KeyError: ‘Blue’
print("########################################################")

# 10. What is the output of the following
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 10, 30, 40, 80, 20, 50}

print(set1.issubset(set2)) 
print(set2.issuperset(set1))
print("########################################################")

# ================================== End ========================================
