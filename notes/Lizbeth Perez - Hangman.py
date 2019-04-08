import random

word_bank = ["i am starving", "bAckpack", "clock", "sweaters", "pizza", "i like turtles", "tables", "camels",
             "dora the explorer", "did you do your homework"]
guesses_left = 8
letters_guessed = []
word = random.choice(word_bank)
real_letters = list(word)

word_list = list(word.lower())

for character in word_list:
    current_index = word_list.index(character)
    word_list.pop(current_index)
    word_list.insert(current_index, "_")
print("".join(word_list))

while guesses_left > 0:
    word = list(word)
    if word_list == real_letters:
        print("You guessed correctly. ")
        exit()
    guess = input("Guess a letter.").lower()
    print("you guessed the letter %s" % guess)
    letters_guessed.append(guess)
    while guess in word:
        current_index = word.index(guess)
        word.pop(current_index)
        word.insert(current_index, "-")
        word_list.pop(current_index)
        word_list.insert(current_index, real_letters[current_index])
        print("".join(word_list))
        print("The letters you have guessed are %s" % letters_guessed)
    if guess not in word_list:
        guesses_left -= 1
        print("You have %s guesses left" % guesses_left)
        print("The letters you have guessed are %s" % letters_guessed)


if guesses_left == 0:
    print("You Lost!!!")
