# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.

# print({
#     (1 + 1 / i) ** i for i in range(1, int(input('N: ')) +  1)
# })
sum = 0
for i in range(1, int(input('N: ')) + 1):
    sum += (1 + 1 / i) ** i
print(sum)
