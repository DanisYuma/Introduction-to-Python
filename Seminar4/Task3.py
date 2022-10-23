# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

x = int(input())
y = int(input())

if x > y:
    max_i = x
else:
    max_i = y

while True:
    if not max_i % x and not max_i % y:
        print(max_i)
        break
    max_i += 1