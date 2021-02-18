import random as r

my_list1 = list(range(r.randint(0, 20)))
my_list2 = list(range(r.randint(0, 20)))
r.shuffle(my_list1 and my_list2)
original_list = my_list1 + my_list2
print(original_list)

new_list = [el for el in original_list if original_list.count(el) == 1]
print(new_list)