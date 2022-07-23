# Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k
import random
k = int(input('Введите степень:'))
example = str(f"{random.randint(0,100)}*x^{k} + {random.randint(0,100)}*x - {random.randint(0,100)} = 0")
print(f'Многочлен с рандомными коэфициентами ({example}) записан в файл file.txt')
data = open('file.txt', 'w')
data.write(example)
data.close()