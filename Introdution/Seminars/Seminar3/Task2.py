# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
N = input('Enter string> ')
counter = 0
target_counter = 2

for i, el in enumerate(lst):
    if N == el:
        counter += 1
        if counter == target_counter:
            print(f'{counter} entering of {N} in index {i}')
            break
else:
    print(f'{target_counter} string not founded')