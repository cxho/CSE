import csv


def check(num: list):
    if 'Fruits' in row:
        if row[13] >= old_csv:
            return True
    return False


with open("SalesRecords.csv", "r") as old_csv:
        reader = csv.reader(old_csv)
        print("processing...")
        for row in reader:
            profits = row[13]
            print(profits)
