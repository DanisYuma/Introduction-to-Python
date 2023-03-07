# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
import os

k = int(input('Enter polynomial degree> '))
ratios = [random.randint(0, 10) for i in range(k + 1)]
print(ratios)

factors = []
for ratio in ratios:
    if ratio:
        ratio = ratio if k == 0 else '' if ratio == 1 else ratio
        degree = 'x' if k == 1 else '' if k == 0 else f'x^{k}'
        factor = f'{ratio}{degree}'
        factors.append(factor)
    k -= 1

polynom = ' + '.join(factors) + ' = 0'
print(polynom)

res_dir = 'files'
if not os.path.exists(res_dir):
    os.mkdir(res_dir)               # Создаем директорию если ее нету

with open(f'{res_dir}\\{"_".join(map(str, ratios))}.txt', 'w', encoding='utf-8') as file:
    file.write(polynom)