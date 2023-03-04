list = []

for i in range(1, 101):
    if(i % 2 == 0):
        list.append(i)

print(list)

list = [i for i in range(1,21) if i % 2 == 0]
print(list)

tuple = [(i, i+1) for i in range(1,21) if i % 2 == 0]
print(tuple)

square = [(i, i**2) for i in range(1,21) if i % 2 == 0]
print(square)