# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

lst = [1, 5, 2, 3, 4, 6, 1, 7]

for i in range(len(lst)):
    result = [lst[i]]
    for j in range(i, len(lst)):
        if lst[j] > result[len(result) - 1]:
            result.append(lst[j])
    if len(result) != 1:
        break

print(result)