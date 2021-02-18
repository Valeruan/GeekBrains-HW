from itertools import count, cycle

print('Здесь можно сгенерировать целые числа, задав стартовое.Для завершения введите 666')
for el in count(int(input('Введите стартовое число для генерации - '))):
    if el > 25:
        elem = input('Продолжим или завершим ? - ')
        if elem == 666:
            break

print('Здесь можно повторить все элементы некоторого списка, определённого заранее.')
user_list = input('Введите элементы списка через пробел: ').split()
new_list = cycle(user_list)
exi = None
while exi != '666':
    print(next(new_list), end=' ')
    exi = input()