# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

print({
    i: 3 * i + 1 for i in range(1, int(input('N: ')) +  1)
})