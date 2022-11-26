message = '''What's we gonna do?
1 - view
2 - add a record
3 - delete record on id N
4 - write to file
5 - exit\n'''

def show_data(data):
    for line in data:
        print(line)

def show_menu():
    answer = int(input(message))
    return answer