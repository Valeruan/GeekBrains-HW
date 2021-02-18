def param(_):
    count = 0
    while count <= 9:
        new_data = []
        all_data = ['name ', 'surname ', 'year of birth ', 'city of residence ', 'email ', 'telephone ']
        for el in all_data:
            data = input(f"Введите ваше {el}")
            new_data.append(data)
        count += 1
        print(new_data)
        break


param(1)