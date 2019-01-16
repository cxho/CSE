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
    for guess in letters_guessed:
        if guess == list(string.ascii_letters):
            current_index = letters_guessed.index(guess)
            letters_guessed.pop(current_index)
            letters_guessed.insert(current_index, "_")
            print(letters_guessed)
        else:
            guesses_left -= 1
            print(guesses_left)
            print(letters_guessed)
