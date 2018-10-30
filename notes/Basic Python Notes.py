'''
print("Hello World!")
print()
# This is a Comment. I can write whatever I want
# Here and it won't do anything about it.
# It has no effect on the code.
print()  # This adds extra spaces onn the terminal
print("This will print here. Notice the Spacing.")

a = 4
b = 3
print(a+b)
print(a * 5)
print(5 - 3)
print(6 / 5)  # Results in an float (with decimals)

print("Figure this out")
print(6 // 4)  # Results in an integer (Without Decimals)
print(12 // 3)
print(9 // 4)

# more math stuff
print("Figure this stuff out too...")
print(6 % 4)
print(5 % 3)
print(9 % 4)


# variables
car_name = "The Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 1024
car_miles_per_gallon = 0.01

print("I have a car called %s. It's pretty nice." % car_name)

# Input
# name = input("what is your name? ")
# print("hello %s" % name)

# Auto-Comment - Ctrl + /
# age = input ("How old are you? ")
# print("%s?! You belong in a museum")

# Hidden age
real_age = int(input("How old are you? >_"))
hidden_age = real_age + 5
print(hidden_age)
print("%d is incredibly old. You are actually %d old." % (hidden_age, real_age))
'''

# functions
def printHelloWorld():
    print("Hello World!")


printHelloWorld()
'''
This is a multi-line comment
I can type anywhere here/
'''


# f(x) = 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)

# Loops
for i in(1, 2, 3):
    printHelloWorld()

print()
for i in range(10):
    printHelloWorld()

print()
for i in range(5):  # Range starts at 0 and goes to 4
    f(i)

for i in range(5):
    print(i**2)


a = 0
# While loops
while a < 10:
    print(a)
    a += 1  # This is the same thing as a = a + 1
