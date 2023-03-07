# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
lst = random.sample(range(0, 10), 10)
print(lst)
print()
lst2 = list(lst[i] * lst[-i-1] for i in range(len(lst) // 2 + len(lst) % 2))
print(lst2)
