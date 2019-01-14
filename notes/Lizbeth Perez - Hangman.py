import random
word_bank = ["i am starving", "Backpack", "clock", "sweaters", "pizza", "i like turtles", "tables", "camels",
             "Dora the Explorer", "did you do your homework?"]
guesses_left = 8
letters_guessed = []
word = random.choice(word_bank)
print(word)

string1 = word
list1 = list(string1)
print(list1)

guess = input("Guess a letter.")
letters_guessed.append(guess)
print("you guessed the letter %s" % guess)
8