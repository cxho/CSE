import random

money = 15
rounds = 0
most_money = money
best_rounds = most_money
while money > 0:
    number1 = random.randint(1, 6)
    number2 = random.randint(1, 6)
    if number1 + number2 == 7:
        print(number1 + number2)
        money += 4
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
    if money > most_money:
        most_money = money
        best_rounds = rounds
print("Sorry you lost. You played %d rounds" % rounds)
print("The most amount of money you had was %d dollars" % most_money)
print("The round with the most amount of money was %d." % best_rounds)
