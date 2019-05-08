import csv


with open("SalesRecords.csv", "r") as old_csv:
    with open("BestProfits.csv", "w", newline="") as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")
        for row in reader:
            
print("ok")
