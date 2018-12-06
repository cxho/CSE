def challenge1(first_name, last_name):
    print(last_name, first_name)


challenge1("Bob", "Dole")

# Challenge 2
number = int(input("enter a number."))
mod = number % 2
if mod > 0:
    print("This is a odd number")
else:
    print("This is an even number.")


# Challenge 3
b = int(input("What is the base of the triangle?"))
h = int(input("What is the height of the triangle?"))

area = b*h/2

print("area", area)


# Challenge 4
number = int(input("Enter a number."))
if number == 0:
    print("This number is zero.")
elif number > 0:
    print("This number is positive.")
elif number < 0:
    print("This number is negative.")


# Challenge 5
r = int(input("What is the radius of a circle"))
pi = 3.14
area2 = pi*r**2
print("area", area2)


# Challenge 6
r = int(input("What is the radius of the sphere?"))
pi = 3.14
volume = 4/3*pi*r**3
print("volume", volume)


# Challenge 7
n = int(input("Enter a number."))
answer = n+n*n+n**3
print(answer)


# Challenge 8
a = int(input("Enter a number."))
if a == 2000 - 150 or a == 3000 - 150:
    print("This number is within 150 of 2000 or 3000.")
elif a < 2000 - 150 or a < 3000 - 150:
    print("This number is not within 150 of 2000 and 3000")
elif a == 2000 + 150 or a == 3000 + 150:
    print("This number is within 150 of 2000 and 3000")
elif a > 2000 + 150 or a > 3000 + 150:
    print("This number is not within 150 of 2000 or 3000")
elif a == 2000 or 3000:
    print("This number is within 150 of 3000 or 2000")


# Challenge 9
def is_vowel(char):
    letters = "aeiou"
    return char in letters


print(is_vowel('a'))
print(is_vowel('l'))
print(is_vowel('i'))
print(is_vowel('o'))
print(is_vowel('t'))

