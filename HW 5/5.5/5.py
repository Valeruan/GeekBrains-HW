from random import randint
with open('Big Data Sum', 'w+', encoding='utf-8') as bd:
    bd.write(' '.join([str(randint(1, 1000)) for el in range(50000)]))
    bd.seek(0)
    print(sum(map(int, bd.readline().split())))
