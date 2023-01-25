# ============================== Iterators & Generators ========================

# ls = ["A", "B", "C", "D", "E", "F", "G", "H"]

# for l in ls:
#     print(l)
    
# print("#" * 75)

# ss = "Yehya"
# for s in ss:
#     print(s)
# print("#" * 75)

# ns = True

# for n in ns:
#     print(n)

# ls = ["A", "B", "C", "D"]

# it = iter(ls)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# for l in iter( "Yehya"):
#     print(l)



# def get_one():
#     return 1
#     return 2
#     return 3
#     return 4

# print(get_one())

def get_one():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


g = get_one()
print(next(g))
print("Sep")
print(next(g))


print("#" * 75)

for n in g:
    print(n)

