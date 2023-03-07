# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

print('Введите цифру, обозначающую день недели')
number = int(input('Ener day number> '))
if number in range(1, 6):
    print('no')
elif number in range(6, 8):
    print('yes')
else:
    print('wrong day number')
