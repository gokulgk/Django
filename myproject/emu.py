import csv 

with open('log.csv', 'r') as file:
    reader = csv.reader(file)
    rows = list(reader)

# Get the first row (header) of the CSV file
header = rows[0]

# Open the CSV file in write mode and write the header row back to the file
with open('log.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)