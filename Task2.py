# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа 
number = int(input('Введите число:'))
result = []
def mylt(number):
    for i in range(2, number+1):
        if number % i == 0:
            number = int(number / i)
            result.append(i)
            mylt(number)
            break
mylt(number)
print(f'Простые множители числа {number} это {result}')