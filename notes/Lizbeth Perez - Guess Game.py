# Random Numbers
import random
number = random.randint(0, 10)
random_guess = int(input("Guess a number between 0 and 10."))
guesses_left = 5
win = False
while guesses_left > 0 and not win:
    if random_guess < number:
        print("The number is too low.")
        random_guess = int(input("Guess again."))
        guesses_left -= 1
    elif random_guess > number:
        print("Your number was too high.")
        random_guess = int(input("Guess again."))
        guesses_left -= 1
    elif random_guess == number:
        print("You guessed right.")
        break
