# Создайте программу для игры с конфетами человек против человека.

#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#  За один ход можно забрать не более чем 28 конфет. 
#  Все конфеты оппонента достаются сделавшему последний ход. 
#  Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

def input_data(name):
    x = int(input(f"{name}, enter the number of sweets you will take from 1 to 28> "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, enter the correct amount of sweets> "))
    return x


def p_print(name, k, rem):                          # rem = ramaining
    print(f"{name}'s turn, he took {k}. There are {rem} sweets left on the table.")

player1 = input("Enter first player's name> ")
player2 = input("Enter second player's name> ")
rem = int(input("Enter number of sweets on the table> "))
flag = randint(0,2)                                 # флаг очередности
if flag:
    print(f"First turn for {player1}")
else:
    print(f"First turn for {player2}")

while rem > 28:
    if flag:
        k = input_data(player1)
        rem -= k
        flag = False
        p_print(player1, k, rem)
    else:
        k = input_data(player2)
        rem -= k
        flag = True
        p_print(player2, k, rem)

if flag:
    print(f"{player1} win")
else:
    print(f"{player2} win")