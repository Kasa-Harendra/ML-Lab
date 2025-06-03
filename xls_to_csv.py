import csv
import sys

def isnum(num):
    return (num[0].isdigit() and not (':' in num))

file = open(f'{sys.argv[1]}.csv', 'r')
file_out = open(f'{sys.argv[1]}_new.csv', 'w', newline='')

reader = csv.DictReader(file)
writer = csv.writer(file_out, delimiter=',')

header = [val.strip("'") for val in list(reader.fieldnames)[0].split(",")]
print(header)
writer.writerow(header)

for row in reader:
    data = [val.strip("'") for val in list(row.values())[0].split(',')]
    real_data = []
    for val in data:
        if isnum(val):
            real_data.append(float(val))
        else:
            real_data.append(val)
    writer.writerow(real_data)
    