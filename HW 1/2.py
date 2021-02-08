what_time = int(input('Введите время в секундах, а я переведу их в привычный для вас формат - '))
hour = what_time // 3600
minutes = (what_time // 60) - (hour * 60)
second = what_time % 60

print(f"{hour} часов {minutes} минут  {second} секунды")

print('Программа завершена успешно')