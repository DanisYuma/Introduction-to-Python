# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
lst = random.sample(range(0, 10), 10)
print(lst)
print()
sum = sum(el for i, el in enumerate(lst) if i % 2)
print(sum)
