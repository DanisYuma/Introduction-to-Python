# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random
from unittest import result

lst = []
for i in range(10):
    lst.append(round(random.uniform(0, 10), 2))
print(lst)
print()

min = lst[0] - int(lst[0])
max = lst[0] - int(lst[0])
for item in lst:
    if item - int(item) < min:
        min = item - int(item)
    if item - int(item) > max:
        max = item - int(item)

res = round((max - min), 2)
print(f'{max} - {min} = {res}')