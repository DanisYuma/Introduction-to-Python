# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Enter number N> '))
number = N
factors = []

for i in range(2, N):
    while N % i == 0:
        factors.append(i)
        N //= i
if N != 1:
    factors.append(N)
print(f'Prime factors of {number} is {factors}')