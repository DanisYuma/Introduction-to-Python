# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

number = int(input('Enter N> '))
print(*((-3) ** i for i in range (number)), sep=', ')