"""
Задача 3. Напишите программу, которая принимает на вход число 
и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
"""


print('Чтобы узнать, является ли число кратным одновременно 5 и 10, или 15, но не 30, введите это число.')
num = int(input())
if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0: print('Кратно.')
else: print('Не кратно.')
# Число должно делиться без остатка (%) сразу и на 5 и на 10, на что указывают внутренние (сиреневые) скобки.
# Либо же на 15, на что указывают внешние (жёлтые) скобки. И эта кратность 5, 10 и 15 объединена внешними скобками.
#  Однако, числа, кратные 30, не являются в этой задаче кратными и, потому, не объединены скобками.