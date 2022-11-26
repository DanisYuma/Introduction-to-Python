import csv

def read_data(file_name):
    data = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row1, row2, row1 in reader:
            row = row[0].split(';')
            data.append(row)
    return data

def write_data(filename, data):
    with open (filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t', quoting=csv.QUOTE_MINIMAL)
        for line in data:
            writer.writerow([line[0], line[1], line[2]])

# def add_data(data):
#     str_data = input('Enter your data delimited by tab> ')
#     row = str_data.split('\t')
#     data.append([row[0], row[1], row[2]])