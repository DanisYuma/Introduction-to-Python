def menu():
    menu_list = {
                1: 'Create dictonary',
                2: 'Download directory from file',
                3: 'Save dictonary',
                4: 'Exit'}
    x = int(input(f'{menu_list} Choose action> '))
    return x
