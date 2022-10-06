# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

number = float(input('Enter number> '))
while int(number) != number:
    number *= 10
sum_digit = 0
while number:
    sum_digit += number % 10
    number //= 10
print(sum_digit)
