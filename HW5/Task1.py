# Напишите программу, удаляющую из текста все слова, содержащие "абв".

txt = 'автобус, варенье, лист, осень, кружка, блин, панкейк, клавиатура'
lst = txt.replace(',','')
lst = lst.split()
print(lst)

result = filter(lambda x: 'а' not in x and 'б' not in x and 'в' not in x, lst)
print(*result)