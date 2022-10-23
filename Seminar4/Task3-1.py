# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

from math import lcm

a, b = tuple(map(int, input('Enter numbers> ').split()))    # ввести 2 числа через пробел

print(f'lcm = {lcm(a, b)}')