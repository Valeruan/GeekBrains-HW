def my_sum(*args):
    try:
        x = 0
        while True:
            component = input('Введите числа через пробел для выхода - 666 - ')
            result = list(map(int, component.split()))
            for el in result:
                x += el
                if el == 666 in result:
                    return x
            fix_x = x
            print(fix_x)

    except ValueError:
        print('Вводите только числа!')


my_sum()