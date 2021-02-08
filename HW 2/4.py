line_user = input('Введите несколько слов через пробел - ')
list = line_user.split()
new = list [0:9]
for ind, el in enumerate(list, 1):
    print(ind, el)