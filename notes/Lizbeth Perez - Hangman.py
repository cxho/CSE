import random

word_bank = ["i am starving", "Backpack", "clock", "sweaters", "pizza", "i like turtles", "tables", "camels",
             "Dora the Explorer", "did you do your homework?"]
guesses_left = 8
letters_guessed = []
word = random.choice(word_bank)

string1 = word
word_list = list(string1)

for character in word_list:
    current_index = word_list.index(character)
    word_list.pop(current_index)
    word_list.insert(current_index, "_")
print("".join(word_list))

print(word)

while guesses_left > 0:
    guess = input("Guess a letter.")
    word_list = list(word_list)
    if guess in word:
        current_index = word.index(guess)
        word_list.pop(current_index)
        word_list.insert(current_index, guess)
        word_list = "".join(word_list)
        print(word_list)
        print("you guessed the letter %s" % guess)
    if guess not in word_list:
        print(guesses_left)
        guesses_left -= 1

print(letters_guessed)
