#reading a csv file
import csv
filename = "aapl.csv"  # File name
fields = []  # Column names
rows = []    # Data rows

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:     # Read rows
        rows.append(row)

    print("Total no. of rows: %d" % csvreader.line_num)  # Row count

print('Field names are: ' + ', '.join(fields))

print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s" % col, end=" ")
    print('\n')

#writing into a csv file
import csv

# Define header and data rows
fields = ['Name', 'Branch', 'Year', 'CGPA']
rows = [
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

filename = "university_records.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)        # Create writer object
    csvwriter.writerow(fields)             # Write header
    csvwriter.writerows(rows)              # Write multiple rows