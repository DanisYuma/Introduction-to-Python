#  Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

a = int(input('Input A> '))
if ((not a % 5 and not a % 10) or not a % 15) and a % 30:
    print (True)
else:
    print (False)