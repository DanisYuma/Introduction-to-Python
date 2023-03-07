def create_data():
    import random
    from datetime import date
    global id
    global name 
    global birthdate
    global phone_1
    global phone_2

    id = []
    name = []
    birthdate = []
    phone_1 = []
    phone_2 = []
    n = int(input('Enter directory size> '))
    for i in range(n * 1):
        id.append(i)
        name.append('user'+str(i + 1))
        birthdate.append(date.today().replace(day = random.randint(1, 28),
                                              month = random.randint(1, 12),
                                              year = random.randint(1960, 2001)))
        phone_1.append(random.randint(10000, 99999))
        phone_2.append(random.randint(10000, 99999))
    return id, name, birthdate, phone_1, phone_2

def save_data():
    global id
    global name 
    global birthdate
    global phone_1
    global phone_2

    with open('phonebook.csv', 'w') as file:
        for i in id:
            file.writelines(str(id[i])+' '+name[i]+' '+str(birthdate[i])+' '
                            + str(phone_1[i])+' '+str(phone_2[i])+"\n")

def get_data():
    global id
    global name
    global birthdate
    global phone_1
    global phone_2

    id = []
    name = []
    birthdate = []
    phone_1 = []
    phone_2 = []
    data = open('phonebook.csv', 'r')
    for line in data:

        items = []
        items = line.split()

        id.append(int(items[0]))
        name.append(items[1])
        birthdate.append(items[2])
        phone_1.append(items[3])
        phone_2.append(items[4])
    data.close()
    return (id, name, birthdate, phone_1, phone_2)