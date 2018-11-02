# Random Numbers
import random
a = (random.randint(0, 10))
random_guess = int(input("Guess a number between 0 and 10."))
if random_guess < a:
    print("The number is lower.")
    random_guess = int(input("Guess again."))
elif random_guess > a:
    print("Your number was too high.")
    random_guess = int(input("Guess again."))
elif random_guess == a:
    print("You guessed right.")
