import random as r

my_list = list(range(r.randint(0, 100)))
r.shuffle(my_list)
print(my_list)
print([my_list[el] for el in range(0, 20) if my_list[el] > my_list[el-1]])