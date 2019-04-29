import csv


invalid = []


def validate(num: str):
    if len(num) == 16:
        last_num = int(num[15])
        num -= last_num
        num = num[:: - 1]
        odd_nums = % 2 = 1

    else:
        invalid.append(num)


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w") as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")
        print("you will drown")
        for row in reader:
            old_number = row[0]  # String
            first_num = int(old_number[0])
            if validate(old_number):
                writer.writerow(row)
        print("ok")