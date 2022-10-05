# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
from random import randint

def get_numbers(N):
    return [randint(-N, N) for i in range(-N, N + 1)]

N = 46
numbers = get_numbers(N)

path = 'file.txt'
data = open(path, 'r')
dlist = [int(line.strip()) for line in data]
data.close()

res = 1
for i in dlist:
    res *= numbers[i]

print(numbers)
print(dlist)
print(res)
