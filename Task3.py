# Задайте последовательность чисел. Напишите программу, которая выведет 
# список неповторяющихся элементов исходной последовательности.
import random
n = int(input("Введите количество элементов последовательности:"))
col = [random.randint(-n,n) for i in range(n)]
unique_col = [i for i in col if col.count(i) == 1]
print(f'Уникальные элементы последовательности {col} равны\n {unique_col}')
