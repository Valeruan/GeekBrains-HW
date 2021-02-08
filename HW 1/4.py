user_num = int(input('Введите любое положительное число и я найду в нём наибольшую цифру -  '))
max_digit = user_num % 10

while user_num > 0:
    numeral = user_num % 10
    if max_digit < numeral:
        max_digit = numeral
        if numeral == 9:
            break

    user_num = user_num // 10
    print(user_num)

print(f"И это цифра {max_digit}")

answer = input('Угадал? - ')
if answer == 'да':
    print('Спасибо!')