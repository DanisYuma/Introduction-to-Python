#  Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

a = int(input("Input A> "))
b = int(input("Input B> "))
if a == b ** 2 or b == a ** 2:
    print("Yes")
else:
    print("No")
