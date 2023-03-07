# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

a = 5
data = []

for count in range(a):
    data.append(int(input("Input number> ")))

max_el = data[0]
for value in data:
    if value > max_el:
        max_el = value

print('max:', max_el)