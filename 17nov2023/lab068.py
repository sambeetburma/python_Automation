import csv

data = [
    ['name', 'age', 'city'],
    ['sambeet', '37', 'kolkata'],
    ['tingri', '31', 'delhi'],
    ['mam', '33', 'bhubaneswar']
]

with open('mynew.csv', 'w') as file:
    writecsv = csv.writer(file)
    for row in data:
        writecsv.writerow(row)