with open('1.txt', 'w', encoding='utf-8') as f1:
    line = input('Введите строку любимой песни - ')
    while True:
        line1 = input('А помните следующую строку ? - ')
        if line1 == 'нет':
            break
        f1.write(f'{line}\n {line1}\n')

f1 = open('1.txt', encoding='utf-8')
song = f1.read()
print(song)
