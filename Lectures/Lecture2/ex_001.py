# colors = ['red', 'green', 'blue']
# data = open('lecture.txt', 'w')
# data.writelines(colors)
# data.close

path = 'lecture.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close
exit()