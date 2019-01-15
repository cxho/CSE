import random
import string

word_bank = ["i am starving", "Backpack", "clock", "sweaters", "pizza", "i like turtles", "tables", "camels",
             "Dora the Explorer", "did you do your homework?"]
guesses_left = 8
letters_guessed = []
word = random.choice(word_bank)

string1 = word
word_list = list(string1)
print(word_list)

while guesses_left > 0:
    guess = input("Guess a letter.")
    letters_guessed.append(guess)
    print("you guessed the letter %s" % guess)
