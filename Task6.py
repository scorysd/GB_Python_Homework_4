# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников 
# и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет 
# оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
# Выполнить подсчёт средней величины дохода сотрудников.
import re
data = open('pay.txt', 'r')
data = (re.split(',| |\n', data.read()))
name, pay = [], []
for i in range(len(data)):
    if i % 2 == 0:
        name.append(data[i])
    else:
        pay.append(data[i])    
for i in range(len(pay)):
    if float(pay[i]) < 20000:
        print(f'Оклад меньше 20 тысяч у сотрудника с фамилией {name[i]}, и составляет {pay[i]}')
pay = [float(item) for item in pay]
print(f'Средняя величина дохода сотрудников {sum(pay) / len(pay)}')