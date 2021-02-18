def my_func(p_1, p_2, p_3):

    if p_1 <= p_2 and p_1 <= p_3:
        print(p_2 + p_3)
        return
    if p_2 <= p_1 and p_2 <= p_3:
        print(p_1 + p_3)
        return
    if p_3 <= p_1 and p_3 <= p_2:
        print(p_1 + p_2)
        return


my_func(int(input('Введите число - ')), int(input('Введите число - ')), int(input('Введите число - ')))