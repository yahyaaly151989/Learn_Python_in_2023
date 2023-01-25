# ========================= Regular Expressions =========================

import re

# text = "Yehya Ali"
# pattern = r"[A-Z]"

# search = re.search(pattern, text)

# # print(dir(search))

# print(search)
# print(search.string)
# print(search.span())
# print(search.group())

# text = "Yehya Ali Ebrahim AAA"
# pattern = r"[A-Z]"

# search = re.findall(pattern, text)

# # print(dir(search))
# # print(type(search))

# print(search)



# text = "Yehya Ali Ebrahim AAA"
# pattern = r"\s"
# my_elements = re.split(pattern, text, 2)
# print(my_elements)


text = "Yehya Ali Ebrahim AAA"
pattern = r"\s"
my_elements = re.sub(pattern, "@" ,text, 2)
print(my_elements)
