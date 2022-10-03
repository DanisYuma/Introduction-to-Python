# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xA = int(input('Enter x coordinate of point A> '))
yA = int(input('Enter y coordinate of point A> '))
xB = int(input('Enter x coordinate of point B> '))
yB = int(input('Enter y coordinate of point B> '))
print('Distanse beetween points is', 
round(
    ((xB - xA) ** 2 + (yB - yA) ** 2) ** (1/2), 2),
    )