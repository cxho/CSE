import random

money = 15
rounds = 1
while money > 0:
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    if number1 + number2 == 7:
        print(number1 + number2)
        money += 5
        print("You got 5 more dollars")
        rounds += 1
    elif number1 + number2 > 7:
        print(number1 + number2)
        money -= 1
        print("Sorry, you lost one dollar")
        rounds += 1
    elif number1 + number2 < 7:
        print(number1 + number2)
        money -= 1
        print("Sorry, you lost one dollar")
        rounds += 1
print("Sorry you lost. You played %d rounds" % rounds)
