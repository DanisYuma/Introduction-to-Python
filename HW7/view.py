def show(key, user, birthdate, phone_1, phone_2):
    # key, user, birthdate, phone_1, phone_2 = data
    result = ''
    print('id name birthdate phone_1 phone_2')
    for i in key:
        result = str(key[i]) + ' ' +str(user[i])+' ' +str(birthdate[i])+ ' ' + str(phone_1[i])+ ' ' + str(phone_2[i])
        print(result)