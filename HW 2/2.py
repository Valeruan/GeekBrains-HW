user_list = []
count = 0
while count <= 3:
    user_list.append(input('Ведите число - '))
    count += 1

u_l = user_list
print(f"Ваши числа: {u_l[0], u_l[1], u_l[2], u_l[3]}")
print(f"Новый порядок чисел: {u_l[1], u_l[0], u_l[3], u_l[2]}")