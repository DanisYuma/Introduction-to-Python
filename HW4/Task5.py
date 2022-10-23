# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import os

dir = 'files'
text_files = [file for file in os.listdir(dir) if file.endswith('.txt')]

result = {}

for txt_file in text_files:
    with open(f'{dir}\\{txt_file}', encoding='utf8') as data:
        polynom = filter(lambda x: x not in ('+', '=', '0'), data.read().split())

for factor in polynom:
    if 'x^' in factor:
        ratio, degree = map(lambda x: int(x) if x else 1, factor.split('x^'))
        result[degree] = result.get(degree, 0) + ratio
    elif 'x' in factor:
        ratio, _ = map(lambda x: int(x) if x else 1, factor.split('x'))
        result[1] = result.get(1, 0) + ratio
    else:
        result[0] = result.get(0, 0) + int(factor)


result = sorted(result.items(), reverse=True)

factors = []
for degree, ratio in result:
    ratio = ratio if degree == 0 else '' if ratio == 1 else ratio
    degree = 'x' if degree == 1 else '' if degree == 0 else f'x^{degree}'
    factor = f'{ratio}{degree}'
    factors.append(factor)

sum_polynom = ' + '.join(factors) + ' = 0'
print(sum_polynom)