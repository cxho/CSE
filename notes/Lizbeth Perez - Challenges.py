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
