# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

import string

string = '7 5 3 87 45 6'
lst = list(map(float, string.split()))

print(f'Max = {max(lst)}')
print(f'Min = {min(lst)}')
