def my_division(arg1, arg2):
    try:
        arg1, arg2 = int(arg1), int(arg2)
        res = arg1 / arg2

    except ZeroDivisionError:
        while arg2 == 0:
            arg2 = input('На 0 делить нельзя, введите другое число -')
    except ValueError:
        while arg2 == '':
            arg2 = input('Введите ЧИСЛО! -')


print(my_division(input("Введите числитель - "), input("Введите знаменатель - ")))

#не понимаю что не работает