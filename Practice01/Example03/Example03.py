"""
Задача 3. Напишите программу, которая будет 
на вход принимать число N и выводить числа от -N до N.   
Примеры:   
- 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""


print('Введите целое положительное число.')
num = int(input())
print('Вывод чисел в диапазоне от -N до N:', end = ' ')
for i in range(-num, num + 1):
    print(i, end = ', ')