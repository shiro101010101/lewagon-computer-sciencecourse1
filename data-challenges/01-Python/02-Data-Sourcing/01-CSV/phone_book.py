import csv

with open('data/phone_book.csv') as csv_file:
    reader = csv.DictReader(csv_file, skipinitialspace=True)

    for row in reader:
        print (row["last_name"]+":"+row["phone_number"])
