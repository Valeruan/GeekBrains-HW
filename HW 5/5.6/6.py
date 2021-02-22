with open('Timetable', 'r+', encoding='utf-8') as t:
    for line in t:
        subject = line.split()
        subject_semestr = sum(map(int, ''.join([el for el in subject if el == '']).split()))
        print(subject_semestr)
# #непобедил..
