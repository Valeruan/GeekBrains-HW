with open('employee - salary', 'r', encoding='utf-8') as f:
    emplo_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    avarage_income = sum(emplo_dict.values()) / len(emplo_dict)
    top_salary = [el[0] for el in emplo_dict.items() if el[1] > 20000]
    print(f"Сотрудники {top_salary} имеют зарплату больше 20к\nА средний доход среди сотрубников - {avarage_income} ")
