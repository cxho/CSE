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
# print("hello %s" % name)
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


# While loops
a = 0
while a < 10:
    print(a)
    a += 1  # This is the same thing as a = a + 1

'''
Hints with loops: 
For loops - use when you know EXACTLY how many iterations
While loops - Use when you DON'T know how many iterations
'''

# Random numbers
import random  # This should always be on line 1
print(random.randint(0, 100))


# Control Statements
def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D+"
    else:
        return "F"


print(grade_calc(90))

# Equality Statements
print(5 > 3)
print(5 >= 3)
print(3 == 3)
print(3 != 4)
'''
a = 3 # A is set to equal 3
a==3 # Is a equal to 3?
'''

# Lists
shopping_list = ["whole milk", "PC", "Eggs", "Switch"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length of the list is %d" % len(shopping_list))

# Changing Elements in a List
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for item in shopping_list:
    print(item)

'''
1. Make a list
2. Change the 3rd thing in the list
3. Print the item
4. Print the full list
'''

# List
school_items = ["backpack", "notebook", "pencils", "binder"]
school_items[2] = "pens"
print("The last thing in the list is %s" % school_items[len(school_items) - 1])
print(school_items)

# Getting part of a list
print(school_items[1:3])
print(school_items[1:4])
print(school_items[1:])
print(school_items[:2])

# Adding things to a list
holiday_list = [] # ALWAYS USE SQUARE BRACKETS
holiday_list.append("Tacos")
holiday_list.append("Bumblebee")
holiday_list.append("Red Dead Redemption 2")
print(holiday_list)
# Notice this is "object.method(Parameters)"

# Removing things from a list
holiday_list.remove("Tacos")
print(holiday_list)

'''
1. make a new list with 3 items
2. add a 4th item to the list
3. remove one of the first three items from the list
'''

electronics_list = ["phone", "laptop", "television"]
electronics_list.append("tablet")
electronics_list.remove("television")
print(electronics_list)

# ALSO removing things from a list
holiday_list.pop(0)  # Removes the item at index 0
print(holiday_list)

# Tuple
brands = ("apple", "Samsung", "HTC")
colors = ['blue', 'pink', 'orange', 'yellow', 'green', 'purple', 'black',
          'red', 'teal', 'gold', 'brown', 'cyan', 'magenta', 'turquoise', 'white', 'gray']
print(len(colors))

# Find the index
print(colors.index("gold"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

for character in list1:
    if character == "u":
        # replace with a *
        current_index = list1.index(character)
        list1.pop(current_index)
        list1.insert(current_index, "*")

# Changing lists into strings
print("".join(list1))

# Function Practice

def pythagorean