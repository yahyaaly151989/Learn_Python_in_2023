# ===============Type Hinting=============== Debugging Code ========================

nums_list = [1, 2, 3, 4]

nums_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4}

for num_list in nums_list:
    print(num_list)
    
for key, val in nums_dict.items():
    print("{} => {}".format(key, val))
    
def hi(name):
    print("Hello {}".format(name))
    
hi("Yehya")