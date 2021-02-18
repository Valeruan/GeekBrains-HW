def my_func(x, y):
    result = x ** y
    print(result)


abscissa = int(input('Введите действительное положительное число -'))
ordinate = int(input('Введите целое отрицательное число - '))
my_func(abscissa, ordinate)


def my_alg(x, y):
    return 1 if y == 0 else my_alg(x, y + 1) * 1 / x
    # признаюсь, украл этот прекрасный метод


print(my_alg(abscissa, ordinate))