import csv


invalid = []


def validate(num: str):
    if len(num) == 16:
        num = list(num)
        num.pop(15)
        return True
    else:
        invalid.append(num)
    return False


def reverse_num(num: str):
    print(num[:: - 1])


def multiply_odd_num(num: str):
    if num[0: 15: 2]:
        multiply = num[0: 15: 2]
        multiply *= 2
        if multiply > 9:
            multiply -= 9
