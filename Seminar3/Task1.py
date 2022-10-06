# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

lst = ["123", "234", 123, "567"]
N = input('Enter number> ')
for item in lst:
    if str(N) in item:
        print(f'Number {N} in string {item}')
        break
else:
    print('no num')