import csv


invalid = []


def validate(num: str):
    if len(num) == 16:
        last_num = num[15]
        num = list(num)
        num.pop(15)
        reversed_version = reverse_num(num)
        # print(reversed_version)
        for index in range(len(reversed_version)):
            reversed_version[index] = int(reversed_version[index])
        # print(reversed_version)

        new_list = multiply_odd_num(reversed_version)
        # print(new_list)
        if int(last_num) == add_all_nums(new_list) % 10:
            return True
    else:
        invalid.append(num)
    return False


def reverse_num(num: list):
    return num[:: - 1]


def multiply_odd_num(num: list):
    for index in range(len(num)):
        if index % 2 == 0:
            num[index] *= 2
        if num[index] > 9:
            num[index] -= 9
    return num


def add_all_nums(num: list):
    add = (num[0] + num[1] + num[2] + num[3] + num[4] + num[5] + num[6] + num[7] + num[8] + num[9] + num[10] + num[11] +
           num[12] + num[13] + num[14])
    return add


with open("Book1.csv", "r") as old_csv:
    with open("MyNewFile.csv", "w", newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("processing...")
        for row in reader:
            old_number = row[0]  # String
            first_num = int(old_number[0])
            if validate(old_number):
                writer.writerow(row)
        print("ok")
