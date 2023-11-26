import csv

temp_data = []

with open("age_update.csv", 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        temp_data.append(row)

temp_data[2][2] = 31
print(temp_data)

with open("age_update.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(temp_data)
