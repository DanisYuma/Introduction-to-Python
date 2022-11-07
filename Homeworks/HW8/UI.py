import fileIO
import view

def menu(data):
    while True:
        answer = view.show_menu()
        if answer == 1:
            view.show_data(data)
        elif answer == 2:
            # fileIO.add_data(data)
            str_data = input('Enter your data delimited by tab> ')
            row = str_data.split('\t')
            data.append([row[0], row[1], row[2]])
        elif answer == 3:
            str_del = input('Ente ID> ')
            for  i in range(len(data)):
                if data[i][0] == str_del:
                    del (data[i])
        elif answer == 4:
            fileIO.write_data('data.csv', data)
        elif answer == 5:
            print('bye')
            break
        else:
            print('Wrong number')