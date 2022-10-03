# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Enter quarter number> '))
if quarter_number in range(1, 5):
    if quarter_number == 1:
        x = 'x > 0'
        y = 'y > 0'
    elif quarter_number == 2:
        x = 'x < 0'
        y = 'y > 0'
    elif quarter_number == 3:
        x = 'x < 0'
        y = 'y < 0'
    elif quarter_number == 4:
        x = 'x > 0'
        y = 'x < 0'
    print (f'Range of possible coordinates is: {x}, {y}')
else:
    print('there is no such quarter')
