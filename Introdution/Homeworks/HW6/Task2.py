# Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, список повторяемых  и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и  [1, 3, 5] и [1, 2, 5, 3, 10]

import random

data = []

for i in range(int(input('Enter list size\n'))):
    data.append(random.randint(0,10))

rep = []        # Повторяющиеся
non_rep = []        # Не повторяющиеся

for i in data:
    if i not in non_rep or i not in rep:
        if data.count(i) == 1:
            non_rep.append(i)
        else:
            if i not in rep:
                rep.append(i)

print()
print(data)
print(f'Unique elements:\n {list(set(data))}')
print(f'Non-repeating elements:\n {non_rep}')
print(f'Repeating elements:\n {rep}')
